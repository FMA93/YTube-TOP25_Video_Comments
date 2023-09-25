import pandas as pd
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

# Here you need to fill in your API Key after you've enabled Youtube Data to your Google Cloud Console Project
# YouTube Data API credentials (obtained from Google Cloud Console, have ot create a free dev account)
API_KEY = "Your_API_Key"  # Replace with your API key

# Replace 'VIDEO_URL' with the YouTube video URL you want to fetch comments from
video_url = "VIDEO_URL"

# Extract video ID from the URL
parsed_url = urlparse(video_url)
video_id = parse_qs(parsed_url.query).get("v")
if video_id:
    video_id = video_id[0]
else:
    raise ValueError("Invalid YouTube video URL")

# Create a YouTube Data API client using your API key
youtube = build("youtube", "v3", developerKey=api_key)

# Function to fetch top comments
def fetch_top_comments(video_id, max_results=25):
    comments = []
    next_page_token = None

    while len(comments) < max_results:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText",
            pageToken=next_page_token,
            order="relevance",
        )
        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append(comment)

        next_page_token = response.get("nextPageToken")

        if next_page_token is None:
            break

    return comments[:max_results]

# Format date and time
def format_datetime(raw_datetime):
    dt = pd.to_datetime(raw_datetime)
    formatted_date = dt.strftime("%d-%m-%Y")
    formatted_time = dt.strftime("%H:%M")
    return formatted_date, formatted_time

# Fetch top comments
comments = fetch_top_comments(video_id)

# Initialize lists to store data
users = []
comment_texts = []
likes = []
dates = []
times = []

# Extract data from comments
for comment in comments:
    users.append(comment["authorDisplayName"])
    comment_texts.append(comment["textDisplay"])
    likes.append(comment["likeCount"])
    formatted_date, formatted_time = format_datetime(comment["publishedAt"])
    dates.append(formatted_date)
    times.append(formatted_time)

# Create a DataFrame to store the data (without the "Dislikes" column)
data = {
    "User": users,
    "Comment": comment_texts,
    "Likes": likes,
    "Date": dates,
    "Time": times
}

df = pd.DataFrame(data)

# Sort the DataFrame by "Likes" column in descending order
df = df.sort_values(by="Likes", ascending=False)

# Export the data to an Excel file
excel_file = "top_comments.xlsx"
df.to_excel(excel_file, index=False, engine="openpyxl")

print(f"Top {len(comments)} comments exported to {excel_file}")