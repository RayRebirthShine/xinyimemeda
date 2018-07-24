# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:22:06 2018
习题7：
1.使用多选其一，完成天气的提醒，淘宝客户端
2.一定要使用多次for循环。偶尔使用while
3.使用到break或者continue。
@author: asus
"""'''
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def lxy(r,t):
    print('day'+str(r))
    print('temp:'+str(data['list'][t]['main']['temp']))
    print('weather:'+str(data['list'][t]['weather'][0]['description']))
    r=str(data['list'][t]['weather'][0]['main'])
    if r=='Clear':
        print('have a good day buddy!')
    elif r=='Clouds':
        print('not sunny but happy!')
    elif r=='Rain':
        print('dont forget your umbrella!')
lxy(1,2)
lxy(1,10)
lxy(1,18)
lxy(1,26)
lxy(1,34)
'''

import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)

def lxy(r):
    for r in range(0,36):
        print('production No.'+str(r+1))
        print('title:'+str(data['mods']['itemlist']['data']['auctions'][r]['title']))
        print('price:'+str(data['mods']['itemlist']['data']['auctions'][r]['view_price'])+'RMB')
        print('nick:'+str(data['mods']['itemlist']['data']['auctions'][r]['nick']))
        print('location:'+str(data['mods']['itemlist']['data']['auctions'][r]['item_loc']))
        print('sales:'+str(data['mods']['itemlist']['data']['auctions'][r]['view_sales']))
        while r==17:
            continue
        if r==35:
            break
lxy(r)
