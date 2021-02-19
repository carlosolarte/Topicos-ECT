def fat(n:int) -> int:
    '''Fatorial recursivo'''
    if n == 0: return 1
    return n * fat(n-1)

# Utilizando recursão de cauda
def fatorial(n:int) -> int:
    return fatrec(n,1)

#Função que utiliza recursão de cauda
# Note que fatrec é a ultima coisa que faz a função
def fatrec(n:int, res:int) -> int:
    if n == 0 : return res
    return fatrec (n-1, res * n)

# Versão iterativa (convertendo a função anterior em um loop)
def fatiter(n:int) -> int:
    res = 1
    while True:
        if n == 0 : return res
        n,res = n-1, n * res

print (fatiter(5))
