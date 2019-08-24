x = "paralelepipedo"
ponteiro = len(x)

def substring(s,n): # s = string a ser impressa ; n = número de caracteres da string
    for j in range(n+1):
        if s.index(s[j-1]) == 0 and s.index(s[j-1]) == None:
            print(s[:j])

        elif s.index(s[j-1]) == len(s) and s.index(s[j+1]) == None:
            print(s)

        else:
            print(s[:j])
for j in x:
    substring(x,len(x))
    x = x[(x.index(j)+1):]










