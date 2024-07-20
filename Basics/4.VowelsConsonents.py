

def vowCon(s):
    vow,con=0,0
    for i in range(len(s)):
        if s[i] in "aeiou":
            vow+=1
        else:
            con+=1
    return vow,con



s="Todayalh"
vowels,consonents=vowCon(s)
print(f'No of vowels= {vowels}')
print(f'No of consonents= {consonents}')