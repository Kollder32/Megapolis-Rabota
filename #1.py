import csv
with open("S:\\11В_2023_2024\\Цыганков Дмитрий\\Работа Мегаполис\\space.txt") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"' )
    answer = list(reader)[:1]



