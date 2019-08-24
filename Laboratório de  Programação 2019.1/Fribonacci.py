
def fribonacci_recursivo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fribonacci_recursivo(n-1) + fribonacci_recursivo(n-2)

print(fribonacci_recursivo(5))