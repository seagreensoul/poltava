# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:26:26 2018

@author: admin
"""

import pandas as pd
import geocoder 
#import folium



df= pd.read_csv('poltava.csv',
                       sep=';', encoding='cp1251')

f = open('poltava_geo1.csv', 'w')
f.write("\"lat\";\"lng\"\n")


for adr in df['adress']:
    adr = "Полтавська область "+adr
    g = geocoder.yandex(adr)
    l=g.latlng
    print(adr)
    try:
        f.write(l[0]+";"+l[1]+"\n")
    except TypeError:
        continue


f.close()
