import csv, json

def to_json(src, dst):
    with open(src, encoding='utf-8') as f:
        rows = [r for r in csv.DictReader(f) if any(v.strip() for v in r.values())]
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f'{dst}: {len(rows)} rows')

to_json('data/mou.csv', 'data/mou.json')
to_json('data/calendar.csv', 'data/calendar.json')
to_json('data/people.csv', 'data/people.json')
