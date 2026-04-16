import csv, json

def to_json(src, dst, skip_rows=0):
    with open(src, encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # ข้าม rows แรก แล้วใช้ row ถัดไปเป็น header
    rows = rows[skip_rows:]
    if not rows:
        json.dump([], open(dst, 'w', encoding='utf-8'))
        return
    
    headers = rows[0]
    data = []
    for row in rows[1:]:
        if not any(v.strip() for v in row):
            continue
        obj = {}
        for i, h in enumerate(headers):
            obj[h] = row[i] if i < len(row) else ''
        data.append(obj)
    
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{dst}: {len(data)} rows, headers: {headers[:5]}')

# MOU Sheet มี 2 header rows ข้ามไป 2 บรรทัด
to_json('data/mou.csv', 'data/mou.json', skip_rows=2)

# Calendar และ People ปกติ
to_json('data/calendar.csv', 'data/calendar.json', skip_rows=0)
to_json('data/people.csv', 'data/people.json', skip_rows=0)
