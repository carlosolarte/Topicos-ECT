## Permutações e Combinações

--- 
### Nesta aula... 

- As funções `product`, `permutations` e `combinations`

---
### Produto Cartesiano

Dados dos conjuntos A e B, o produto cartesiano $A \times B$ está definido como
{$(x,y) | x \in A$  e $y \in B $}

Lembre que $|A \times B| = |A| \times |B|$. 

>Ex. {1,2} $\times$ {3,4} = {(1,3),(2,4),(2,3),(2,4)} 

---
### Produto Cartesiano

```
from itertools import product

disciplinas = ["LIP", "LOP"]
turmas = ["A","B","C","D"]

print(list(product(disciplinas, turmas)))
# [('LIP', 'A'), ('LIP', 'B'), ('LIP', 'C'), ('LIP', 'D'), 
#  ('LOP', 'A'), ('LOP', 'B'), ('LOP', 'C'), ('LOP', 'D')]
```
---

### Produto Cartesiano
De fato, `product` trabalha com qualquer número de iteráveis

```
print(list(product([1,2],[3,4],[5,6])))

#[(1, 3, 5), (1, 3, 6), 
# (1, 4, 5), (1, 4, 6),
# (2, 3, 5), (2, 3, 6), 
# (2, 4, 5), (2, 4, 6)]
```

---
### Permutações
Uma permutação é um agrupamento que pode ser formado mudando as posições dos 
elementos de um conjunto dado.

Por exemplo, as permutações de {A,B,C} são:

> ABC, ACB, BAC, BCA, CAB, e CBA

Lembre que o número de permutações de n elementos é n!

---
### Permutações

Por exemplo, podemos produzir anagramas com a função `permutations`

```
# Permutações
print(list(permutations("mundo")))
#[('m', 'u', 'n', 'd', 'o'), ('m', 'u', 'n', 'o', 'd'),
# ('m', 'u', 'd', 'n', 'o'), ('m', 'u', 'd', 'o', 'n'),
# ('m', 'u', 'o', 'n', 'd'), ('m', 'u', 'o', 'd', 'n'),
# ('m', 'n', 'u', 'd', 'o'), ('m', 'n', 'u', 'o', 'd'),
# ...
# ('o', 'd', 'n', 'u', 'm')]
```

---
### Permutações

Por exemplo, podemos produzir anagramas com a função `permutations`

```python
print(list(
       map( lambda x: "".join(x), 
            permutations("alo"))))

#['alo', 'aol', 'lao', 'loa', 'oal', 'ola']
```

---
#### Problema de optimização (por força bruta!)

Vamos supor que temos 3 horários, 2 disciplinas e 3 professores: 
```python
horarios = ["M","T","N"]
disiciplinas = ["LOP","LIP"]
profs = ["P1", "P2", "P3"]
```

Primeiro calculamos todas as turmas:
```python
Turma = namedtuple("Turma", "disciplina horario")
turmas = [ Turma(*x) for x in product(disciplinas,horarios)]
```
---
#### Problema de optimização (por força bruta!)
Os professores definem preferências por disciplinas e horários:

```python
prefdisciplina = { ("P1", "LOP") : 8, ("P1", "LIP") : 10,
                   ("P2", "LOP") : 9, ("P2", "LIP") : 7,
                   ("P3", "LOP") : 6, ("P3", "LIP") : 9 }

prefhorario = { ("P1", "M") : 4, ("P1", "T") : 7 , ("P1", "N") : 10,
                ("P2", "M") : 10,("P2", "T") : 9 , ("P2", "N") : 3,
                ("P3", "M") : 8, ("P3", "T") : 8 , ("P3", "N") : 8 }
```
---
#### Problema de optimização (por força bruta!)
Devemos criar permutações de P1,P1,P2,P2,P3,P3

```python
def flat(ls):
    '''de listas de lista para uma lista:
       [ [a,b],[],[c,d]] --> [a,b,c,d]
    '''
    return (x for l in ls for x in l)

lprof = flat( ([x,x] for x in profs))

#Todas as configurações possíveis (algumas repetidas)
opcoes = permutations(lprof)
```

---
#### Problema de optimização (por força bruta!)

Dada uma turma e um professor, podemos calcular o nível de preferência assim:

```python
def vpreferencia(turma,prof):
    '''preferência de um professor'''
    return prefdisciplina[(prof, turma.disciplina)] + \
           prefhorario[(prof, turma.horario)]
```

A ideia é encontrar uma solução que maximize esse valor
---
#### Problema de optimização (por força bruta!)

Considere uma possível permutação: P2, P1, P3, P2, P3, P1

Vamos utilizar um zip para produzir algo como:

> (P2, turma1, pref) , (P1, t2, pref), (P3, t3, pref), (P2, t4, pref)...

```python
def zipwith(it1, it2, f):
    '''zip entre it1, it2 utilizando a função f'''
    it1 = iter(it1)
    it2 = iter(it2)
    while True:
        try:
            a = next(it1)
            b = next(it2)
            yield(a,b,f(a,b))
        except StopIteration:
            break
```

---
#### Problema de optimização (por força bruta!)

Para gerar todos os dados, com preferências, é só utilizar um `map`:

```python
preferencias = map(lambda opc: list(zipwith(turmas, opc, vpreferencia)), 
                   opcoes)
```

Um exemplo de um elemento em `preferencias`:

```
[(Turma(disciplina='LIP', horario='M'), 'P3', 17), 
 (Turma(disciplina='LIP', horario='T'), 'P3', 17), 
 (Turma(disciplina='LIP', horario='N'), 'P1', 20), 
 (Turma(disciplina='LOP', horario='M'), 'P2', 19), 
 (Turma(disciplina='LOP', horario='T'), 'P2', 18), 
 (Turma(disciplina='LOP', horario='N'), 'P1', 18)]
```

---
#### Problema de optimização (por força bruta!)

Como escolher a melhor configuração?

Comparamos cada elemento em `preferencias` utilizando o somatório das preferências:

```python
melhor = max(preferencias , 
             key = lambda l: sum(map(lambda x: x[2],l)))

```
---
#### Problema de optimização (por força bruta!)

> Existem técnicas muito mais eficientes que __força bruta__ para solucionar este tipo de problemas. Veja <a href="https://en.wikipedia.org/wiki/Combinatorial_optimization"> aqui</a>. 

> Note que o número de configurações/permutações cresce muito rápido!
---
### Combinações
As combinações são como as permutações mas a ordem dos elementos é irrelevante. 

O número de combinações de $p$ elementos que podem ser formadas a partir de um 
conjunto de $n$ elementos é $\frac{n!}{p! (n-r)!}$.

---
### Combinações

```
# Combinações
print(list(combinations([1,2,3],3)))
#[(1, 2, 3)]
print(list(combinations([1,2,3],2)))
#[(1, 2), (1, 3), (2, 3)]
print(list(combinations([1,2,3],1)))
#[(1,), (2,), (3,)]
```

---
### Exercícios

- A função `permutations` aceita como segundo argumento o número de elementos
  que deve ter cada permutação. Como poderíamos gerar todos  os palíndromos que
  podem ser formados com as letras de uma palavra?

- Considere que você tem 5 notas, cada uma de valor diferente. Quais seriam
os valores dos artículos que você poderia comprar sem receber troco?

- Considere um grupo de 5 pessoas:
 1. Quantas chapas para presidente e vice-presidente podemos formar?
 2. Quantas equipes de trabalho de 3 membros podemos formar?

> Não utilize as fórmulas ;-)
