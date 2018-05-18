import pandas as pd
import folium
import folium.plugins
import re

df= pd.read_csv('poltava.csv',sep=';', encoding='cp1251')
df1=pd.read_csv('poltava_geo.csv', sep=";")
map1 = folium.Map([df1.iloc[0][0],df1.iloc[0][1]],zoom_start=9)
dark=folium.FeatureGroup(name="darkness")
fg=[folium.FeatureGroup(name=str(i+1)+" марта", overlay = False) for i in range(30)]
folium.TileLayer('openstreetmap', overlay = True).add_to(map1)
sh=df1.shape[0]
s = pd.Series(range(len(df1)), index=pd.MultiIndex.from_arrays(df1.values.T))
s = s.sort_index()

i=0
while i<sh:
    strok = '<table border=1>'
    idx = s[df1.iloc[i][0],df1.iloc[i][1]]
    s1 = re.match(r'[\d]*', str(df.iloc[i][0]))
    
    for j in idx.values:
        s2=re.match(r'[\d]*', str(df.iloc[j][0]))
        #print(s1[0], s2[0])
        if s1[0]==s2[0]:
            strok += '<tr><td>'+str(df.iloc[j][0])+'</td><td>'+str(df.iloc[j][1])+'</td><td>'+str(df.iloc[j][2])+'</td></tr>'
            print(str(df.iloc[j][2]))
    f=fg[int(s1[0])-1]
    strok+='</table>'
    f.add_child(folium.Marker(location = [df1.iloc[i][0],df1.iloc[i][1]], popup = folium.Popup(strok ,max_width='auto'), icon = folium.Icon(color = 'orange') ))
    i+=1

for i in range(30):
    map1.add_child(fg[i])

map1.add_child(folium.LayerControl())
map1.save(outfile="poltava.html")
