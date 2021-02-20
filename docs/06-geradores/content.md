## Geradores e compreensão de listas

--- 
## Nesta aula... 

Um mecanismo muito útil em Python...  inspirado em... Haskell!

- Entender e utilizar o mecanismo de _compreensão de listas_ e iteradores

- Definir **funções geradores**

- Resolver problemas utilizando essas técnicas

---
## Iteradores

Já sabemos que os laços `for` em Python são um pouco mais gerais que em outras linguagens: 

```python
# Por cada letra na string...
for x in "bom dia!":
    print(x)

l = [1,2,3,4]
# por cada elemento na lista
for x in l:
    print(x)
```

As listas e strings (também os conjuntos e as tuplas) são _iteráveis_. 

---
## Iteradores

> Um _iterável_ é uma sequência física (armazenada) ou um objeto que pode produzir novos valores (__sob demanda__). 

Lembra do conceito de _preguiça_ na última aula?

- Considere um arquivo grande. Não  podemos carregá-lo na memória.  Devemos processar pouco a pouco o conteúdo. 
- Considere um streaming: processamos os dados a medida que vão chegando. 

---
## Protocolo de Iteração

Todo iterador implementa uma operação básica: 

> _`next`_: para retornar o próximo elemento 

Se não tiver mais elementos, _next_ levanta uma exceção __`StopIteration`__

---
## Protocolo de Iteração

Um exemplo simples com um arquivo:

```python
>>> f = open("test.txt")
>>> next(f)
'um\n'
>>> next(f)
'dois\n'
>>> next(f)
'tres\n'
>>> next(f)
Traceback (most recent call last):...  StopIteration
```
> Utilizando _next_ podemos ler, linha por linha, o conteúdo do arquivo

Basicamente estamos _"iterando" pelo arquivo!_

---
## Protocolo de Iteração

Um exemplo simples com um arquivo.

Utilizando um laço `for`

```python
for l in open("test.txt"):
  print(l)
```

> Por cada linha `l` no arquivo... faça ...

---
## Protocolo de Iteração

Sem  utilizar `for`... não muito pythônico...

```python
f = open("test.txt")
while True:
    try:
        l = next(f) # next pode levantar uma excepção 
        print(l)
    except StopIteration:
        break # Fim da iteração
```
Lembra um pouco o famoso `do{ ... }while(!eof)`

---
## Protocolo de Iteração

As listas, conjuntos, tuplas, etc são iteráveis. Portanto, podemos _construir um
iterador_ a partir dessas estruturas. 

```python
l = [1,2,3,4]
iterl = iter(l) # Construir um iterador a partir de l
print(next(iterl))
print(next(iterl))
print(next(iterl))
print(next(iterl))
```
---
## Protocolo de Iteração
As listas, conjuntos, tuplas, etc são iteráveis. Portanto, podemos _construir um
iterador_ a partir dessas estruturas. 

```python
s = {"a","b","c"}
iters = iter(s) # Iterador sobre os elementos de s
print(next(iters))
print(next(iters))
print(next(iters))
```
---
## Protocolo de Iteração

Mais um exemplo... `range!`
```python
r = range(5)
iterr = iter(r)
print(next(iterr))
print(next(iterr))
...
```

Note que podemos construir uma lista a partir de `range`

```python
l = list(range(1,9,2))
print(l) # Imprimir [1,3,5,7]
```

Só lembrando... em Haskell `[1,3 .. 7]`
---
## Outros objetos iteráveis 

Lembra de `enumerate`?

```python
l = ["a","b","c","d"]
for (i, x) in enumerate(l):
    print(f'i={i}, x={x}')
```

Resultado: 
```
i=0, x=a
i=1, x=b
i=2, x=c
i=3, x=d
```
---
## Outros objetos iteráveis 

Lembra de `enumerate`?
```python
e = enumerate(l)
print(next(e)) # Podemos iterar e!
print(next(e))
```
---
## Iteradores

- Um _protocolo_ simples: `next` / `StopIteration`
- Normalmente utilizamos _laços `for`_: por cada elemento na sequência...
- Listas, conjuntos, tuplas, etc podem ser iterados.

```python
l = [1,2,3]
next(l) # Erro!! As listas não são iteradores
it = iter(l) # Mas iter retorna um iterador a partir de um iterável
next(it)
```

---
## Compreensão de listas

Alguns exemplos (sem utilizar a linguagem):

```
S = { x | x >=0 e x < 10 } # 0,1,2,...,9
S = { 2x | x >=0 e x <10 } # 0,2,4,...,18
S = {x | x >=0 e x <10 e x =/= 5} = # 0 ,1,2,3,4,,6,7,8,9
```
Essas construções são muito comuns (e úteis) 

Inspirados em linguagens como Haskell, Python (e outras) implementam compreensão de listas

---
## Compreensão de listas

Assuma que precisamos incrementar em 1 cada um dos elementos de uma lista:

```python
l = [1,2,3]
for i in range(len(l)):
    l[i] = l[i]+1

print(l)
```

afff... muito feio! 

Note que estamos modificando `l`.

---
## Compreensão de listas
Assuma que precisamos incrementar em 1 cada um dos elementos de uma lista:

A forma pythônica... utilizando _compreensão de listas_

```python
l = [1,2,3]
il1 = (x+1 for x in l)
print(next(il1))
print(next(il1))
print(next(il1))
```

Note que a expressão "__`x+1 for x in l`__" é um iterador

> Em palavras: "Gere" os elementos da forma `x+1` por cada x em `l`

---
## Compreensão de listas
Podemos criar listas (conjuntos, tuplas, etc) a partir de iteradores. 

```python
l1 = list(range(10))
l2 = [x for x in l1]
l3 = list(x+1 for x in range(10))
print(l1)
print(l2)
print(l3)
```

---
## Computação Preguiçosa 

Um iterador __não materializa os valores__.

Os valores são calculados só quando forem utilizados

```
from time import sleep
def incdevagar(n):
    '''retorna n+1 depois de 2 segundos'''
    sleep(2)
    print("terminei!")
    return n+1
```

---
## Computação Preguiçosa 

Um iterador não materializa os valores.
```python
it1 = (incdevagar(x) for x in [1,2,3])
```
 > `it1` tem o "potencial" de gerar uma sequência... mas ainda não calculou nada

 ```python
# Só 2 segundos (para calcular o primeiro elemento)
print(next(it1)) 
```

---
## Computação Preguiçosa 
Se materializamos a estrutura, todos os elementos devem ser calculados:

```python
it1 = (incdevagar(x) for x in [1,2,3]) 
l = list(it1) # 6 segundos
print(l)
# De forma alternativa
l = [incdevagar(x) for x in [1,2,3] ] # 6 segundos
print(l)
```

---
## Compreensão de listas

Podemos utilizar compreensão de listas para _filtrar_ alguns elementos: 
```python
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
```
---
## Compreensão de listas

Podemos utilizar compreensão de listas para _filtrar_ alguns elementos: 
```python
l = [x for x in range(100) if ehPrimo(x)]
print(f'primos: {l}')
```

---
### Geradores

Com compreensão de listas conseguimos (_expressões geradoras_):
 - Gerar novas sequências a partir de sequências já definidas
 - Filtrar elementos (`if...`)
 - Realizar operações por cada elemento (`[ f(x) for ...]`)

```python
l = [1,2,3]
# l2 é uma lista
l2 = list( x+1 for x in l)
print(l2) # [2, 3, 4]
# De forma alternativa
l3 = [ x+1 for x in l]
print(l3) # [2, 3, 4]
```
---
### Geradores
Também podemos gerar conjuntos
```python
s1 = { x+1 for x in l }
s2 = set( x+1 for x in l)
print(s1) # {2, 3, 4}
print(s2) # {2, 3, 4}
```
> `x+1 for x in l` é um _expressão geradora_ que podemos __materializar__ como uma lista, set, etc. 

---
## Geradores (Expressões)

```python
>>> g = (x+1 for x in l)
>>> print(g)
< generator object < genexpr > at 0x10cc98270 >

```
> `g` é um _gerador_ e não uma lista!

---
## Geradores (Expressões)

Os geradores podem ser utilizados só uma vez!
```python
>>> l = [1,2,3]
>>> g = (x+1 for x in l)
>>> l1 = list(g)
>>> l2 = list(g) # g já foi consumido!
>>> print(l1)
[2, 3, 4]
>>> print(l2) 
[]
```
---
## Funções Geradoras

Como geramos a sequência Fibonacci?

```
1  1  2  3  5  8  13 ....
```

Parece um pouco difícil utilizando só _expressões geradoras_

---
## Funções Geradoras
Lembra da implementação imperativa?

```python
def nFib(n):
    '''retorna o elemento n da sequência fibonacci'''
    a1,a2 = 1,1
    if n <= 2: return 1
    for i in range(n -2):
        novo = a1+a2
        a1,a2 = a2, novo
    return novo
```

Como podemos __gerar__ a sequência? 

---
## Funções Geradoras
Uma função geradora utiliza _`yeild`_ (em lugar de __`return`__) para gerar
o próximo elemento

```python
def fibseq(n):
    '''Gera os n primeiros elementos da sequência'''
    a1,a2 = 1,1
    yield a1 # Primeiro elemento
    yield a2 # segundo elemento
    for i in range(n -2):
        novo = a1+a2
        a1,a2 = a2, novo
        yield novo

l = list(fibseq(10)) # gerador + materialização
print(l)
```
---
## Funções Geradoras
O comando `yield` __pausa a execução__ (_execução preguiçosa!_)

Segue uma sequência __infinita__:

```
def fibseqinf():
    '''Sequência infinita'''
    a1,a2 = 1,1
    yield a1 # Primeiro elemento
    yield a2 # segundo elemento
    while True:
        novo = a1+a2
        a1,a2 = a2, novo
        yield novo #Depois de gerar, pausa!

from itertools import islice
# Como a função "take" em Haskell
l = list(islice(fibseqinf(), 10))
print(l)
```

---
## Funções Geradoras
O comando `yield` pausa a execução (execução preguiçosa!)

Formas alternativas: 

```python
g= fibseqinf()
for i in range(10):
    print(next(g))

#Também podemos utilizar compreensão de listas!
g= fibseqinf() # Por que precisamos disto?
lfib = [ next(g) for x in range(10) ]
print(lfib)

```
> Por que instanciamos de novo `g`?

---
## Funções Geradoras
Mais uma alternativa.

- `fibseqinf` gera uma sequência infinita
- Podemos escrever uma função para "consumir" os n primeiros elementos

```python
def fibseqinfn(n):
    '''n primeiros elementos utilizando fibseqinf'''
    g = fibseqinf()
    for i in range(n):
        yield next(g)

l = list(fibseqinfn(10))
```

---
## Funções Geradoras
Mais uma alternativa:
```python
def fibnenum(n):
    '''Gerar os n primeiros termos utilizando uma enumeração'''
    for (i,x) in enumerate(fibseqinf()):
        if i>=n: break
        yield x

l = list(fibnenum(10))
```
> Note que tudo isto funciona porque os geradores são _preguiçosos_. `Enumerate`
> __não__ está enumerando todos os elementos da sequência. Ele retorna os elementos __sob demanda__!

---
## Para Casa
Os exercícios a seguir devem ser resolvidos utilizando _expressões geradoras e/ou 
funções geradoras_. 

1. "Gerar" os fatores primos de um número n (todos os números primos que dividem a n). Por exemplo, para n=12, a sequência 2,3 deve ser gerada

1'. (extra). "Gerar" uma sequência de tuplas (p,m) com a  decomposição em fatores primos de um número n. Por exemplo, para n=12, a sequência deveria ser (2,2), (3,1) porque 2^2 * 3^1 = 12

Dica: Pense em construir um gerador da sequência (infinita) de todos os números primos. 
---
## Para Casa
Os exercícios a seguir devem ser resolvidos utilizando _expressões geradoras e/ou 
funções geradoras_. 

2. "Gerar" a coluna `n` de uma matriz. Lembre que uma matriz pode ser vista como uma lista de listas:
```
[ [1,2,3], [4,5,6], [7,8,9]]
```

Para este exemplo, se `n=1`, a sequência 2,5,8 deve ser gerada. 

---
## Para Casa
Os exercícios a seguir devem ser resolvidos utilizando _expressões geradoras e/ou 
funções geradoras_. 

3. Faça uma função que receba como parâmetros duas listas l1 e l2. Você pode assumir que `len(l1) == len(l2)`. A função deve
gerar uma sequência de tuplas (x1,y1), (x2, y2)... onde `xi` pertence a `l1` e `yi` pertence a `l2`.

```
l1 = [1,2,3]
l2 = ["a","b","c"]
res = list(func(l1,l2)) #  [(1, 'a'), (2, 'b'), (3, 'c')]
```
