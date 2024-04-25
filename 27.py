
path="jawiki-country.json"
import re

regex20='.*"title".+"イギリス"'
regex25='\{\{基礎情報.*\\\\n\}\}\\\\n'
regex25_2='\\\\n\|(.*?) ?=(.*?)(?=\\\\n)'
regex26="''+"
regex27_1="(\[\[|\]\])"

f=open(path,"r",encoding="utf-8")

file=f.readlines()

for line in file:
    if re.match(regex20,line):
        UK=line

base=re.search(regex25,UK).group()

part=re.findall(regex25_2,base)

answer=dict()


for k,v in part:     
   v=re.sub(regex26,"",v)
   v=re.sub(regex27_1,"",v)
   answer[k]=v
   print(k+":"+answer[k])
   

