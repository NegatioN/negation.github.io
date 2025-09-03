#!/usr/bin/env python3

import argparse
from datetime import datetime
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

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
    quote = quote.replace('"', '\\"')
    print(fr'"{repr(quote)}","{args.author}","{args.origin}", "{args.origin_url}","{datetime.now().strftime("%Y-%m-%d")}","{args.typ}"')
    return 0

if __name__ == "__main__":
    exit(main())