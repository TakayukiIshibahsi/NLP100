def n_gram_char(string: str,n: int)->list:
    return [string[i:i+n] for i in range(0,len(string)-n+1)]

s1="paraparaparadise"
s2="paragraph"

s1gram=n_gram_char(s1,2)
s2gram=n_gram_char(s2,2)

sasyu=list(set(s1gram)-set(s2gram))

print(sasyu)

wasyu=list(set(s1gram)|set(s2gram))

print(wasyu)

sekisyu=list(set(s1gram)&set(s2gram))

print(sekisyu)

print("se" in n_gram_char(s1,2))
print("se" in n_gram_char(s2,2))