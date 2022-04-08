import csv

FilePath = "/home/ssam/Documents/misc/place/2022_place_canvas_history.csv"
coords = "122,706"

with open(FilePath) as file:
    reader = csv.reader(file, delimiter =',')
    for row in reader:
        if row[3] == coords:
            print(row)
