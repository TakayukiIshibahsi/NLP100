path="neko.txt.mecab"
import re

class Mecab :
    surface:str
    base:str
    pos:str
    pos1:str

    def __init__(self,arg1,arg2,arg3,arg4) -> None:
        self.surface=arg1
        self.base=arg2
        self.pos=arg3
        self.pos1=arg4

#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
regex30="(.*?)\t(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)"
regex31="(.*?)\t動詞"

f=open(path,"r",encoding="utf-8")

file = f.readlines()

count=0

result = []

for record in file:
    
    if re.match(regex31,record):
        count+=1   
        for value in re.findall(regex30,record):
            new=Mecab(value[0],value[7],value[1],value[2])
            result.append(new)

for key,val in enumerate(result):
        print(val.surface)  