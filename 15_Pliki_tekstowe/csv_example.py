import csv
import os
print(os.getcwd())
with open('data\\foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open('data\\foods.csv') as csvfile:
    for line in csvfile:
        print(line.strip().strip(','))
        n += 1
