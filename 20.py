path="jawiki-country.json"
import re

regex='.*"title".+"イギリス"'

f=open(path,"r",encoding="utf-8")

file=f.readlines()

for record in file:
    if re.match(regex,record):
        UK=record

print(UK)

f.close()