import csv, json

def csv_to_json(src, dst, header_row=0, fiscal_year=None):
    with open(src, encoding='utf-8') as f:
        rows = list(csv.reader(f))
    headers = rows[header_row]
    data = []
    for row in rows[header_row+1:]:
        if not any(v.strip() for v in row):
            continue
        obj = {headers[i]: (row[i] if i < len(row) else '') for i in range(len(headers))}
        if fiscal_year:
            obj['ปีงบประมาณ'] = fiscal_year
        data.append(obj)
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{dst}: {len(data)} rows')

# MOU: header อยู่ row 2
csv_to_json('data/mou.csv', 'data/mou.json', header_row=2)

# Calendar
csv_to_json('data/calendar.csv', 'data/calendar.json', header_row=0)

# People: รวม 2 ปีงบประมาณ
import os
d1, d2 = [], []

with open('data/people_2526.csv', encoding='utf-8') as f:
    rows = list(csv.reader(f))
    headers = rows[0]
    for row in rows[1:]:
        if not any(v.strip() for v in row):
            continue
        obj = {headers[i]: (row[i] if i < len(row) else '') for i in range(len(headers))}
        obj['ปีงบประมาณ'] = '2025-2026'
        d1.append(obj)

with open('data/people_2425.csv', encoding='utf-8') as f:
    rows = list(csv.reader(f))
    headers = rows[0]
    for row in rows[1:]:
        if not any(v.strip() for v in row):
            continue
        obj = {headers[i]: (row[i] if i < len(row) else '') for i in range(len(headers))}
        obj['ปีงบประมาณ'] = '2024-2025'
        d2.append(obj)

all_people = d1 + d2
with open('data/people.json', 'w', encoding='utf-8') as f:
    json.dump(all_people, f, ensure_ascii=False, indent=2)
print(f'data/people.json: {len(all_people)} rows ({len(d1)} + {len(d2)})')
