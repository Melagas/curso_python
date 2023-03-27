import csv

with open ("archivos2\\datos.csv") as archivos:
    reader = csv.reader(archivos)
    for row in reader:
        print(row)