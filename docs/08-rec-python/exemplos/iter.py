# Comparando Iteradores e Iteráveis

from typing import Iterable, Iterator

# Uma função geradora, quando chamada, cria um iterador
def contar(n:int) -> Iterator: #Também, Iterator[int]
    for i in range(n):
        yield i

# Como todo iterador, podemos utilizar next
it = contar(4)
print(next(it))

# Uma lista é um iterável, e podemos construir um iterador utilizando iter
l = [1,2,3]
it = iter(l)
print(next(it))

# Mas os iteráveis não possuem método next
# Erro!
#print(l.next())

# A função a seguir trabalha com iteráveis  (como parâmetro)
def maisUm(s:Iterable[int]) -> Iterator[int]:
    # Note que next não é explicitamente utilizando
    # Mas, o laço for internamente cria um iterador a partir de s (iter(s))
    # e, depois, chama o método next
    for x in s:
        yield x+1

# Note que maisUm funciona com qualquer iterável
# Como todo iterador é um iterável, a função também trabalha com iteradores

print(list(maisUm(range(4)))) # Range é  um iterável
print(list(maisUm([1,2,3]))) # Funciona com listas (que são iteráveis) 
print(list(maisUm((1,2,3)))) # Também com tuplas
print(list(maisUm(contar(4)))) # Também com iteradores

# As expressões geradoras são iteradores. Portanto, maisUm funciona
print(list(maisUm( x for x in range(10)))) # Utilizando uma expressão geradora
expgen = (x for x in range(5)) # Expressão geradora
print(list(maisUm(expgen)))

# A função a seguir utiliza explicitamente "next". Portanto, só podemos utilizar
# iteradores (e não iteráveis) como parâmetros. 

def meuzip(c1:Iterator, c2:Iterator) -> Iterator:
    while True:
        try:
            e1,e2 = next(c1), next(c2)
            yield e1, e2
        except StopIteration:
            return


#Erro! As listas não implementam o método next (não são iteradores)
#print(meuzip([1,2,3],[4,5,6]))

# Antes de chamar a função, devemos gerar um iterador a partir do iterável
print(meuzip(iter([1,2,3]),iter([4,5,6])))

# Como sempre podemos construir um iterador a partir de um iterável (utilizando
# iter()) A função a seguir "generaliza" a anterior:

def meuzip2(c1:Iterable, c2:Iterable) -> Iterator:
    it1 = iter(c1) # Criando os iteradores a partir dos iteráveis 
    it2 = iter(c2)
    while True:
        try:
            e1,e2 = next(it1), next(it2)
            yield e1, e2
        except StopIteration:
            return

# meuzip2 funciona com listas, tuplas e iteradores

print(list(meuzip2([1,2,3], range(3))))
print(list(meuzip2(contar(4), (1,2,3,4))))
