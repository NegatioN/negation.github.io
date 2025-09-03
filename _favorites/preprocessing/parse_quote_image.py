#!/usr/bin/env python3

import argparse
from datetime import datetime
from preprocess_quotes import create_id
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

def generate_favorites_file(quote, author, origin, typ="book", origin_url=""):
    """Generate the favorites markdown file"""
    quote_id = create_id(author, origin)
    content = f"""---
text: >
  "{quote}"
author: {author}
origin: 1
origin_url: {origin_url}
id: {quote_id}
date: {datetime.now().strftime('%Y-%m-%d')} 
type: {typ}
---
"""
    filepath = f"../{quote_id}.md"
    with open(filepath, 'w+') as f:
        f.write(content)
    
    return filepath

def doctr_parse(img_path):
    model = ocr_predictor(pretrained=True)
    # PDF
    doc = DocumentFile.from_images(img_path)
    return model(doc).render()

def main():
    parser = argparse.ArgumentParser(description='Extract quotes from images using OCR and format as favorites')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--author', required=True, help='Author name')
    parser.add_argument('--origin', required=True, help='Textual description of Origin')
    parser.add_argument('--origin-url', default="", help='Origin URL (optional)')
    parser.add_argument('--typ', default="book", help='Type of quote')

    args = parser.parse_args()
    
    try:
        quote = doctr_parse(args.image_path)
        print(f"Extracted quote: {quote}")
    except Exception as e:
        print(f"Error running OCR: {e}")
        return 1
    quote = quote.replace('"', '\\"').encode("unicode_escape").decode()
    print(fr'"{quote}","{args.author}","{args.origin_url}","{args.origin}","{datetime.now().strftime("%Y-%m-%d")}","{args.typ}"')

    try:
        filepath = generate_favorites_file(quote, args.author, args.origin, args.origin_url)
        print(f"Generated favorites file: {filepath}")
    except Exception as e:
        print(f"Error generating file: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())