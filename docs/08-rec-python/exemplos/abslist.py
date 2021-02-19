
def absgen(c):
    ''' Gerar a sequência abs(x1), abs(x2),... a partir da sequência x1,x2,...'''
    try:
        v = next(c) # Próximo elemento 
        yield abs(v) # Gerar um valor
        yield from absgen(c) # Continuar gerando 
    except StopIteration: # Fim da sequência 
        return

# Sem utilizar "yield from" para evitar estourar a pilha de execução 
def absgenloop(c):
    try:
        while True:
            v = next(c) # Próximo elemento 
            yield abs(v) # Gerar um valor

    except StopIteration: # Fim da sequência 
        return
# Uma forma mais simples utilizando for
def absfor(c):
    for x in c: # por cada x na sequência c
        yield abs(x)

# Ainda mais simples, retornando uma expressão geradora
def absexpgen(c):
    return (abs(x) for x in c)

it = iter([-4,-2,1,4,-6])
it2 = iter(range(0,-1000,-1))
it3 = iter(range(0,-1000,-1))
it4 = iter(range(0,-1000,-1))
print(list(absgen(it)))
print(list(absgenloop(it2)))
print(list(absfor(it3)))
print(list(absfor(it4)))


print( [ abs(x) for x in range(0,-1000,-1) ] )
