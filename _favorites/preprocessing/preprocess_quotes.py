import csv
from pathlib import Path
import hashlib
def create_id(author, text):
    h = hashlib.sha256(text.encode('utf-8'))
    return f'{author.lower().replace(" ", "_")}-{h.hexdigest()}'

if __name__ == "__main__":
    with open('quotes_arranged', 'r') as csvfile:
        reader = csv.reader(csvfile, quotechar='"', delimiter=',', escapechar='\\')
        headers = next(reader, None)
        output = [{'text': row[0], 'author': row[1], 'origin': row[2], 'origin_url': row[3], 'date': row[4], 'type': row[5]} for i, row in enumerate(reader)]
        for item in output:
            item_id = create_id(item['author'], item['text'])
            fname = Path('..', f'{item_id}.md')
            if not fname.is_file():
                with open(fname, 'w') as f:
                    f.write(f"---\ntext: >\n  {item['text']}\nauthor: {item['author']}\norigin: \"{item['origin']}\"\norigin_url: {item['origin_url']}\nid: {item_id}\ndate: {item['date']}\ntyp: {item['type']}\n---\n")
