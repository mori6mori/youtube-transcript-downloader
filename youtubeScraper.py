import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import urlparse, parse_qs

def clean_url(url):
    """Clean and validate YouTube URL"""
    url = url.strip()
    if not url.startswith('http'):
        return None
    # Remove any markdown formatting
    url = url.replace('[', '').replace(']', '')
    return url

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if not url:
        return None
    try:
        if "youtube.com" in url:
            parsed_url = urlparse(url)
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif "youtu.be" in url:
            return url.split("/")[-1]
    except Exception:
        return None
    return None

def download_transcript(url, output_path):
    """Download YouTube video transcript"""
    try:
        print(f"\nAttempting to get transcript from: {url}")
        video_id = get_video_id(url)
        if not video_id:
            print(f"Could not extract video ID from: {url}")
            return False
            
        # Get transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        # Create output file path using video ID (since we don't have access to title)
        output_file = os.path.join(output_path, f"{video_id}.txt")
        
        # Save transcript to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_transcript)
            
        print(f"Successfully downloaded transcript for video: {video_id}")
        return True
        
    except Exception as e:
        print(f"Error downloading transcript for {url}: {str(e)}")
        return False

def main():
    # Add these debug lines
    print(f"Current working directory: {os.getcwd()}")
    print(f"Does youtube_links.txt exist? {os.path.exists('youtube_links.txt')}")
    
    # Dictionary to store category and its URLs
    categories = {}
    current_category = None
    
    # Read the input text and organize URLs by category
    with open('youtube_links.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if 'youtube.com' not in line.lower() and 'youtu.be' not in line.lower():
                current_category = line.strip()
                categories[current_category] = []
            else:
                if current_category:
                    clean_link = clean_url(line)
                    if clean_link:
                        categories[current_category].append(clean_link)

    # Create directories and download transcripts
    for category, urls in categories.items():
        # Create category directory
        category_dir = category.lower().replace(' ', '_')
        os.makedirs(category_dir, exist_ok=True)
        
        print(f"\nProcessing category: {category}")
        for url in urls:
            print(f"Processing URL: {url}")
            download_transcript(url, category_dir)

if __name__ == "__main__":
    main()
    

