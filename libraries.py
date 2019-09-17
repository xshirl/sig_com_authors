import requests
import base64
import json
import glob
import uuid
        
PATCH_url = 'http://[::1]:3000/signature-commons-metadata-api/%s'
username = 'admin'
password = 'admin'
credential = base64.b64encode('{username}:{password}'.format(username=username, password=password).encode()).decode()

for i in glob.glob("out/*.json"):
    with open(i) as o:
        auth = json.loads(o.read())
        data = {
            "id": str(uuid.uuid4()),
            resources: uuid,
            "meta": {
                "$validator":"https://raw.githubusercontent.com/xshirl/sig_com_authors/master/validator.json",
                "Author's name" : auth["author name"],
                "Institution": auth["institution name (large institutions only)"],
                "Country": auth["country associated with most recent institution"],
                "Number of papers 1960-2018": auth["# papers 1960-2018"],
                "Year of first publication": auth["year of first publication"],
                "Year of last publication": auth["year of most recent publication"],
                "Rank based on composite score c, self-citations excluded": auth["rank based on composite score c, self-citations excluded"],
                "Total citations 1996-2018, self-citations excluded":auth["total cites 1996-2018, self-citations excluded"],
                "H-index as of end-2018, self-citations excluded": auth["h-index as of end-2018, self-citations excluded"],
                "Hm-index as of end-2018, self-citations excluded": auth["hm-index as of end-2018, self-citations excluded"],
                "Number of single authored papers, self-citations excluded": auth["number of single authored papers, self-citations excluded"],
                "Total citations to single authored papers, self-citations excluded":auth["total cites to single authored papers, self-citations excluded"],
                "Number of single+first authored papers, self-citations excluded":auth["number of single+first authored papers, self-citations excluded"],
                "Total cites to single+first authored papers, self-citations excluded": auth["total cites to single+first authored papers, self-citations excluded"],
                "Number of single+first+last authored papers, self-citations excluded": auth["number of single+first+last authored papers, self-citations excluded"],
                "Total cites to single+first+last authored papers, self-citations excluded":auth["total cites to single+first+last authored papers, self-citations excluded"],
                "composite score, self-citations excluded": auth["composite score, self-citations excluded"],
                "Number of distinct citing papers, self-citations excluded": auth["number of distinct citing papers, self-citations excluded"],
                "Ratio of total citations to distinct citing papers, self-citations excluded": auth["ratio of total citations to distinct citing papers, self-citations excluded"],
                "Self-citation percentage": auth["self-citation percentage"],
                "Rank based on composite score c": auth["rank based on composite score c"],
                "Total cites 1996-2018": auth["total cites 1996-2018"],
                "H-index as of end-2018": auth["h-index as of end-2018"],
                "Hm-index as of end-2018": auth["hm-index as of end-2018"],
                "Number of single authored papers": auth["number of single authored papers"],
                "Total cites to single authored papers": auth["total cites to single authored papers"],
                "Number of single+first authored papers": auth["number of single+first authored papers"],
                "Total cites to single+first authored papers": auth["total cites to single+first authored papers"],
                "Number of single+first+last authored papers": auth["number of single+first+last authored papers"],
                "Total cites to single+first+last authored papers": auth["total cites to single+first+last authored papers"],
                "Composite score": auth["composite score"],
                "Number of distinct citing papers": auth["number of distinct citing papers"],
                "Ratio of total citations to distinct citing papers": auth["ratio of total citations to distinct citing papers"],
                "Top ranked Science-Metrix category (out of 186) for author": auth["top ranked Science-Metrix category (out of 186) for author"],
                "Name of top ranked Science-Metrix category for author": auth["name of top ranked Science-Metrix category for author"],
                "Fraction of AR+RE+CP in Science-Metrix category for author": auth["fraction of AR+RE+CP in Science-Metrix category for author"],
                "Second ranked Science-Metrix category (out of 186) for author" : auth["second ranked Science-Metrix category (out of 186) for author"],
                "Associated category name (name2)": auth["associated category name (name2)"],
                "Associated category fraction (frac2)": auth["associated category fraction (frac2)"],
                "Top ranked higher-level Science-Metrix category (out of 22) for author": auth["top ranked higher-level Science-Metrix category (out of 22) for author"],
                "Associated category name (name22)": auth["associated category name (name22)"],
                "Associated category fraction (frac22)": auth["associated category fraction (frac22)"]

            },
            "dataset": "authors",
            "dataset_type": "geneset_library"
        }
        res = requests.request("POST", PATCH_url%"libraries",
            headers={"Content-Type": "application/json", 'Authorization': 'Basic {credential}'.format(credential=credential)},
            json=data
        )
        if not res.ok:
            print(res.json())
            break

