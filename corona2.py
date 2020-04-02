import re
import urllib3
from json import loads
from bs4 import BeautifulSoup
from requests import get
import json

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

http = urllib3.PoolManager(cert_reqs='CERT_NONE')
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

url ="https://corona.mako.co.il/"
URL = "https://z.ynet.co.il/fast/content/2020/coronavirus/status1.aspx"


data_received = http.request('GET', url).data
soup = BeautifulSoup(data_received, "html.parser")
body = soup.find_all('div', class_ = 'stats-box')

newlist= {}

# worldwide_sick
# worldwide_death
# israel_sick
# israel_death, israel_recoverd, israel_hard, israel_med, israel_koma, nothing 
print(len('<div class="flex-box">'))
for i in body:
    print(i)
    # json_data = json.dumps(str(i))
    a=i.contents[1].getText()
    b=i.contents[3].getText()
    # print(str(a), str(b))
    newlist[str(a)]=str(b)
print(newlist)


with open('my_file.txt', 'w') as f:
    [print(key,value) for key, value in newlist.items()]
    [f.write(str(key) + str(val) + '\n\n') for key,val in newlist.items()]




