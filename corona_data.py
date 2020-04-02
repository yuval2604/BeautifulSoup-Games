import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import re
import urllib3
from bs4 import BeautifulSoup
from sys import stdout
from collections import deque
import sys
import requests
from json import loads
http = urllib3.PoolManager(cert_reqs='CERT_NONE')
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from datetime import datetime

import time
starttime=time.time()
def job():

    url ="https://www.ynet.co.il/home/0,7340,L-8,00.html"
    URL = "https://z.ynet.co.il/fast/content/2020/coronavirus/status1.aspx"
    data_received = http.request('GET', URL).data
    soup = BeautifulSoup(data_received, "html.parser")
    data_json = loads(re.search(b"var data = {.*};", data_received).group(0).split(b" = ")[-1][:-1])['rss']['channel']['item']
    worldwide_sick = data_json['title']
    worldwide_death = data_json['subTitle']
    israel_sick = data_json['author']
    israel_death, israel_recoverd, israel_hard, israel_med, israel_koma, nothing = data_json['description'].replace(" ","").replace('-',',').split(",")


    page = """
    <html>
    <head>
    </head>
    <body>
    worldwide sick: {WWS}
    <br>
    worldwide death: {WWD}
    <br>
    israel sick: {ISRS}
    <br>
    israel death: {ISRD}
    <br>
    israel recoverd: {ISRR}
    <br>
    israel hard: {ISRH}
    <br>
    israel med: {ISRM}
    <br>
    israel koma: {ISRK}
    <br>
    </body>
    </html>
    """

    with open("index.html", "w") as f:
        f.write(page.format(WWS=worldwide_sick, WWD=worldwide_death, ISRS=israel_sick, ISRD=israel_death, ISRR=israel_recoverd, ISRH=israel_hard, ISRM=israel_med, ISRK=israel_koma))
    
    print ("Decorated job")
    time.sleep(10)

if __name__ == '__main__':
    while True:
        job()

  





