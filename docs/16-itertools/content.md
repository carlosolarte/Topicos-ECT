# Itertools

--- 
## Nesta aula... 

- Algumas outras funções do pacote `itertools`

---
## A função `count`

Dado um valor inicial `i` e um valor opcional `n`, retorna um iterador da sequência:
```
i, i+n, i+2n, i + 3n, ....
```

Note que se parece a `range` mas sem limite superior

---
## A função `count`

Pode ser implementada assim:
```python
def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
```
---
## A função `count`
Podemos implementar `enumerate` a partir de `count` e `zip`:

```python
from itertools import *

def myenum(seq):
    return zip(count(), seq)

print(list(myenum("alo")))
#[(0, 'a'), (1, 'l'), (2, 'o')]
```

---
## A função `cycle`

`cycle` recebe como parâmetro um iterável `l` e retorna
um iterador da sequência `l0, l1, l2,...,ln, l0, l1, l2 ...`

```python
print(list(islice(cycle("alo"),7)))
#['a', 'l', 'o', 'a', 'l', 'o', 'a']
```

---
## A função `cycle`

Segue a implementação:

```python
def cycle(iterable):
    saved = []
    for element in iterable: # Materliazar os elementos
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
```
---
## A função `repeat`

Retorna um iterador que repete o mesmo elemento um número indefinido de vezes. 
Para sequências finitas, o segundo argumento `times` pode ser utilizado:

```python
def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object
```
---
## A função `compress`

A implementação:
```python
def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)
```

Por exemplo: 
```python
sel = cycle([False,True,True])
print(list(compress([1,2,3,4,5,6,7,8,9,10], sel)))
# [2, 3, 5, 6, 8, 9]
```

---
## `dropwhile` e `takewhile`

Já conhecíamos essas funções de Haskell:

```python
def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x): yield x
        else: break

def dropwhile(predicate, iterable):
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

---
## `dropwhile` e `takewhile`

Alguns exemplos:

```python
print(list(takewhile(lambda x: x < 3, range(10))))
# [0, 1, 2]
print(list(dropwhile(lambda x: x < 3, range(10))))
# [3, 4, 5, 6, 7, 8, 9]
```

--- 
## Exercícios

- Utilizando <a href="https://docs.python.org/3/library/itertools.html">`accumulate`</a> implemente uma função que dado um país X e um número
  N, determine o primeiro dia que X superou um número total de  N casos.  A sua função
  não pode utilizar a coluna `total_cases` (só `new_cases`)
--- 
## Exercícios
- Considere os comandos:

``` 
todos = repeat(0) 
cadaN = lambda n: cycle(range(n)) 
escolher = lambda it: (x == 0 for x in it) 
```

Note que podemos utilizar essas construções para gerar _todos_ os dados
ou realizar uma amostragem cada _n dados_. Teste essas construções
com o arquivo da Covid. 

Como poderíamos realizar 
uma amostragem aleatória? Para isso gere uma sequência (infinita) de números
aleatórios (veja o pacote <a href="https://docs.python.org/3/library/random.html">random</a>)
e depois utilize `zip`, `compress`, etc para filtrar os dados. 

