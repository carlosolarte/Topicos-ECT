# Somatório
def somatorio(l):
    if l == []: return 0
    h,*t = l
    return h + somatorio(t)

# Produto
def produto(l):
    if l == []: return 1
    h,*t = l
    return h * produto(t)


# Reduce
from functools import reduce

def soma(x,y): return x + y

print(reduce(soma, [1,2,3],0))
print(reduce(soma, [1,2,3]))

# Utilizando lambdas

print(reduce(lambda x,y: x + y, [1,2,3]))

import operator
print(reduce(operator.add, [1,2,3]))

# Maior elemento
def maior(x,y):
    return x if x > y else y

print(reduce(maior, [1,5,2,5,7,10,4]))


# Expressões booleanas 

def ehPar(n): return n % 2 == 0

print(reduce(operator.and_, map(ehPar, [2,4,6,8])))
# print(reduce(operator.and_, map(ehPar, []))) # Erro!
print(reduce(operator.and_, map(ehPar, []),True)) 

print(all(map(ehPar, [2,4,6,7,8])))

