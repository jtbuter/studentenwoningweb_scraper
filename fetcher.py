import requests
import math
import json

def sww_page(page):
    url = "https://www.studentenwoningweb.nl/webapi/zoeken/find/"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Connection": "close"
    }
    payload = {
        "url": "model[Regulier aanbod]~plaatsenwijken[Amsterdam,Diemen]",
        "command": "page[" + str(page) + "]",
        "hideunits": "hideunits[]"
    }

    return requests.post(url, headers=headers, json=payload).text

def sww_all():
    page = 1
    max = math.inf
    cumulative = []

    while page <= max:
        result = json.loads(sww_page(page))
        cumulative.append(result["Resultaten"])

        max = math.ceil(float(result["TotalSearchResults"]) / float(10))
        page += 1

    return cumulative
