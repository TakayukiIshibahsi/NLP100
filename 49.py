path="45.txt.cabocha"

f = open(path,"r",encoding="utf-8") 
file =f.readlines()

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

class Chank:
    dst:int
    def __init__(self,arg1,arg2,arg3) -> None:
        self.morphs=arg1
        self.dst=arg2
        self.srcs=arg3

import re



regex40="(.*?)\t(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,.*"
regex41="\* (\d+?) (-\d+|\d+)D.*"

katuyoukei=["動詞","形容詞","形容動詞","接尾辞"]

f=open(path,"r",encoding="utf-8")

file = f.readlines()

count=0
next=False
start=False
result=[[]]
result45=[[Chank]]

from_to=[[]]*200
morph_list=[[]]
sentence=[]
atesaki=[]


for key,record in enumerate(file):

    if record=="EOS\n": #EOSごとに取得した文の更新作業
        next=False
        if start :
            for i in range(int(p)+1):
                sentence+=[Chank(morph_list[i],atesaki[i],from_to[i])]
            
            result45[count]=sentence
            
    else:
        if next==False: #一つ前がEOSだった時の開始動作
            next=True
            count+=1
            result+=[[]]
            result45+=[[]]
        
        if re.match(regex41,record):  #文節開始にヒット
            value=re.findall(regex41,record)[0]
            p=value[0]
            to=value[1]
            atesaki+=[int(to)]
            if int(to)!=-1:
                if from_to[int(to)]==[]:
                   from_to[int(to)]=[int(p)]
                else:
                   from_to[int(to)]+=[int(p)]   
            start=True
            morph_list+=[[]]
        if re.match(regex40,record):    #単語にヒット

            value=re.findall(regex40,record)[0]
            if value[1]in katuyoukei :
                temp=Morph(value[0],value[7],value[1],value[3])
            else:
                temp=Morph(value[0],value[7],value[1],value[2])
            
            result[count]+=[temp]
            if start:
                
                morph_list[int(p)]+=[temp]

s=[]

class bunsetu:
    noun:str
    els:str
    def __init__(self,a,b) -> None:
        self.noun=a
        self.els=b

for chank in result45[1]:
    temp_bunsetu=bunsetu("","")
    for m in chank.morphs:
        if m.pos=="名詞":
            temp_bunsetu.noun+=m.surface
        else:
            temp_bunsetu.els+=m.surface  
    s+=[temp_bunsetu]

def f_48(s,a,index,n):
    print(s[index],end="")
    if a[index]>0:
        print(" -> ",end="")
        f_48(s,a,a[index])
    else:
        print("")


