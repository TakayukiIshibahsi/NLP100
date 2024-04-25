
path="jawiki-country.json"
import re

regex20='.*"title".+"イギリス"'
regex25='\{\{基礎情報.*\\\\n\}\}\\\\n'
regex25_2='\\\\n\|(.*?) ?=(.*?)(?=\\\\n)'
regex26="''+"
regex27_1="(\[\[|\]\])"
regex28_1="<ref( |>).*"
regex28_2="<br.*"
regex28_3="\{\{.*\|(?=[^|]+)"
regex28_4="\{\{(.*?)\}\}"
regex28_5="\}\}"
regex28_6="\|.*\|.*"
regex28_7=":en:"


f=open(path,"r",encoding="utf-8")

file=f.readlines()

for line in file:
    if re.match(regex20,line):
        UK=line

base=re.search(regex25,UK).group()

part=re.findall(regex25_2,base)

answer=dict()

regex=[regex26,regex27_1,regex28_1,regex28_2,\
       regex28_3,regex28_4,regex28_5,regex28_6,regex28_7]

for k,v in part:
   for reg in regex:
       v=re.sub(reg,"",v)     
   
   answer[k]=v
   print(k+":"+answer[k])
   

