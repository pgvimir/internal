import csv, json

def csv_to_json(src, dst, header_row=0):
    with open(src, encoding='utf-8') as f:
        rows = list(csv.reader(f))
    
    headers = rows[header_row]
    data = []
    for row in rows[header_row+1:]:
        if not any(v.strip() for v in row):
            continue
        obj = {headers[i]: (row[i] if i < len(row) else '') for i in range(len(headers))}
        data.append(obj)
    
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{dst}: {len(data)} rows | headers: {headers[:6]}')

# MOU: row 0-1 = title/blank, row 2 = headers จริง
csv_to_json('data/mou.csv', 'data/mou.json', header_row=2)

# Calendar และ People: header row 0
csv_to_json('data/calendar.csv', 'data/calendar.json', header_row=0)
csv_to_json('data/people.csv', 'data/people.json', header_row=0)
