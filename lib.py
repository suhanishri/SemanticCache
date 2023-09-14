
import requests
import uuid
import json
import os
from libconstants import *

def upload(q, hdata):
    url = f"http://{HAYSTACK_IP}:8000/file-upload"

    payload = {'meta': json.dumps({"q":q, "intent": "cache", "id": str(uuid.uuid4())})}

    fname = "tmp_" + str(uuid.uuid4()) + ".txt"
    with open(fname, 'w') as f:
        f.write(hdata)

    files = { 'files': open(fname,'rb') }
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # Delete all tmp files
    for fname in os.listdir():
        if fname.startswith("tmp_"):
            os.unlink(fname)

    print('\t', f"upload(q={q}, hdata={hdata})", response.text)
    print()

def getdoc(metaid):
    url = f"http://{HAYSTACK_IP}:8000/documents/get_by_filters"
    headers = {
        'Accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {"filters": { "id": metaid }}
    response = requests.request("POST", url, headers=headers, data=payload)
    print('\t', f"getdoc(metaid={metaid})", response, response.json())
    print()
    return response.json()

def query(q):
    url = f"http://{HAYSTACK_IP}:8000/query"
    headers = {
        'Accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {"query": q }
    response = requests.request("POST", url, headers=headers, data=payload)
    print('\t', f"query(q={q})", response, response.json())
    print()
    return response.json()