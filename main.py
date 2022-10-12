import csv

# Загрузить данные из csv
data = []
with open('datasets/ads.csv', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(row)


# Запись в файл author.csv
authors = []
for i in data:
    if i != data[0]:
        authors.append(i[2])
uniq_authors = set(authors)
count = 1
with open('author.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for author in uniq_authors:
        writer.writerow([count, author])
        count += 1

# Уникальные адреса
adr = []
for a in data:
    if a != data[0]:
        adr.append(a[5])
uniq_adr = set(adr)
count = 1
with open('address.csv', 'w', newline='', encoding='utf-8') as f:
    file = csv.writer(f)
    for idx in uniq_adr:
        file.writerow([count, idx])
        count += 1

adr_file = []
with open('address.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        adr_file.append(row)

authors_file = []
with open('author.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        authors_file.append(row)

with open('new.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for d in data[1:]:
        for author in authors_file:
            if d[2] == author[1]:
                d[2] = author[0]
        for adr in adr_file:
            if d[5] == adr[1]:
                d[5] = adr[0]
        writer.writerow(d)



