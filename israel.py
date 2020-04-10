from urllib3.exceptions import InsecureRequestWarning
import re
import urllib3
from json import loads
from bs4 import BeautifulSoup
from requests import get
import json

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from openpyxl import Workbook, load_workbook

http = urllib3.PoolManager(cert_reqs="CERT_NONE")

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
    newlist.append([ele for ele in cols])
# ['', '21/02/2020', '2', '2', '', '', '']

newlist.remove([""])
[r.pop(0) for r in newlist]
newlist = np.array(newlist)

for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        if newlist[i][j] == "":
            newlist[i][j] = "0"
            # newlist[i][j] = 0

title = ['Date', "Total Cases", "New Cases",
         "בינוני Moderate", "קשה Severe", "נפטרו Deceased"]
# print(newlist)
df = pd.DataFrame(newlist, columns=title)
print(df)

lastrow = newlist[-1]  # get the last row

lastrow = pd.DataFrame(lastrow)
# print(lastrow)


writer = pd.ExcelWriter(
    '/Users/user/Documents/Web/charts and graphs/apexchart/backend/data.xlsx', engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook('data.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel('data.xlsx')
# print(len(reader)+1)
# write out the new sheet
df.to_excel(writer, index=False, header=False, startrow=1)

writer.close()

# with open("/Users/user/PycharmProjects/soldgame/fun/data.csv", "w") as f:
#     f.write(str(lastrow))
#[f.write(str(key) + "\n\n") for key in newlist]
