import csv

with open("employees.csv", 'a', encoding="utf-8") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Brumbál", 3000])
    writer.writerow(["Harry", 2000])
    writer.writerow(["Potter", 10])