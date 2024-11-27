# YouTube Transcript Scraper

A Python script that downloads transcripts from YouTube videos and organizes them by categories.

## Description

This tool allows you to batch download transcripts from YouTube videos using a structured input file. Videos can be organized by categories, and the transcripts will be saved in corresponding category folders.

## Features

- Supports both youtube.com and youtu.be URL formats
- Handles markdown-formatted links
- Organizes transcripts by categories
- Provides detailed console output during processing
- Handles errors gracefully

## Prerequisites
bash
pip install youtube-transcript-api


## Usage

1. Create a `youtube_links.txt` file with your video links organized by categories:

text
Category Name
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
Another Category
https://www.youtube.com/watch?v=VIDEO_ID_3
https://youtu.be/VIDEO_ID_4


2. Run the script:

bash
python youtubeScraper.py


3. Transcripts will be downloaded to category-specific folders (e.g., `category_name/VIDEO_ID.txt`)

## File Structure
├── youtubeScraper.py
├── youtube_links.txt
├── category_1/
│ ├── video1_transcript.txt
│ └── video2_transcript.txt
└── category_2/
├── video3_transcript.txt
└── video4_transcript.txt

## Input File Format

- Each category should be on its own line
- URLs should be listed under their respective categories
- Blank lines are ignored
- Supports both regular and markdown-formatted URLs

## Error Handling

- Invalid URLs are skipped
- Videos without available transcripts are logged
- Network errors are caught and reported

## Limitations

- Only works with videos that have available transcripts
- YouTube channel URLs are not supported
- Requires videos to be publicly accessible
