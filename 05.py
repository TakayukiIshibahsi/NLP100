def n_gram_char(string: str,n: int)->list:
    return [string[i:i+n] for i in range(0,len(string)-n+1)]

def n_gram_word(string: str,n :int)->list:
    return [string.split(" ")[i:i+n] for i in range(0,len(string.split(" "))-n+1)]

s="I am an NLPer"

print("単語:",n_gram_word(s,2),"文字:",n_gram_char(s,2))
