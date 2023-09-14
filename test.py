
from lib import *

upload("How big is sun?", "How big is sun? *** The sun has a diameter of approximately 1.39 million kilometers (864,938 miles). It is so large that it accounts for about 99.86% of the total mass of the Solar System.")
print("Upload successful")

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
