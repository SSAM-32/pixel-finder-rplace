import csv
from PIL import Image, ImageColor

wh = 2000
img  = Image.new( mode = "RGB", size = (wh, wh) )
a = False

FilePath = ""
UserID = ""

with open(FilePath) as file:
    reader = csv.reader(file, delimiter =',')
    for row in reader:
        if a and row[1] == UserID:
            coords = row[3].split(",")
            img.putpixel( (int(coords[0]),int(coords[1])), ImageColor.getcolor(row[2], "RGB") )
            print(row)
        else:
            a = True
img.show()

