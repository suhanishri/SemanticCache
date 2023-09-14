import argparse
from lib import *

if __name__ == "__main__":
    print("Enter query ")
    q = input()

    ret = query(q)
    print("Query", ret)

    metaid = getmetaid(ret)
    print("metaid", metaid)

    ret = getdoc(metaid)
    print("GetDoc", ret)

    print("Response", ret[0])
