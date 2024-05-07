import urllib
import urllib.request
import MeCab


reg="\\n"

url="https://nlp100.github.io/data/neko.txt"

cat_text=urllib.request.urlopen(url).read().decode().replace('\u2014',"-")


file="neko.txt"

f=open(file,"w",encoding="utf-8")

f.write(cat_text)

f.close()
