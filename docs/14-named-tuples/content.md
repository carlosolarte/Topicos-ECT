## Named Tuples

--- 
## Nesta aula... 

- Utilizar Namedtuples para representar objetos simples 

---
## Tuplas

Já utilizamos várias vezes tuplas como uma forma de organizar informações de
forma simples:

```python
P = (0.0, 0.0) # Um ponto no plano cartesiano

# Enumerate retorna uma sequência de tuplas: 
for i,x in enumerate(stream):
  # i é o índice
  # x é o valor armazenado em stream
```

---
## Tuplas

Utilizamos a notação de índices para acessar os elementos:

```python
P = (0.0, 0.0)
print(P[0])
```
> _As tuplas são imutáveis_: Lembre que os elementos das tuplas __não podem ser modificados__
---

### O problema de acesso

No exemplo da última aula, precisávamos saber o número de coluna para acessar os elementos:

```python
def rowdata():
    url = "./owid-covid-data-topicos.csv"

    with open(url) as cvsfile:
        cr = csv.reader(cvsfile)
        _ = next(cr)
        for l in cr:
            yield l

def brasil(data):
    '''Só as informações do Brasil'''
    return filter(lambda row: row[2] == "Brazil", data)
```

---
### O problema de acesso

E se o arquivo mudar? Será que existe  uma forma melhor para acessar os elementos?

Poderíamos utilizar classes:

```python
class DadosCovid:
  def __init__(self, pais, casos,.....)
    self.pais = pais
    self.casos = casos
    ...

```

> Mas isso parece muito código para simplesmente apresentar e filtrar informações.

---
### Named Tuples

Adicionam nomes legíveis a cada um dos valores armazenados!

```python
from collections import namedtuple

Ponto = namedtuple('Ponto', ['x', 'y'])
P = Ponto(1,2)
print(P) # Ponto(x=1, y=2)
print(P.x) # acessando os elementos
print(P.y)

# De forma alternativa
Ponto = namedtuple('Ponto', "x y")
```

---
### Named Tuples

O desempacotamento funciona como com qualquer tupla:

```python
P = Ponto(1,2)
x,y = P
print(x) # 1
print(y) # 2
```

---
### Named Tuples e arquivos CSV

Podemos modificar facilmente o código do último exercício para gerar Named Tuplas (em lugar de listas).

```python
def rowdata():
    url = "./owid-covid-data-topicos.csv"

    with open(url) as cvsfile:
        cr = csv.reader(cvsfile)
        # Utilizar a primera linha com os nomes das colunas
        Dado = namedtuple("Dado", next(cr))
        for l in cr:
            yield Dado(*l)

```
Note o uso do operador de desempacotamento em `Dado(*l)`

---
### Named Tuples e arquivos CSV

Agora é mais simples acessar os atributos:

```python
it = ( (d.date, d.location,toInt(d.new_deaths))
         for d in rowdata()
         if toInt(d.new_deaths) >=1500
            and d.continent == "Europe")
print(list(it))
```

> Note que `it` é um iterador (que resulta de uma expressão geradora). 

---
### Exercícios

O método `_replace` retorna uma __copia__ de uma tupla. Antes de 
realizar a copia,  é possível mudar alguns dos seus atributos: 

```python
>>> Ponto = namedtuple("Ponto", ["x", "y"])
>>> P = Ponto(0,0)
>>> P2 = P._replace(x=5)
>>> P
Point(x=0, y=0)
>>> P2
Point(x=5, y=0)
>>> P3 = P._replace(x=2,y=-7)
>>> P
Point(x=0, y=0)
>>> P3
Point(x=2, y=-7)
```

> Note que `P` não _muda_! `P2` e `P3` são _copias_ de `P`. 
---

Utilizando essa técnica, faça que a função `rowdata` gere corretamente tuplas
onde todos os valores numéricos sejam `int` e a data seja do tipo `date`. 

> Com isso geramos dados mais estruturados a partir do arquivo CSV!

---
### Exercícios

Faça uma função que receba como parâmetros duas datas `ini` e `fim` (tipo `datetime`) e 
um país (`str`). A função deve gerar os dados relacionados com esse pais entre as duas datas. 

---
### Exercícios

Considere a lista `v=[1,4,3,5]`. 
Precisamos calcular a diferença entre 2 posições consecutivas de `v`:

`[ 4 - 1 , 3 -4 , 5 - 3] = [3,-1,2]`

Implemente uma função geradora que, dada um iterador, gere as diferenças
dos seus elementos como no exemplo anterior. 

---

Agora vamos implementar uma versão alternativa. 

Lembre que os iteradores podem ser consumidos só uma vez. 

A função `tee` permite criar "copias" de um iterador: 

```python
from itertools import tee
l = [1,2,3,4]
it = iter(l)
it1, it2 = tee(it)
>>> next(it1)
1
>>> next(it2)
1
>>> next(it1)
2
>>> next(it2)
2
```
---

O que significa fazer:
```python
l = [1,2,3,4]
it = iter(l)
it1, it2 = tee(it)
_ = next(it2) # descartar o primeiro elemento de it2
z = zip(it1, it2)
```

Como podemos utilizar isso para solucionar o problema das diferenças? 

Utilize essa técnica para implementar uma função que, dado um pais e duas datas, gere
a porcentagem de variação diária dos novos casos (com relação ao dia anterior). 

