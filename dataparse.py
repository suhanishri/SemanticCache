
import os, shutil, time
import json
import requests
import uuid

INPUT = "alpaca_data.json"
OUTPUT = "haystack-data"
SEP = " *** "
HAYSTACK_IP = '10.1.0.4'

if os.path.exists(OUTPUT):
    shutil.rmtree(OUTPUT)
    time.sleep(0.1)

os.mkdir(OUTPUT)

def upload(q, hdata):
    url = f"http://{HAYSTACK_IP}:8000/file-upload"

    payload = {'meta': {"q":q, "id": str(uuid.uuid4())}}

    fname = str(uuid.uuid4())
    with open(fname, 'w') as f:
        f.write(hdata)

    # files=[
    #     ('files',(fname + '.json', open(fname,'rb'),'application/json'))
    # ]
    files = { 'files': open(fname,'rb') }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    os.unlink(fname)
    print('\t', response.text)

# Read file.
with open(INPUT) as f:
    data = f.read()
    jdata = json.loads(data)

    for idx, el in enumerate(jdata):
        print(idx, '/', len(jdata))
        q = el["instruction"]
        output = el["output"]

        hdata = q + SEP + output

        upload(q, hdata)
        print('\tDone')

