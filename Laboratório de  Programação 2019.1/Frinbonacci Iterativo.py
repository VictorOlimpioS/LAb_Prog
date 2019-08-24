def fribonacci_iterativo(n):
    a = b = 1 # começando da segunda iteração
    for i in range(3,n+1):
        a,b = b,a+b
    return b
print(fribonacci_iterativo(6))