# YouTube Top Comments Extractor

This Python script fetches the top comments from a YouTube video using the YouTube Data API and stores them in an Excel file. It utilizes the `pandas` library for data manipulation and the `google-api-python-client` library to interact with the YouTube Data API.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/)

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt



Obtaining a YouTube Data API Key
To use the YouTube Data API, you need to obtain an API Key from the Google Cloud Console. Follow these steps:

Create a free developer account on Google Cloud Console if you don't already have one.

Enable the YouTube Data API for your project.

Generate an API Key.

Replace "Your_API_Key" in the script with your API key.



Usage
Replace "VIDEO_URL" with the URL of the YouTube video from which you want to fetch top comments.

Run the script using the following command:

python youtube_top_comments.py


The script will fetch the top comments, including user names, comment text, likes, and timestamps.

The data is stored in an Excel file named top_comments.xlsx.



Customization
You can modify the max_results variable in the fetch_top_comments function to specify the maximum number of comments to fetch.

Customize the Excel file name by changing the excel_file variable.

You can further process or analyze the comment data as needed.



License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute to the project and report any issues or suggestions!




