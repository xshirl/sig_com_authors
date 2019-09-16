import json
import csv

key_map = {}
with open("keymap.tsv") as o:
    csvreader = csv.reader(o, delimiter="\t")
    for row in csvreader:
        key_map[row[0]] = row[2]

with open("authors_edited.json") as o:
    authors = json.loads(o.read())

authors2 = []
for auth in authors:
    auth2 = {}
    for key, value in auth.items():
        auth2[key_map[key]] = value
    authors2.append(auth2)
# for i in authors2:
#     print(i["author name"])
# print(authors2)

for auth in authors2:
    filename="out/%s.json"%auth["author name"]
    with open(filename, "w") as o:
        json.dump(auth, o, indent=4)
        print(filename)

