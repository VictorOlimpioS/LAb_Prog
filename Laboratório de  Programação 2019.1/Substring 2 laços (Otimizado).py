def substring(s,n):
    for i in range(n+1):
        print(s[:i])

x= "ana"
for j in x:
    substring(x,len(x))
    x = x[(x.index(j)+1):]