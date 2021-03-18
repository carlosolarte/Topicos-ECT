## Ordenando e Agrupando

--- 
## Nesta aula... 

- A função `sorted`
- A função `groupby`

---
## Ordenar

Ordenar uma sequência `l` significa:
 1. Produzir uma _permutação_ de `l`
 2. Que satisfaça o critério de ordenação 

> A lista ordenada deve ter os mesmos elementos que a lista original!

---
### Ordenar em Python

```python
# Ordenação

l = [5,3,1,6]
ls = sorted(l)

print(l) #  [5, 3, 1, 6]
print(ls) # [1, 3, 5, 6]
```

> Note que `sorted` retorna uma lista

---
### Ordenar de forma decrescente 

A função `sorted` recebe um parâmetro opcional `reverse`:

```
ls2 = sorted(l, reverse=True)
```

---
### Ordenar listas

O método `sort` da classe lista permite ordenar modificando a própria lista:

```
l = [3,1,6,8]
l.sort()
print(l)
```

---
### Ordenar:  O parâmetro `key`

Considere o problema de ordenar uma lista de palavras:

```python
pals = "Uma frase com Maiúsculas e também minúsculas".split()
# pals = ['Uma', 'frase', 'com', 'Maiúsculas', 'e', 'também', 'minúsculas']

print(sorted(pals))
# ['Maiúsculas', 'Uma', 'com', 'e', 'frase', 'minúsculas', 'também']
```

> Na tabela ascii, primeiro se encontram as maiúsculas e depois as minúsculas. 

---
### Ordenar:  O parâmetro `key`

Poderíamos utilizar um `map` para converter tudo para minúscula: 

```python
print(sorted(map(str.lower, pals)))
# ['com', 'e', 'frase', 'maiúsculas', 'minúsculas', 'também', 'uma']

# Utilizando lambda
print(sorted(map(lambda x: x.lower(), pals)))
```

---
### Ordenar:  O parâmetro `key`

Alternativamente, a função `sorted` recebe como parâmetro 
`key`, que  deve ser _uma função_ que recebe um único argumento e retorna a
__chave__ que deve ser utilizada como critério de ordenação. 

```python
print(sorted(pals, key = str.lower))
# ['com', 'e', 'frase', 'maiúsculas', 'minúsculas', 'também', 'uma']

# Utilizando lambdas:
print(sorted(pals, key = lambda x: x.lower()))
# ['com', 'e', 'frase', 'maiúsculas', 'minúsculas', 'também', 'uma']
```

---
### Ordenando tipos estruturados

Considere uma lista de pessoas:
```python
from collections import namedtuple

Pessoa = namedtuple("Pessoa", "nome idade")
lp = [ Pessoa("Pessoa 1", 20), Pessoa("Pessoa 2", 15), 
       Pessoa ("Pessoa 3", 35) ]

```

Como podemos ordenar essa lista utilizando como critério a idade?

---
### Ordenando tipos estruturados

```python
print(sorted(lp, key = lambda x: x.idade))
# [Pessoa(nome='Pessoa 2', idade=15), Pessoa(nome='Pessoa 1', idade=20), 
#  Pessoa(nome='Pessoa 3', idade=35)]

```
Essa construção é bastante comum... e pode ser simplificada: 

```python
from operator import attrgetter
print(sorted(lp, key = attrgetter('idade')))

```

---
### Ordenando tipos estruturados

De fato, podemos utilizar vários critérios de ordenação:

```python
# Primeiro ordenar por idade e, depois, pelo nome
print(sorted(lp, key = attrgetter('idade','nome')))

```
---
# Agrupar Informação

---
### Agrupar  

Considere o conjunto de dados a seguir, representando o número de casos/contágios por dia: 
```
Dado = namedtuple("Dado", "Estado Cidade Casos")
l = [Dado("RN", "Natal", 20), Dado("RN", "Parnamirim", 10),
     Dado("RJ", "Rio", 30) , Dado("RJ", "Niteroi", 50) ]
```

Como podemos acumular/totalizar os valores por estado?

---
### Agrupar  
> A função `groupby` _agrupa_ os elementos de um iterável utilizando uma chave

O resultado é um iterador de tuplas `(k, elems)`:
 - `k` é a __chave__
 - `elems` é um _iterador_ ao grupo de elementos com a mesma chave

```python
from itertools import groupby
for k, elems in groupby(l, key = attrgetter("Estado")):
    print(f'Estado: {k}: {list(elems)}')

# Estado: RN: [Dado(Estado='RN', Cidade='Natal', Valor=20), Dado(Estado='RN', Cidade='Parnamirim', Valor=10)]
# Estado: RJ: [Dado(Estado='RJ', Cidade='Rio', Valor=30), Dado(Estado='RJ', Cidade='Niteroi', Valor=50)]
```

---
### Agrupar  
_Nota_: Antes de chamar a função `groupby`, os dados devem estar ordenados
utilizando o mesmo critério:

```python
l = [1,1,2,2,2,1,3,3,2,2]
for k, elems in groupby(l):
    print(f'Key: {k}: {list(elems)}')

#Key: 1: [1, 1]
#Key: 2: [2, 2, 2]
#Key: 1: [1]
#Key: 3: [3, 3]
#Key: 2: [2, 2]
```
---

### Exercício

1. Dado um parágrafo, retorne a palavra que mais se repete. 
2. Dada uma lista `l`, retorne uma lista com os diferentes valores que aparecem em `l`:

```
l = [1,2,3,2,1,4,1]
resultado: [1,2,3,4]
```

3. Utilizando o exercício da última aula, gere o total (somatório de `new_cases`) do número de casos por continente.
4. Como podemos totalizar o número de casos por continente e por ano?
