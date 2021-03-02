## Funções zip e unzip

--- 
## Nesta aula... 

- Funções `zip` e `unzip` 
- Unpacking

---
## Função Zip

A função zip recebe:

- Zero o mais Iteráveis
- Retorna um objeto zip (iterador)

> O iterador retornado gera tuplas de tamanho n (correspondendo ao número de iteráveis)

---
## Função Zip

Exemplos:

```python
>>> list(zip())
[]
>>> list(zip([1,2,3]))
[(1,), (2,), (3,)]
>>> list(zip([1,2,3],[4,5,6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1,2,3],[4,5,6],[7,8,9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

> Em python, `(1,)`representa uma tupla de um elemento. 

---
## Unpacking (desempacotamento de sequência)
Em python, podemos utilizar o operador de atribuição assim

```python
a = 1
b = 0
a,b = a+1, a+2
print(a,b) # Imprime 2,3
```

> _Atribuição múltipla_: atribuir um conjunto de valores a um conjunto de variáveis.

---
## Unpacking 

De fato, podemos desempacotar uma tupla assim:
```pyhon
t = (1,2)
x,y = t
print(x,y)
```

Já fizemos isso várias vezes: 

```python
>>> for i,v in enumerate("alo"):
...   print(i,v)
...
0 a
1 l
2 o
```

---
## Unpacking 

Essa técnica funciona também com listas: 

```python
>>> a,b,c = [1,2,3]
>>> print(a,b,c)
```

Um pouco mais interessante:
```python
>>> a,*b,c = [1,2,3,4,5]
>>> print(a,b,c)
1 [2, 3, 4] 5
```

---
## Unpacking 
O típico pattern matching que utilizamos em Haskell:
```python
>>> head, *tail = [1,2,3,4]
>>> print(head,tail)
1 [2, 3, 4]
```

---
## Unpacking

Essa técnica pode ser utilizada para chamar funções. Por exemplo:

```python
def soma(x,y): return x + y

t = (1,2) # t é uma tupla
soma(*t) 
3
```

> Note que `*t` desempacota a tupla e fornece os dois parâmetros que `soma` precisa 

---
## Unpacking

Como é que `zip` consegue receber um número não determinado de parâmetros?

```python
def func1(*args):
    for a in args:
        print(f'Argument: {a}')
# Chamando a função com alguns parâmetros

func1(3,"alo")
func1("mundo",4,[1,2,3])

# De fato, podemos  utilizar tuplas!
t = (1,5,[1,2,3],"alo")
func1(*t)
```

---
## A função unzip

Considere uma lista de tuplas:
```python
[ (1,'a'), (2,'b'), (3,'c') ]
```

Como retornamos uma tupla com 2 listas?
```python
( [1,2,3] , ['a', 'b', 'c'])
```

---
## A função unzip
Opção No 1: compreensão de listas:

```python
l = list(zip([1,2,3], "alo"))

def unzip1(l):
    return [ x[0] for x in l] , [ x[1] for x in l]

l1,l2 = unzip1(l)
print(l1,l2) # [1, 2, 3] ['a', 'l', 'o']
```
Um pouco mais elegante:

```zip
def unzip2(l):
    return [ x for x,_ in l] , [ y for _,y in l]
```

---
## A função unzip
Opção No 2: utilizando o próprio zip

```python
def unzip3(l):
    return tuple(zip(*l))

print(unzip3(l)) # ((1, 2, 3), ('a', 'l', 'o'))
```

> Note que estamos retornando uma tupla de tuplas

---
## A função unzip
Opção No 2: utilizando o próprio zip

Podemos utilizar map para retornar uma tupla de listas

```python
def unzip4(l):
    return tuple(map(list, zip(*l)))

print(unzip4(l))  # ([1, 2, 3], ['a', 'l', 'o'])
```

---
## A função unzip
Opção No 3: A forma boooring.... ;-)

```python
def unzip5(l):
    l1,l2 = [], []
    for x,y in l:
        l1.append(x)
        l2.append(y)

    return l1,l2

print(unzip5(l)) # ([1, 2, 3], ['a', 'l', 'o'])
```

---
## Exercícios

1. Como você imeplementaria `enumerate` utilizando `zip`?
2. Utilize desempacotamento de sequências para implementar uma função que retorne o penúltimo e o último elemento de uma lista (não vazia) 

---
## Exercícios

3. Lembre que os iteradores consumem, __e não armazenam__, os valores consumidos:

```python
>>> l = [1,2,3]
>>> it = iter(l)
>>> l1 = list(it)
>>> l2 = list(it)
>>> l2
[]
```

Como podemos utilizar essa ideia para implementar a função que agrupa os elementos de uma sequência de 2 em 2? 
```
[1,2,3,4,5] -- > [ (1,2), (3,4) ]
```
Podemos generalizar essa ideia para gerar agrupamentos de n elementos?
---
## Exercícios

4.  Lembra do fatiamento de listas?
```
>>> l = [1,2,3,4,5]
>>> l[0::2]
[1, 3, 5]
```
Podemos utilizar essa ideia para implementar a função de agrupamento do item anterior?

---
## Exercícios

5. Como poderíamos calcular o produto escalar de dois vetores?

6. Implemente sua própria função `zip` (como uma função geradora). 

