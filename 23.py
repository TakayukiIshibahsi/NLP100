path="jawiki-country.json"
import re

regex20='.*"title".+"イギリス"'
regex23_1='==(.*?)=='



f=open(path,"r",encoding="utf-8")

file=f.readlines()

for line in file:
    if re.match(regex20,line):
        UK=line

UKlines=UK.split("\\n")

for line in UKlines:
    if re.match(regex23_1,line):
        print(line.replace("=","")+":",int(len(re.findall("=",line))/2-1))
