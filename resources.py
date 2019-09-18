import requests
import base64
import json
import glob
import uuid
import json

PATCH_url = 'http://[::1]:3000/signature-commons-metadata-api/%s'
username = 'admin'
password = 'admin'
credential = base64.b64encode('{username}:{password}'.format(username=username, password=password).encode()).decode()

with open("query.json") as o:
    institutionsWiki = json.loads(o.read())


with open("institutions.txt", 'r') as f:
    institutions = f.read().split('\n')
    
for i in institutions:
    for inst in institutionsWiki:
        data = {
        "id": str(uuid.uuid4()),
        "meta": {
            "$validator": "https://raw.githubusercontent.com/xshirl/sig_com_authors/master/institutionValidator.json",
            "Institution name": i,
            "Country":  inst["countryName"] if i == inst["name"] else "",
            "Url": inst["url"] if i == inst["name"] else "",
            "Logo": inst["logo"] if i == inst["name"] else ""
        },
         "dataset": "institutions",
        "dataset_type": "geneset_library" 
        }
        res = requests.request("POST", PATCH_url%"resources",
                    headers={"Content-Type": "application/json", 'Authorization': 'Basic {credential}'.format(credential=credential)},
                    json=data
                )
        if not res.ok:
            print(res.json())
            break
