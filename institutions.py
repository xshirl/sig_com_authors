import json
import glob

institutions = set()
for i in glob.glob("*.json"):
    with open(i) as o:
        auth = json.loads(o.read())
        inst = auth["inst_name"]
        institutions.add(inst)
