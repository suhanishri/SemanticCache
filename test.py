
from lib import *

ret = query("What is the diameter of sun?")
print("Query", ret)

confidence = getconfidence(ret)
print("Confidence", confidence)

metaid = getmetaid(ret)
print("metaid", metaid)

ret = getdoc(metaid)
print("GetDoc", ret)
