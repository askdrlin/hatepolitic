
# coding: utf-8

# In[24]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
response = urlopen("https://cn.nytimes.com/")
html = BeautifulSoup(response)
html


# In[26]:


# html.find_all("li", class_ = "list-rst")
news = html.find_all("li", {"class":" first "})
for r in news:
    man = r.find("a", class_="en_byline")
    print(man)


# In[1]:


import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)


for m in range(1000,1100):
    url  ="https://www.ptt.cc/bbs/beauty/index"+ str(m)+ ".html"
    res = rs.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_links=sp.find_all(['a','img']) 

    for link in all_links:
        # 讀取 src 和　href 屬性內容
        src=link.get('src')
        href = link.get('href')
        attrs=[src,href]
        for attr in attrs:
            # 讀取　.jpg 和　.png 檔
            if attr != None and ('.jpg' in attr or '.png' in attr):
                # 設定圖檔完整路徑
                full_path = attr            
                filename = full_path.split('/')[-1]  # 取得圖檔名
                print(full_path)
                # 儲存圖片
                try:
                    image = urlopen(full_path)
                    f = open(os.path.join(images_dir,filename),'wb')
                    f.write(image.read())
                    f.close()
                except:
                    print("{} 無法讀取!".format(filename))


# 抓取多頁標題

# In[2]:


import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

for m in range(2500,2501):
    url  ="https://www.ptt.cc/bbs/beauty/index"+ str(m)+ ".html"
    res = rs.get(url, headers=headers)
    sp = BeautifulSoup(res.text, 'html.parser')
    all_links=sp.find_all(['a','img'])
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.select('.r-ent')
    for item in items:
        if "正妹" in item.select('.title')[0].text:
            print(item.select('.title')[0].text)
git remote add origin https://github.com/askdrlin/hatepolotic.git


# 爬所有照片

# In[ ]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json

payload = {
       'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)


n = 0
for i in range(2550,2697):#目標頁數
    print("現在在抓第",i,"頁")
    room =[]
    t = i + 1    #批次進行迴圈,一次1頁,避免太多url加入room卡死
    for m in range(i,t):#每頁表特版迴圈解析 若標題含有關鍵字者加入該超連結URL至ROOM
        url  ="https://www.ptt.cc/bbs/beauty/index"+ str(m)+ ".html"#
        res = rs.get(url, headers=headers)
        sp = BeautifulSoup(res.text, 'html.parser')

        girls = sp.find_all("div", {"class":"r-ent"})
        for g in girls:
            blog = g.find("a")["href"]
            if "正妹" in g.select('.title')[0].text:
                room.append(blog)
        print("一頁讀取完了,開始下載!")
    for u in room:#room陣列中挨個url抓取裡面的圖片
        url1 = "https://www.ptt.cc"+ str(u)+""
        print(url1)
        html = requests.get(url1)
        html.encoding="utf-8"

        sp = BeautifulSoup(html.text, 'html.parser')

        # 建立 images 目錄儲存圖片
        images_dir="images/"
        if not os.path.exists(images_dir):
            os.mkdir(images_dir)

        # 取得所有 <a> 和 <img> 標籤
        all_links=sp.find_all(['a','img']) 
        for link in all_links:
            # 讀取 src 和　href 屬性內容
            src=link.get('src')
            href = link.get('href')
            attrs=[src,href]
            for attr in attrs:
                # 讀取　.jpg 和　.png 檔
                if attr != None and ('.jpg' in attr or '.png' in attr):
                    # 設定圖檔完整路徑
                    full_path = attr            
                    filename = full_path.split('/')[-1]  # 取得圖檔名
                    print(full_path,filename,"下載成功")
                    # 儲存圖片
                    try:
                        image = urlopen(full_path)
                        f = open(os.path.join(images_dir,filename),'wb')
                        f.write(image.read())
                        n += 1
                        print("這是第",n,"張照片")
                        f.close()
                    except:
                        print("{} 無法讀取!".format(filename))
                else:
                    pass

print("下載完畢!")


# #抓取單頁之 url

# In[ ]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
url  ="https://www.ptt.cc/bbs/beauty/index.html"
res = rs.get(url, headers=headers)
sp = BeautifulSoup(res.text, 'html.parser')

girls = sp.find_all("div", {"class":"r-ent"})

for g in girls:
    blog = g.find("a")["href"]
    if "正妹" in g.select('.title')[0].text:
            print(g.select('.title')[0].text,blog)


# 抓取多頁之url

# In[ ]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json

payload = {
       'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
for m in range(2490,2500):
    url  ="https://www.ptt.cc/bbs/beauty/index"+ str(m)+ ".html"
    res = rs.get(url, headers=headers)
    sp = BeautifulSoup(res.text, 'html.parser')

    girls = sp.find_all("div", {"class":"r-ent"})
    for g in girls:
        blog = g.find("a")["href"]
        if "正妹" in g.select('.title')[0].text:
                print(g.select('.title')[0].text,blog)


# 製作url陣列

# In[10]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json

payload = {
       'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)

room =[]
for m in range(2500,2510):
    url  ="https://www.ptt.cc/bbs/beauty/index"+ str(m)+ ".html"
    res = rs.get(url, headers=headers)
    sp = BeautifulSoup(res.text, 'html.parser')

    girls = sp.find_all("div", {"class":"r-ent"})
    for g in girls:
        blog = g.find("a")["href"]
        if "正妹" in g.select('.title')[0].text:
                print(g.select('.title')[0].text,blog)
                room.append(blog)
print(room)

