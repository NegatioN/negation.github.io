import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import sys
import re


def fetch_hackernews_comment(url):
    try:
        # Parse the URL to extract comment ID from anchor
        parsed_url = urlparse(url)
        comment_id = parsed_url.fragment  # Gets the part after #
        
        if not comment_id:
            print(f"No comment ID found in URL: {url}")
            return None
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        comment_row = soup.find('tr', id=comment_id)
        
        if not comment_row:
            print(f"Comment with ID {comment_id} not found")
            return None
            
        author_link = comment_row.find('a', class_='hnuser')
        author = author_link.get_text(strip=True) if author_link else 'Unknown'
        comment_span = comment_row.find('div', class_='body_html')

        return {'author': author, 'text': comment_span.decode_contents(), 'origin': 'Hacker News', 'origin_url': url, 'date': datetime.now().strftime('%Y-%m-%d')}
        
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
    except Exception as e:
        print(f"Error parsing comment from {url}: {e}")
        return None

def fetch_reddit_comment(url):
    try:
        json_url = url.rstrip('/') + '.json'
        response = requests.get(json_url)
        response.raise_for_status()

        data = response.json()
        comment_data = data[1]['data']['children'][0]['data']
        print(comment_data)

        return {
            'author': comment_data.get('author', 'Unknown'),
            'text': comment_data.get('body_html', '').strip(),
            'origin': 'Reddit',
            'origin_url': url,
            'id': f'reddit-{comment_data.get("id", "unknown")}',
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = sys.argv[1]
    if re.match(r'^https?://news\.ycombinator\.com/item\?id=\d+#\d+$', url):
        out = fetch_hackernews_comment(url)
    elif re.match(r'^https?://www.reddit.com.*', url):
        out = fetch_reddit_comment(url)
    else:
        print("Unsupported URL format. Please provide a valid Hacker News comment URL.")

    print('csv format:')
    yaml_text_block = out["text"].replace('\n', '\n  ').replace('"', '\\"')
    print(fr'"{repr(yaml_text_block)}","{out["author"]}","{out["origin"]}","{out["origin_url"]}","{out["id"]}","{out["date"]}"')