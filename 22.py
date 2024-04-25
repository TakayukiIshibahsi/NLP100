path="jawiki-country.json"
import re

regex20='.*"title".+"イギリス"'
regex21='.*\[Category'
regex22='(?<=:)(.+?)(?=(\]|\|))'

f=open(path,"r",encoding="utf-8")

file=f.readlines()

for record in file:
    if re.match(regex20,record):
        UK=record

UKrecords=UK.split("\\n")



for record in UKrecords:
    if re.match(regex21,record):
        m=re.search(regex22,record)
        print(m.group())
        
f.close()