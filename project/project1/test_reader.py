import csv
with open('boxoffice.csv', newline='', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movieCd'], row['movieNm'], row['audiAcc'], row['week'])