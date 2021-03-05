## Reduções

--- 
## Nesta aula... 

- Reduções 
- Funções `reduce`, `sum`, `any`, `all`, etc
- Pacote `functool` e `operator`

---
### Recursão e reduções

Considere as funções para calcular o somatório e produto dos elementos de uma lista:

```python
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
```

> O código é quase igual... só mudamos a forma de _acumular_ os valores e o 
> elemento inicial (do _caso base_).

---
## A função `reduce`

`reduce` é uma função de _ordem superior_ que recebe:
- Uma função `f` (que recebe 2 parâmetros)
- Uma sequência 
- Um valor inicial (opcional) 

e _reduze_ a sequência, de esquerda para direita,  a um valor utilizando a função `f`. 

---
## A função `reduce`

Segue a implementação em Python:

```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```
---
## A função `reduce`

Alguns exemplos:
```python
from functools import reduce
def soma(x,y): return x + y

s = reduce(soma, [1,2,3],0)
```

O resultado seria:
```
value = 0
value = soma(0, 1) = 1
value = soma(1, 2) = 3
value = soma(3, 3) = 6
```
De fato, não precisamos do valor inicial:

```
s = reduce(soma, [1,2,3]) # value inicia em 1
```

---
### Lambda e o módulo `operator`

Não precisamos implementar a função `soma`:

```python
s = reduce(lambda x,y: x + y, [1,2,3])
```

De fato, a maioria de operações básicas (aritméticas, booleanas, relacionais, etc)
estão definidas no módulo `operator`

```python
import operator
print(reduce(operator.add, [1,2,3]))
```

---
### Lambda e o módulo `operator`

Note que a função para calcular o somatório já existe:

```python
s = sum([1,2,3,4])
```

---
## Maior elemento

Calcular o maior elemento de uma sequência
```python
def maior(x,y):
    return x if x > y else y

print(reduce(maior, [1,5,2,5,7,10,4]))
```

De fato, essa função já existe em Python:

```python
m = max([1,5,2,5,7,10,4])
```

> `max` não está definida para listas vazias 

---
## `reduce` e expressões booleanas

Vamos supor que precisamos testar se todos os elementos
de uma sequência satisfazem certa condição, por exemplo, 
se todos os números da sequência são pares. 

```python
def ehPar(n): return n % 2 == 0
```

Precisamos _reduzir_ a lista utilizando uma conjunção:

```python
print(reduce(operator.and_, map(ehPar, [2,4,6,8])))
```

> Note que o identificar da função é `and_`
---
## `reduce` e expressões booleanas

O que acontece com a lista vazia?

```python
# print(reduce(operator.and_, map(ehPar, []))) # Erro!
```

`reduce` precisa de _pelo menos_ um elemento:
```python
print(reduce(operator.and_, map(ehPar, []),True))
```

> Por _vacuidade_, todos os elementos de uma lista vazia são pares

---
## `reduce` e expressões booleanas

A função `all` retorna `True` se `bool(x)` é `True` 
para cada elemento `x` do iterável. 

```python
bool(5) # True
bool(0) # False
bool("") # False
bool("alo") # True
bool([]) # False
bool([False]) # True
```
Por exemplo:

```python
print(all([1,3,2,0,4])) # False
print(all([1,5,2])) # True
```

---
## `reduce` e expressões booleanas
Voltando para nosso exemplo:

```python
print(all(map(ehPar, [2,4,6,7,8]))) # False
print(all(map(ehPar, [2,4,6,8]))) # True
```
---
## Exercícios
- Implementar a função fatorial utilizando `reduce`. 
- Calcular o somatório das posições pares de  um vetor
- Determinar de todas as palavras de uma lista de strings tem, pelo menos, 5 caracteres
- Dada uma lista de números, ex [1,2,3], retornar a string "1,2,3".
---
## Exercícios
- Como você poderia utilizar `reduce` para calcular o tamanho de uma lista?
- Já vimos como testar se *todos* os elementos do iterável satisfazem uma
  condição. Como poderíamos testar se pelo menos um deles satisfaze a condição?
  Implemente uma função para isso. Considere o caso da lista vazia. 
  (Nota, essa função já existe: `any`)
