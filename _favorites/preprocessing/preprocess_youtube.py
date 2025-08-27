import re
import requests
from datetime import datetime
import os
from pathlib import Path

def process_youtube_url(video_id):
    title = get_video_title(video_id)
    embed_link = f"https://www.youtube.com/embed/{video_id}"
    
    return {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "link": embed_link
    }

def extract_video_id(url):
    patterns = [r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})', r'youtube\.com/v/([a-zA-Z0-9_-]{11})']
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_video_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = requests.get(url)
        response.raise_for_status()
        
        title_match = re.search(r'<title>(.+?) - YouTube</title>', response.text)
        if title_match:
            return title_match.group(1).strip()
        else:
            return f"YouTube Video {video_id}"
            
    except requests.RequestException:
        return f"YouTube Video {video_id}"

if __name__ == "__main__":
    with open('youtube', 'r') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        video_id = extract_video_id(url)
        fname = Path('..', f'{video_id}.md')
        if video_id and not os.path.isfile(fname):
            result = process_youtube_url(video_id)
            with open(fname, 'w') as f:
                f.write(f"---\ntitle: {result['title']}\ndate: {result['date']}\nlink: {result['link']}\ntype: video\n---\n")

