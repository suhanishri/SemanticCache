
from lib import *

ret = query("What is the diameter of sun?")
print("Query", ret)

metaid = getmetaid(ret)
print("metaid", metaid)

ret = getdoc(metaid)
print("GetDoc", ret)
