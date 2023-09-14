
import os, shutil, time
import json
from libconstants import *
from lib import *

if os.path.exists(OUTPUT):
    shutil.rmtree(OUTPUT)
    time.sleep(0.1)

os.mkdir(OUTPUT)

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
