## Listas, Tuplas e Conjuntos em Python

--- 

### Objetivos

Nesta aula utilizaremos Tuplas, Listas e Conjuntos em Python

Aprenderemos alguns dos métodos da biblioteca padrão para manipular essas estruturas

Resolveremos problemas utilizando essas estruturas 

---
## Python

Já sabemos que Python e Haskell são bem diferentes

Python implementa alguns conceitos da programação funcional

Hoje não utilizaremos conceitos *funcionais*... só estudaremos  o uso de algumas
estruturas de dados (de forma _imperativa_)

---
## Tuplas

As tuplas armazenam vários valores de forma agrupada

Depois de criada, uma tupla é _imutável_ (__como em Haskell!__)

Ou seja, não podemos modificar os valores armazenados

---
## Tuplas

Alguns exemplos:
```python
a = (1,2,3)
a[0] # Primeiro elemento da tupla
# Uma tupla de tuplas!
b = ((1, 'cálculo',10), (2, 'álgebra', 9))
# Erro! a[1] = 5 ... 'tuple' object does not support item assignment
```

---
## Tuplas
Uso típico: retornar mais de um valor em uma função:
```python

#Utilizando tuplas para retornar mais de um valor
def sumprod(x, y):
    '''Retorna a soma e o produto de um número'''
    return (x+y, x*y)

# Atribuir em a o primeiro resultado e em b o segundo
a,b = sumprod(3,5) 
```

---
## Tuplas e Tipos
Utilizaremos o tipo `Tuple[int,int]`: 

```python
# Incluir Tuple do pacote typing
from typing import Tuple

#Com anotações de tipos
def sumprodtipos(x:int, y:int) -> Tuple[int, int]:
    '''Retorna a soma e o produto de um número'''
    return (x+y, x*y)

```
---
## Tuplas e Tipos

A função a seguir retorna o primeiro elemento de uma tupla:
```
def first(t):
  return t[0]
```

Qual seria o tipo dessa função?

Se `t` é uma tupla do tipo `Tuple[int, float]` o tipo (de retorno) de `first` deveria ser `int`

Mas se `t` é do tipo `Tuple[str,str]`?

De forma geral: Para qualquer tipo `A` e `B`, se `t` é do tipo `Tuple[A,B]`, `first(t)` deve
retornar um objeto do tipo `A`.

---
## Tuplas e Tipos

Para especificar "para todo tipo `T1` e `T2`..." utilizaremos `TypeVar`:

```python
from typing import Tuple, TypeVar
T1 = TypeVar('T1')
T2 = TypeVar('T2')

def primeiro(t: Tuple[T1,T2]) -> T1:
    '''Retorna o primeiro elemento de uma tupla'''
    return t[0]

```
---
## Listas
Diferente de  Haskell, as listas de Python são __mutáveis__:

- Elementos podem ser inseridos e eliminados
- Podemos modificar os elementos da lista

Além disso, as listas de Python podem conter elementos de diferentes tipos

Note que "`tail l`" em Haskell __não modifica__ a lista `l`: `tail` retorna 
_outra_ lista que contem os elementos de `l` sem o primeiro. 

---
## Listas
Declaração:

```python
l = [] # Lista vazia
l = [1,2,3] 
l2 = [1.93, 'alo', (0,'aula')] 
```

---
### Acesso e Fatiamento (slicing) de Listas
- `l[3]`: 4to elemento da lista
- `l[-1]`: último elemento da lista
- `l[2:5]`: sublista [ l[2],l[3],l[4] ]
- `l[::2]`: sublista nos índices pares
- `l[::-1]`: reverso da lista

De forma geral: `l[ini:fim:inc]`

---
## Operações básicas:

Pertence:
```python
>>> 3 in [1,5,2,3,6]
True
```

Tamanho:
```python
>>> len ([1,2,3,4])
4
```

---
## Percorrer uma lista

Por cada elemento `x` em `l`:
```python
for x in l:
    print(x)
```

Utilizando índices (não muito pythónico):
```python
for i in range(len(l)):
    print(l[i])
```

A forma pythónica:
```python
# enumerate retorna tuplas (indice, valor)
for (i,v) in enumerate(l):
    print(f'indice={i}, valor={v}')
```

---
## Algumas operações em listas
As listas são mutáveis!

Adicionar no final da lista:
```python
>>> l = [1,2,3]
>>> l.append(4)
>>> l
[1, 2, 3, 4]
```
Concatenar:
```python
l = [1,2,3] + [4,5,6]
```
Inserir numa posição

```python
l = [1,2,3]
l.insert(0,-10) # [-10,1,2,3]
```

---
## Algumas operações em listas
Remover o último elemento
```python
l = [1,2,3]
l.pop() # l = [1,2]
```
Novamente... compare com Haskell
```haskell
Prelude> l = [1,2,3,4]
Prelude> init l -- retorna uma lista que contem os elementos de l sem o último
[1,2,3]
```

---
## Algumas operações em listas

Remover em uma posição
```python
>>> l = [1,2,3]
>>> l.pop(0) # Retorna o elemento eliminado
1
>>> l
[2, 3]
```
---
## Tipos em Listas
Seguem alguns exemplos:
```python
from typing import List, TypeVar

T1 = TypeVar('T1')

def tamanho(l:List[T1]) -> int:
    '''Retorna o número de elementos de uma lista'''
    return len(l)

def ehVazia(l:List[T1]) -> bool:
    '''Determinar se l é vazia'''
    return l == []
```

---
## Conjuntos (Set)

Coleção de elementos _não repetidos_

```python
>>> s = {1,2,3,2,1}
>>> s
{1, 2, 3}
```

A ordem é irrelevante:

```python
>>> {1,2,3} == {3,2,1}
True
```

---
## Conjuntos (Set)
União: parece funcional! Retorna um novo conjunto
```python
>>> s1 = {1,2,3}
>>> s2 = s1.union({3,4,5})
>>> s2
{1, 2, 3, 4, 5}
>>> s1
{1, 2, 3}
```
---
## Conjuntos (Set)
União: parece funcional! Retorna um novo conjunto

Mas... podemos atualizar com a união:
```python
>>> s = {1,2,3}
>>> s.update({3,4,5})
>>> s
{1, 2, 3, 4, 5}
```
O utilizar atribuição (que não existe em Haskell!)
```python
>>> s = {1,2,3}
>>> s = s.union({3,4,5})
>>> s
{1, 2, 3, 4, 5}
```
---

# Jupyter-notebook
