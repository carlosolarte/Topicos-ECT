
# As listas podem ser iteradas
l = [1,2,3]
for x in l: # Por cada elemento x na lista l
    print(x)

# As tuplas também 
t = (1,2,3)
for x in t:
    print(x)

#########################
# Escreva em um arquivo texto test.txt 3 linhas, por exemplo, 
#um
#dois
#três

# Ler manualmente cada uma das linhas do arquivo
f = open("test.txt")
while True:
    try:
        l = next(f)
        print(l)
    except StopIteration:
        break # Fim da iteração

# Uma forma mais simples! Utilizando um laço for

f = open("test.txt")
for l in f:
    print(l)


###############
#Listas e Sets como iteradores

l = [1,2,3,4]
iterl = iter(l)
print(next(iterl))
print(next(iterl))
print(next(iterl))
print(next(iterl))


s = {"a","b","c"}
iters = iter(s)
print(next(iters))
print(next(iters))
print(next(iters))

#####
# Range como um iterador

r = range(5)
iterr = iter(r)
print(next(iterr))
print(next(iterr))

# Construir uma lista a partir de um range
l = list(range(1,7,2))
print(l)

#############
# Enumeration

l = ["a","b","c","d"]
for (i, x) in enumerate(l):
    print(f'i={i}, x={x}')

e = enumerate(l)
print(next(e))
print(next(e))


#====================
# Compreensão de listas


l = [1,2,3]
for i in range(len(l)):
    l[i] = l[i]+1

print(l)
# Existe uma forma muito melhor de fazer isso!

l = [1,2,3]
il1 = (x+1 for x in l)
print(next(il1))
print(next(il1))
print(next(il1))

# Criando uma lista a partir de um iterador
l1 = list(range(10))
l2 = [x for x in l1]
l3 = list(x+1 for x in range(10))
print(l1)
print(l2)
print(l3)

###############
# Computação Preguiçosa
from time import sleep
def incdevagar(n):
    '''retorna n+1 depois de 2 segundos'''
    sleep(2)
    print("terminei!")
    return n+1

# A atribuição é instantânea (a função incdevagar não voi ainda chamada)
it1 = (incdevagar(x) for x in [1,2,3])
print(next(it1)) # Só 2 segundos (para calcular o primeiro elemento)

# Se materializamos o iterador, incdevagar deve ser executada para cada elemento
it1 = (incdevagar(x) for x in [1,2,3])
l = list(it1)

# De forma alternativa
l = [incdevagar(x) for x in [1,2,3] ]
print(l)


# Compreensão de listas 

def ehPrimo(n:int) -> bool:
    ''' Determina se n (>=0)  é primo '''
    assert(n>=0)
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i+= 2
    return True


l = [x for x in range(100) if ehPrimo(x)]
print(f'primos: {l}')

# Geradores
l = [1,2,3]
# l2 é uma lista
l2 = list( x+1 for x in l)
print(l2) # [2, 3, 4]
# De forma alternativa
l3 = [ x+1 for x in l]
print(l3) # [2, 3, 4]
# Mas também podemos gerar conjuntos
s1 = { x+1 for x in l }
s2 = set( x+1 for x in l)
print(s1) # {2, 3, 4}
print(s2) # {2, 3, 4}

# Um gerador pode ser utilizando só uma vez
l = [1,2,3]
g = (x+1 for x in l)
l1 = list(g)
l2 = list(g) # g já foi consumido!
print(l1) # [2, 3, 4]
print(l2) # [] 

################

def nFib(n):
    '''retorna o elemento n da sequência fibonacci'''
    a1,a2 = 1,1
    if n <= 2: return 1
    for i in range(n -2):
        novo = a1+a2
        a1,a2 = a2, novo
    return novo

#Utilizando uma função geradora

def fibseq(n):
    '''Gera os n primeiros elementos da sequência'''
    a1,a2 = 1,1
    yield a1 # Primeiro elemento
    yield a2 # segundo elemento
    for i in range(n -2):
        novo = a1+a2
        a1,a2 = a2, novo
        yield novo

l = list(fibseq(10))
print(l)


def fibseqinf():
    '''sequência "infinita"'''
    a1,a2 = 1,1
    yield a1 # Primeiro elemento
    yield a2 # segundo elemento
    while True:
        novo = a1+a2
        a1,a2 = a2, novo
        yield novo


from itertools import islice
# Como a função "take" em Haskell
l = list(islice(fibseqinf(), 10))
print(l)

# De forma alternativa 
g= fibseqinf()
for i in range(10):
    print(next(g))

#Também podemos utilizar compreensão de listas!
g= fibseqinf()
lfib = [ next(g) for x in range(10) ]
print(lfib)

def fibseqinfn(n):
    '''n primeiros elementos utilizando fibseqinf'''
    g = fibseqinf()
    for i in range(n):
        yield next(g)

l = list(fibseqinfn(10))
print(l)

# Mais uma alternativa... utilizando enumerate

def fibnenum(n):
    '''Gerar os n primeiros termos utilizando uma enumeração'''
    for (i,x) in enumerate(fibseqinf()):
        if i>=n: break
        yield x

l = list(fibnenum(10))
print(l)
