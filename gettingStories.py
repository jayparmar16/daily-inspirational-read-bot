### IMPORTING LIBRARIES
import bs4
import pandas as pd
import requests
import re
import string

### GETTING LINK AND CREATING BS4 OBJECT
res = requests.get("http://www.dailytenminutes.com/p/short-stories.html")
res.raise_for_status() # checking if request was successful
readsSoup = bs4.BeautifulSoup(res.text,'html.parser')

### GETTING ALL LINKS
links = []
for a in readsSoup.find_all('a',href=True): #Finding all links from bs4 object
    if a.text:
        links.append(a['href'])
l = len(links)
#print(l)

### USING REGEX TO FIND LINKS FOR STORIES
def cleaningLinks(L):
    rlinks = []
    for i in links:
        linkreg = re.search('[a-zA-Z.]+/\d+/\d+',i)
        if linkreg!=None:
            rlinks.append(i)
    return rlinks

a = cleaningLinks(links)

### STORING LINKS TO CSV WITH 'DONE' COLUMN WITH DEFAULT VALUE 0
def csvLinks(links):
    df = pd.DataFrame(links,columns=["Links"])
    df["Done"] = 0
    df.to_csv("links.csv",index = False)
csvLinks(a)
