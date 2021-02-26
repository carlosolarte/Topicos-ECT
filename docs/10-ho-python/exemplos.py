# Exemplos
import math
from typing import Callable,TypeVar

def inc(x:int) -> int:
    return x + 1

type(inc) # Uma função! class function
# Toda função implementa o método "call"
print(inc.__call__(3))
# Mas sempre chamamos as funções com a notação usual de parênteses 
print(inc(3))


# O que faz a função a seguir?
def misterio(f, n):
    return f(n)

print(misterio(inc, 3))
print(misterio(math.sqrt, 3))

incrementar = inc
print(incrementar(4))


#chamar: recebe:
# - uma função do tipo T -> T (para qualquer tipo T), 
# - um objeto do tipo T
# - retorna um objeto do tipo T

T = TypeVar('T')
def chamar(f: Callable[[T], T], x:T) -> T:
    return f(x)

print(chamar(inc, 5))

# Utilizando map

l = [1,2,3,4]
m = map(inc, l)
print(next(m))
print(list(map(inc,l)))


# Expressões lambda
finc = lambda x: x + 1
print(finc(3))

print(list(map(lambda x: x+1, [1,2,3,4])))

# Duração de atividades

atividades = [ (1,5), (3,7),(4,20) ]
duracao = list(map(lambda t : t[1] - t[0] , atividades))
print(duracao)

# Utilizando Compreensão de listas
dur = [ fin - ini for (ini,fin) in atividades ]
print(dur)

# Filter

pares = filter(lambda x: x%2 ==0, range(10))
print(next(pares)) # protocolo de iteração
# Materializando o iterador numa lista
print(list(filter(lambda x: x%2 ==0, range(10))))


# Utilizando compreensão de listas
numpares = [ x for x in range(10) if x % 2 ==0]
print(numpares)
