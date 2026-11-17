import csv, datetime

times = []
with open('data.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        if row:
            times.append(row[0])

print("总行数:", len(times))

prev = None
gap = 0
for ts in times:
    t = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    if prev and (t - prev).total_seconds() > 10:
        print("断档:", prev, "→", ts)
        gap += 1
    prev = t

print("断档次数:", gap)
