str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str=str.replace(".","")
str_split=str.split(" ")
e=[1,5,6,7,8,9,15,16,19]
d=dict()
for i in range(0,len(str_split)):
    t=str_split[i]
    if i+1 in e:
        str_split[i]=t[0]
    else:
        str_split[i]=t[:2]



for i in range(0,len(str_split)):
    d[str_split[i]]=i+1

print(d)