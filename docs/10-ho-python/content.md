## Funções de Ordem Superior

--- 
## Nesta aula... 

- Funções de ordem superior 
- Funções `map` e `filter` 
- Funções anônimas 

---

## Funções como objetos de primeira classe

- Funções podem ser tratadas como qualquer outro objeto

- Podemos _retornar_ funções

- Ou utilizar funções como _parâmetros_ de outras funções. 

---

## Funções como objetos de primeira classe

```python
def inc(x):
  return x + 1

>>> type(inc)
< class 'function' >
>>> inc.__call__(3)
4
>>> inc(3)
4
```

> Toda função é "callable" (que pode ser chamada)

---
## Funções como parâmetros

O que faz a função a seguir?

```python
def misterio(f, n):
    return f(n)
```


---
## Funções como parâmetros

```python
print(misterio(inc, 3))
```

Note como passamos `inc` como _parâmetro da função_

Isso funciona com qualquer função (que receba um parâmetro):

```python
print(misterio(math.sqrt, 3))
```

---
## Funções como parâmetros

Note que isto também funciona (como com qualquer objeto)

```python
incrementar = inc # Atribuir
print(incrementar(4))
```

`incrementar` _é uma referência_ à __mesma__ função definida por `inc`

---

## Funções como parâmetros

Qual seria o tipo da função `misterio`?

```python
T = TypeVar('T')
def chamar(f: Callable[[T], T], x:T) -> T:
    return f(x)

print(chamar(inc, 5))
```

Para qualquer tipo `T`, a função `chamar`:
- _Recebe_ uma função do tipo `T -> T`
- _Recebe_ um objeto do tipo `T`
- __Retorna__ um objeto do tipo `T`

---

## A função map

- Recebe uma função 
- Um (ou mais) iteráveis 
- Retorna um objeto `map` (que é um _iterador_)

```python
l = [1,2,3,4]
m = map(inc, l)
print(next(m)) # Protocolo de iteração 
print(list(map(inc,l)))  # Materializando o iterador
```

--- 
## Expressões lambda

No exemplo anterior utilizamos a função `inc`

Será que precisamos definir explicitamente essa função para utilizar `map`?

```python
finc = lambda x: x + 1
print(finc(3))
```

> As expressões lambda são funções __anônimas__ (não precisamos de um nome para
> elas)

```python
print(list(map(lambda x: x+1, [1,2,3,4])))
```

---
## Expressões lambda

Vamos supor que temos uma sequência de tuplas (ini, fim) com o tempo de inicio
e fim de uma atividade. Como podemos calcular a duração de cada atividade?

```python
atividades = [ (1,5), (3,7),(4,20) ]
duracao = list(map(lambda t : t[1] - t[0] , atividades))
print(duracao)
```

--- 
## Map e Compreensão de listas

Note que também podemos utilizar compreensão de listas para resolver o mesmo problema

```python
dur = [ fin - ini for (ini,fin) in atividades ]
print(dur)
```

---
## Filter

A função `filter`
- Recebe como parâmetro uma função do tipo `T -> bool` (um _predicado_)
- Um iterável `L`
- Retorna um iterador com os elementos de `L` que satisfazem o predicado

```python
pares = filter(lambda x: x%2 ==0, range(10))
print(next(pares)) # protocolo de iteração
# Materializando o iterador numa lista
print(list(filter(lambda x: x%2 ==0, range(10))))
```

---
## Filter e compreensão de listas

```python
numpares = [ x for x in range(10) if x % 2 ==0]
print(numpares)
```

---
## Exercícios

1. Considere uma lista de strings. Cada elemento deve representar um número inteiro. 
Porém, alguns dos elementos da lista devem ser descartados porque incluem 
caracteres diferentes a digitos. Sua tarefa consiste em calcular o somatório
das entradas válidas.

```
["3" , "5" , "b5", "", "2" ] -->
3 + 5 + 2 = 10
```
---
## Exercícios

2. Considere um sensor que mede a temperatura em graus Fahrenheit. Precismos
traduzir essas medidas para graus Celcius e identificar as medidas atípicas,
ou seja, aquelas que não pertencem ao intervalo [5-10]. 

3. Implemente a função `filter` (como uma função _geradora_). Escreva as 
anotações de tipos e utilize mypy para verificar que os tipos são corretos. 

