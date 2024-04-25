path="jawiki-country.json"
import re
import urllib
import urllib.parse
import urllib.request
import json

regex20='.*"title".+"イギリス"'
regex25='\{\{基礎情報.*\\\\n\}\}\\\\n'
regex25_2='\\\\n\|(.*?) ?= ?(.*?)(?=\\\\n)'


f=open(path,"r",encoding="utf-8")

file=f.readlines()

for line in file:
    if re.match(regex20,line):
        UK=line

base=re.search(regex25,UK).group()

part=re.findall(regex25_2,base)

answer=dict()

for k,v in part:     
   answer[k]=v
 


url="https://www.mediawiki.org/w/api.php?action=query&titles=File:"+\
    urllib.parse.quote(answer["国旗画像"])+"&format=json&prop=imageinfo&iiprop=url"
connection = urllib.request.urlopen(url)
print(connection)
print(json.loads(connection.read().decode())["query"]["pages"]["-1"]["imageinfo"][0]["url"])


