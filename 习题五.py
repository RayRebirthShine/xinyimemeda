# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:03:23 2018
1.使用到函数 使用到list的一些功能
2.优化代码，用函数的方式修改练习4。输出每一天的天气（函数）
3.打印温度折线图，使用函数来优化（必须要有返回值）
@author: asus
"""
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
'''
def day(y,z):
    print('day'+str(z)+'`s weather:')
    print('temp:'+str(data['list'][y]['main']))
    print('temp_min:'+str(data['list'][y]['main']['temp_min']))
    print('temp_max:'+str(data['list'][y]['main']['temp_max']))
    print('pressure:'+str(data['list'][y]['main']['pressure']))
    print('description:'+str(data['list'][y]['weather'][0]['description']))
day(2,'1')
day(10,'2')
day(18,'3')
day(26,'4')
day(34,'5')
   
'''   
''' 
def ray(x):
    return'-'*int(data['list'][x]['main']['temp'])

print('day1:'+ray(2))
print('day2:'+ray(10))
print('day3:'+ray(18))
print('day4:'+ray(26))
print('day5:'+ray(24))
'''

def lxy(a):
    return data['list'][a]['main']['temp']
a1=lxy(2)
a2=lxy(10)
a3=lxy(18)
a4=lxy(26)
a5=lxy(34)
b=[a1,a2,a3,a4,a5]
print('排序为：')
print(sorted(b))


