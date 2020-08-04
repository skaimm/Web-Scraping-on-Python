# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:40:58 2020

@author: uasmt
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"},limit=10)

productDict = {}
index = 0
for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    try:
        newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')
    except IndexError:
        newprice = oldprice
        oldprice = 0

    productDict[index] = {
        "name" : name,
        "link" : link,
        "oldprice" : oldprice,
        "price" : newprice
    }
    
    index +=1
    

for key,value in productDict.items():
    for k,v in productDict[key].items():
        print( k +" : "+ str(v))