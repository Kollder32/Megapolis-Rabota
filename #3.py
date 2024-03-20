import csv
with open("S:\\11В_2023_2024\\Цыганков Дмитрий\\Работа Мегаполис\\space.txt", encoding="utf8") as f:
    reader = csv.DictReader(f, delimiter=',', quotechar='"')
    dat = sorted(reader, key=lambda x: x[-])
id_project = input()
while id_project != 'stop':
    id_project = int(id_project)
