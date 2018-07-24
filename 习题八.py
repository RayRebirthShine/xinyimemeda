# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:54:52 2018

@author: asus
"""

import json
import urllib.request as r
import time
word = r.quote('裙子')
url = 'https://s.taobao.com/search?q='+word+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B8%A9%E5%B7%9E&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=0&ajax=true'
itemList = []

def reqTimeOut(url,timeOut):
    for i in range(0,100):
        urlPage = url + '&s=' + str(i*44)
        try:
            req = r.urlopen(urlPage)
            if req.getcode()==200:
                data = req.read().decode('utf-8','ignore')
        except Exception as err:
            print('网络请求错误,正在重试中。。。')
            i = i-1
            break
      #  data = json.loads(data)
        try:
            
            fileURL = open('reqDatas.txt','a+',encoding='gbk')
#            fileList = open('reqList.txt','w',encoding='utf-8')
            fileURL.write(data+'\n')
            fileURL.close()
        except Exception as err:
            print('文件写入错误！重试中。。。')
            continue
     #   itemList.append(data['mods']['itemlist']['data']['auctions'])
        print('爬去第'+str(i+1)+'页成功')
        time.sleep(timeOut)
reqTimeOut(url,0)
