
from lib import *

ret = query("What is the diameter of sun?")
print("Query", ret)

docs = ret["documents"]
if len(docs) <= 0:
    print("No docs in response")
    exit()
metaid = docs[0]["meta"]["id"]
print("metaid", metaid)
ret = getdoc(metaid)
print("GetDoc", ret)
