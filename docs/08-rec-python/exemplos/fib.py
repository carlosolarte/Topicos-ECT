def fibrec(n:int) -> int:
    '''Retorna o elemento n da sequência Fibonacci'''
    if n == 1 or n == 2 : return 1
    return fibrec(n-1) + fibrec(n-2)

# Utilizando recursão de cauda
def fibtail(n:int) -> int:
    return fibtailrec(n,1,1) 
# Função auxiliar que implementa recursão de cauda 
def fibtailrec(n:int, pult:int, ult:int) -> int:
    if n == 1 or n == 2 : return ult
    return fibtailrec(n-1,ult, pult + ult)

# Utilizando um loop para evitar o problema da pilha de execução 
def fibloop(n:int) -> int:
    pult, ult = 1,1
    while True:
        if n == 1 or n == 2 : return ult
        n,pult,ult = n-1, ult, pult + ult

print(fibloop(1000))

