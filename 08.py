def cipher(s:str):
    s2=""
    for i in range(0,len(s)):
        
        if s[i].islower:
            s2.join(chr(219-ord(s[i])))
        else:
            s2.join(s[i])
    return s2

print(cipher("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
