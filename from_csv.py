import pandas as pd
import geocoder 

df= pd.read_csv('poltava.csv',sep=';', encoding='cp1251')
f = open('poltava_geo.csv', 'w')
f.write("\"lat\";\"lng\"\n")

for adr in df['adress']:
    adr = "Полтавська область "+adr
    g = geocoder.yandex(adr)
    l=g.latlng
    print(adr)
    try:
        f.write(l[0]+";"+l[1]+"\n")
    except TypeError:
        f.write('a'+";"+'a')
        continue
f.close()
