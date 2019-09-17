import json
import glob

institution= set()
for i in glob.glob("out/*.json"):
    with open(i) as o:
        auth = json.loads(o.read())
        inst = auth["institution name (large institutions only)"]
        institution.add(inst)

with open("institutions.txt", "w") as f:
    for item in institution:
        f.write("%s\n" % item)
