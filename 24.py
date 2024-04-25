path="jawiki-country.json"
import re

regex20='.*"title".+"イギリス"'
regex24='.*\[\[ファイル:'
regex24_1='(?<=:)[^|\/]+\.[a-zA-Z]+'



f=open(path,"r",encoding="utf-8")

file=f.readlines()

for line in file:
    if re.match(regex20,line):
        UK=line

UKlines=UK.split("\\n")

for line in UKlines:
    if re.match(regex24,line):
        for match in re.findall(regex24_1,line):
            print(match)
        