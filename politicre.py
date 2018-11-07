#!/usr/bin/env python
# coding: utf-8

# In[29]:


#此為抓正常新聞 非回文

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
import sys

#author為作者id, title為標題, date為日期, main_content為內文
#push_tag為推文標籤, push_userid為推文id, push_content為推文內容, push_time為推文時間
#num 為推噓文總數, g為推文總數, b為噓文總數, n為箭頭總數


#先過18禁

payload = {
       'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)

def store(data):
    with open('mainptt1.json','a',encoding='utf8') as f:
        f.write(data.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

for i in range(1,50):#目標頁數
    print("現在在抓第",i,"頁")
    room =[]
    t = i + 1    #批次進行迴圈,一次1頁,避免太多url加入room卡死
    for m in range(i,t):#每頁迴圈解析 若標題含有關鍵字者加入該超連結URL至ROOM
        url  ="https://www.ptt.cc/bbs/HatePolitics/index"+ str(m)+ ".html"
        res = rs.get(url, headers=headers)
        sp = BeautifulSoup(res.text, 'html.parser')
        news = sp.find_all("div", {"class":"r-ent"})
        for g in news:
            try:
                blog = g.find("a")["href"]
                if "新聞" in  g.select('.title')[0].text and "R" not in g.select('.title')[0].text :
                    room.append(blog)
                    print(g.select('.title')[0].text)
            except:
                break
                
    #到此,做出了一個塞滿擁有許多過了篩選條件url的room
        
    for u in room: #開始一頁一頁去抓
        url1 = "https://www.ptt.cc"+ str(u)+""
        html = requests.get(url1)
        html.encoding="utf-8"
        sp = BeautifulSoup(html.text, 'html.parser')
        
        main_content = sp.find(id="main-content")
        metas = main_content.select('div.article-metaline')
        try:
            author = metas[0].select('span.article-meta-value')[0].string  #抓出作者ID
            title = metas[1].select('span.article-meta-value')[0].string   #抓出標題
            date = metas[2].select('span.article-meta-value')[0].string    #抓出日期

            content = sp.find(id="main-content").text
            target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
            content = content.split(target_content)
            content = content[0].split(date)
            main_content = content[1].replace('\n', '  ')
            # print 'content:',main_content
        except:
            break
        num, g, b, n, message = 0, 0, 0, 0, {}
        for tag in sp.select('div.push'):
            try:
                # push_tag  推文標籤  推  噓  註解(→)
                push_tag = tag.find("span", {'class': 'push-tag'}).text
                #print(push_tag)

                # push_userid 推文使用者id
                push_userid = tag.find("span", {'class': 'push-userid'}).text
                #print(push_userid)

                # push_content 推文內容
                push_content = tag.find("span", {'class': 'push-content'}).text
                push_content = push_content[1:]
                #print(push_content)

                # push-time 推文時間
                push_time = tag.find("span", {'class': 'push-ipdatetime'}).text
                push_time = push_time.rstrip()
                #print(push_ipdatetime)

                num += 1
                message[num] = {"狀態": push_tag,
                                "內容": push_content}

                # 計算推噓文數量 g = 推 , b = 噓 , n = 註解
                if push_tag == u'推 ':
                    g += 1
                elif push_tag == u'噓 ':
                    b += 1
                else:
                    n += 1
            except :
                continue
        
    #存成json
    try:
        d = {"作者": author, "標題": title, "日期": date,
             "內文": main_content, "推文": message, "推噓文總數:":num}
        json_data = json.dumps(d, ensure_ascii=False, indent=4, sort_keys=True)
        store(json_data)
    except:
        continue


# In[28]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
import sys

#author為作者id, title為標題, date為日期, main_content為內文
#push_tag為推文標籤, push_userid為推文id, push_content為推文內容, push_time為推文時間
#num 為推噓文總數, g為推文總數, b為噓文總數, n為箭頭總數


#先過18禁

payload = {
       'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)

url = "https://www.ptt.cc/bbs/HatePolitics/M.1541579733.A.BCE.html"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'html.parser')
main_content = sp.find(id="main-content")
metas = main_content.select('div.article-metaline')
author = metas[0].select('span.article-meta-value')[0].string  #抓出作者ID
title = metas[1].select('span.article-meta-value')[0].string   #抓出標題
date = metas[2].select('span.article-meta-value')[0].string    #抓出日期
one = sp.find(id="main-content")

content = sp.find(id="main-content").text
target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
content = content.split(target_content)
content = content[0].split(date)
main_content = content[1].replace('\n', '  ')
# print 'content:',main_content

print(author)
print(title)
print(date)
print(main_content)


# In[ ]:




