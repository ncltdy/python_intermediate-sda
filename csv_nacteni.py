import csv

with open("employees.csv", encoding="utf-8") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)