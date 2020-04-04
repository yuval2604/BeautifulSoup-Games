import re
import urllib3
from json import loads
from bs4 import BeautifulSoup
from requests import get
import json

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

http = urllib3.PoolManager(cert_reqs="CERT_NONE")
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

url = "https://github.com/idandrd/israel-covid19-data/blob/master/IsraelCOVID19.csv"

data_received = http.request("GET", url).data
soup = BeautifulSoup(data_received, "html.parser")
body = soup.find_all("tr", class_="js-file-line")

newlist = []

for row in body:
    arr = []
    cols = row.find_all("td")

    cols = [ele.text.strip() for ele in cols]
    print(cols)
    newlist.append([ele for ele in cols])
# print(newlist)

newlist.remove([""])
[r.pop(0) for r in newlist]

newlist = np.array(newlist)

for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        if newlist[i][j] == "":
            newlist[i][j] = "0"
            # newlist[i][j] = 0
# new = map(lambda x: list(x.replace("", "0")), newlist)
# print(list(new))
# newlist = [r.replace("", "0") for r in newlist]

# a = [map(lambda r: r, key) for key in newlist]

# a = map(lambda r: r, newlist)
# print(list(a))

with open("israel.csv", "w") as f:
    [f.write(str(key) + "\n\n") for key in newlist]
