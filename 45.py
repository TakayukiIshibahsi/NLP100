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

    if record=="EOS\n":
        next=False
        if start :
            for i in range(int(p)+1):
                sentence+=[Chank(morph_list[i],atesaki[i],from_to[i])]
            
            result45[count]=sentence
            

    else:
        if next==False:
            next=True
            count+=1
            result+=[[]]
            result45+=[[]]
        
        if re.match(regex41,record):
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
        if re.match(regex40,record):

            value=re.findall(regex40,record)[0]
            if value[1]in katuyoukei :
                temp=Morph(value[0],value[7],value[1],value[3])
            else:
                temp=Morph(value[0],value[7],value[1],value[2])
            
            result[count]+=[temp]
            if start:
                
                morph_list[int(p)]+=[temp]


class judge:
    v:bool
    j:bool
    verb:str
    joshi:str

    def __init__(self,a,b) -> None:
        self.v=a
        self.n=b

class kaku:
    def __init__(self,arg,args) -> None:
          self.v=arg
          self.k=args

judger=[]
s=[]

for chank in result45[1]:
    j=judge(False,False)
    sentence=""
    for m in chank.morphs:
        sentence+=m.surface
        if m.pos=="動詞":
            j.v=True
            j.verb=m.base
        if m.pos=="助詞":
            j.j=True
            j.joshi=m.surface
    if judger==[]:
        judger=[j]
    else:
        judger+=[j]
    s+=sentence

kakus=[]
for key,chank in enumerate(result45[1]):
    
    words=[]
    t=False
    for index in chank.srcs:
        if judger[key].v and judger[index].j:
            pair={judger[index].joshi:s[index]}
            t=True
            if words==[]:
                words=[judger[index].joshi]
            else :
                words+=[judger[index].joshi]
    if t :
        a=[kaku(judger[key].verb,words)]
        if kakus==[]:
            kakus=a
        else:
            kakus+=a



for k in kakus:
    print(k.v+"\t",end="")
    for j in k.k:
        print(j+" ",end="")