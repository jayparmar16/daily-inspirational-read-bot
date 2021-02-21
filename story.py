import re
import pandas as pd
import requests
import telegram
import bs4

### EXTRACTING LINK FROM CSV AND MARKING IT DONE 
def getLink():
    df = pd.read_csv("links.csv")
    for index,row in df.iterrows():
        if row['Done'] == 1:
            continue
        else:
            #print(index,row['Links'],row['Done'])
            df.loc[index,"Done"] = 1
            df.to_csv("links.csv", index=False)
            return row['Links']
            break
a = getLink()

### MINE THE STORY FROM EXTRACTED LINK
bookres = requests.get(a)
bookres.raise_for_status()
linksSoup = bs4.BeautifulSoup(bookres.text,'html.parser')
L = []
def getStory(): 
    p = linksSoup.findAll('article')
    for r in p:
        L.append(r.get_text())
getStory()

### CLEANING THE STORY
def cleanStory(L):
    f = re.sub(r'\\n+|\\| Read 300+ stories on DailyTenMinutes.com'," ",L[0]) #removing all \n
    f1 = " ".join(f.split())
    flag = True
    while flag == True:    # removing the intro part
        for i in range(len(f1)//2):
            if f1[i] == "." and f1[i-1] == "." and f1[i-2] == ".": #Pattern
                p = f1[i+1:len(f1)]
                flag = False
    return p
a = cleanStory(L)
#print(type(a))

my_token = '1609959829:AAGB6Uvtbhv82EOM2ceevKcl5befJSWeIQI'

def send(msg, chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)
send(a,1211116531,my_token)