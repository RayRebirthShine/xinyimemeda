# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:08:46 2018
1.显示4个商品然后打印分割线，只要第一页36个商品信息
2.列出36个商品
3.获取所有的商品价格并排序，从高到低
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示。
@author: asus
"""
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
'''
def pro(a):
        print('第'+str(a+1)+'个')
        print('名称:'+str(data['mods']['itemlist']['data']['auctions'][a]['title']))
        print('价格:'+str(data['mods']['itemlist']['data']['auctions'][a]['view_price']))
        print('店铺:'+str(data['mods']['itemlist']['data']['auctions'][a]['nick']))
        print('产地:'+str(data['mods']['itemlist']['data']['auctions'][a]['item_loc']))
        print('销量:'+str(data['mods']['itemlist']['data']['auctions'][a]['view_sales']))
        print(' ')
        if((a+1)%4==1):
            print('*'*20)
            
def pros(b):
    pro(b)
    pro(b+1)
    pro(b+2)
    pro(b+3)
    pro(b+4)
    pro(b+5)
pros(0)    
pros(6) 
pros(12) 
pros(18) 
pros(24) 
pros(30) 
    '''    
            

            
'''
ls=[]            
def pri(a):     
    for a in range(0,36):
        p=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        ls.append(p)
    return ls
pri(a)
b=sorted(ls)
print('排序为：')
b=list(reversed(b))
print(b)
'''
'''
li=[]            
def qua():     
    for x in range(0,36):
        q=int(data['mods']['itemlist']['data']['auctions'][x]['view_sales'][:-3])
        li.append(q)
    return li
qua()
r=sorted(li)
print('排序为：')
r=list(reversed(r))
print(r)
'''
def fee():
    for i in range(0,36):
        x=i
        if float(data['mods']['itemlist']['data']['auctions'][x]['view_fee'])==0.00:
            print ('第{}个商品包邮'.format(x+1))
fee()            
            
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           

