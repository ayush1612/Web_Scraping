
# coding: utf-8

# In[88]:


import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("https://www.nasdaq.com/markets/indices/major-indices.aspx")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all1=soup.find_all("table",{"class":"USMN_MarketIndices"})[0]


td=all1.find_all("td")
l=[]
#symbols
for i in range(0,len(td),6):
    d={}
#Change net%

    try:
        d["Change net%"]=td[i+3].text
    except:
        pass

#High

    try:
        d["High"]=td[i+4].text
    except:
        pass

#Low

    try:
        d["Low"]=td[i+5].text
    except:
        pass
#index value

    try:
        d["Index"]=td[i+2].text
    except:
        pass
#NAMES

    try:
        d["Name"]=td[i+1].text
    except:
        pass

#Symbol    
    try:
            d["Symbol"]=td[i].find("h3").text
    except:
            pass

    
    l.append(d)




df=pandas.DataFrame(l)
df.to_csv("Output.csv")

