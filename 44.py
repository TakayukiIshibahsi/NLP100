path="ai.ja.cabocha"
from graphviz import Digraph

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



regex40="(.*?)\t(.*?)\,(.*?)\,(.*?)\,(.*?)\,(.*?)\,.*"
regex41="\* (\d+?) (-\d+|\d+)D.*"

katuyoukei=["動詞","形容詞","形容動詞","接尾辞"]

f=open(path,"r",encoding="utf-8")

file = f.readlines()

count=0
next=False
start=False
result=[[]]
result41=[[Chank]]

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
            
            result41[count]=sentence
            from_to=[[]]*200
            morph_list=[[]]
            sentence=[]
            atesaki=[]
            start=False
            

    else:
        if next==False:
            next=True
            count+=1
            result+=[[]]
            result41+=[[]]
        
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
                temp=Morph(value[0],value[5],value[1],value[3])
            else:
                temp=Morph(value[0],value[5],value[1],value[2])
            
            result[count]+=[temp]
            if start:
                
                morph_list[int(p)]+=[temp]


regex42=",|、|\n|）|（|『|』|「|」"
s=[]
class judge:
    v:bool
    n:bool

graph = Digraph(format="png")



for k,chank in enumerate(result41[2]):
    sentence=""
    graph.node("node"+str(k))
    for m in chank.morphs:
        sentence+=m.surface
    for val in chank.srcs:
        graph.edge("node"+str(val),"node"+str(k))
    
    s+=[str(re.sub(regex42,"",sentence))]


graph.render("image/output")

# 画像を表示
graph.view()

