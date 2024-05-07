path="ai.ja.cabocha"

class Morph :
    surface:str
    base:str
    pos:str
    pos1:str

    def __init__(self,arg1,arg2,arg3,arg4) -> None:
        self.surface=arg1
        self.base=arg2
        self.pos=arg3
        self.pos1=arg4




import re

regex40="(.*?)\t(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,.*"


katuyoukei=["動詞","形容詞","形容動詞","接尾辞"]

f=open(path,"r",encoding="utf-8")

file = f.readlines()

count=0
next=False

result=[[]]

for record in file:
    if record=="EOS\n":
        next=False
    else:
        if next==False:
            next=True
            count+=1
            result+=[[]]
        if re.match(regex40,record):

            value=re.findall(regex40,record)[0]
            if value[1]in katuyoukei :
                temp=Morph(value[0],value[5],value[1],value[3])
            else:
                temp=Morph(value[0],value[5],value[1],value[2])
            
            result[count]+=[temp]
        
            
            
for key,value in enumerate(result):
    if key>5:
        break
    print(str(key)+":")
    for key2,value2 in enumerate(value):
        print(str(key2)+":"+value2.base)
    print("\n")
