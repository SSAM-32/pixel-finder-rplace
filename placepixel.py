import csv

FilePath = ""
coords = ""

with open(FilePath) as file:
    reader = csv.reader(file, delimiter =',')
    for row in reader:
        if row[3] == coords:
            print(row)
