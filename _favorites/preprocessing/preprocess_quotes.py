import csv
from pathlib import Path

if __name__ == "__main__":
    with open('quotes', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        output = [{'text': row[0], 'author': row[1], 'num': i} for i, row in enumerate(reader)]
        for item in output:
            fname = Path('..', f'quote_{item["num"]}.md')
            if not fname.is_file():
                with open(fname, 'w') as f:
                    f.write(f"---\ntext: >\n  \"{item['text']}\" - {item['author']}\ntype: quote\n---\n")
