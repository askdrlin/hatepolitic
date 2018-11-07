
# coding: utf-8

# In[2]:


#抓第二層li中的六個url

import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time, re
url = ('https://news.tvbs.com.tw/politics/')
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'html.parser')

first = sp.find_all("div", {"class":"real_time_box"})[0]
two = first.find("ul")
three = two.find_all('li')[0]#變量 0~拉到底
four = three.find_all("div", {"class":"content_center_contxt_real_news"})[0]
for i in range(0,6):
    five = four.select('a')[i]['href']
    news_url = "https://news.tvbs.com.tw"+str(five)
    print(news_url)
    title = four.select("h2")[i].text
    print(title)


# In[2]:


import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time, re


def store(data):
    with open('tvbs.json','a',encoding='utf8') as f:
        f.write(data.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://news.tvbs.com.tw/politics/")
count = 0
for i in range(1,100):#拉一百次
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
sp = BeautifulSoup(driver.page_source)
for j in range(0,700):#我不知道底多少,設一個較大的數字
    try:
        first = sp.find_all("div", {"class":"real_time_box"})[0]
        two = first.find("ul")
        three = two.find_all('li')[j]#變量 0~拉到底
        four = three.find_all("div", {"class":"content_center_contxt_real_news"})[0]
    except:
        continue
    for i in range(0,6):
        try:
            five = four.select('a')[i]['href']#變量 一個li中有6個a href
            news_url = "https://news.tvbs.com.tw"+str(five)
            print(news_url)
            title = four.select("h2")[i].text
            print(title)
            html1 = requests.get(news_url)
            html1.encoding="utf-8"
            sp1 = BeautifulSoup(html1.text, 'html.parser')
            inside = sp1.find("div", {"class":"h7 margin_b20"}).text
            print(inside)
            count += 1
            print('第幾',count)
            
            d = {"內文": inside, "標題": title}
            json_data = json.dumps(d, ensure_ascii=False, indent=4, sort_keys=True)
            store(json_data)
        except:
            continue

print("下載玩了!")

