## Python Básico

--- 

### Objetivos

O objetivo da aula é introduzir comandos básicos em Python:
 - Terminal interativo de comandos
 - Variáveis e tipos
 - Operadores e expressões
 - Entrada e saída
 - Controle de fluxo (`if`, `while`, `for`)
 - Definição de funções
 - Documentação 
 - _Anotações de tipos (mypy)_

 ---

## A Linguagem de Python

Por que Python?

- Simplicidade
- Facilidade de aprendizado e de correção de erros
- Código limpo
- Código multiplataforma (Linux/Mac/Windows)
- **Suporta o paradigma funcional**

---
## A Linguagem Python

- É uma linguagem _interpretada_
- Suporta um terminal de comandos interativo
- Qualquer comando da linguagem pode ser executado
    - Agiliza a programação
    - Facilita a depuração de erros
    - Visualiza ajuda das funções/classes declaradas
- **Importante**: confira se a versão do Python é a 3.X

---
## Terminal de comandos interativo
<video data-autoplay src="./img/terminal.mp4"></video>

---
## Arquivos .py
<video data-autoplay src="./img/exec.mp4"></video>

--- 
## Jupyter Notebook
<video data-autoplay src="./img/jupyter.mp4"></video>

--- 
## Jupyter Notebook

Também é possível utilizar Google [Colaboratory](https://colab.research.google.com/)

---

## Zen do python

```
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
```
---
## Diferenças entre C++ e Python

 - _Tipagem dinâmica_: Os tipos são determinados automaticamente

 ```python
 x = 4 
 type(x) # int
 s = "alo"
 type(s) # str

 ```

> Nesta disciplina vamos utilizar anotações de tipos como forma de documentar 
> o código
--- 
## Diferenças entre C++ e Python
-  A indentação é obrigatória: 

```python
def f(n):
   return n+1 # Código indentado 

while c:
   ....
```
--- 
## Diferenças entre C++ e Python
-  `;` não é necessário

```python
i = 5
i +=1
print(i)
```

> Em programação funcional (pura), `i+= 1` não faz sentido!

Só por hoje está permitido utilizar esse tipo de instruções

--- 
## Diferenças entre C++ e Python

#### Estruturas de controle

Em programação funcional não precisamos delas!

Mas é só por hoje para introduzir a linguagem.
--- 
## Diferenças entre C++ e Python

Estruturas de decisão:

```python
if x % 2 == 0:
 print(f'{x} e par')
else:
 print(f'{x} e impar')
```

Não escreva `if (x%2 ==0)`... isso não é pythónico!

---

## Diferenças entre C++ e Python
Laços `while`
 
Funcionam como  em C++ (do-while não existe)

```python
while x >= 0:
    x -= 1
    print(x)
```

---
## Diferenças entre C++ e Python
-  Laços for

```python
for i in range(0,n): # até n-1
   print(i)
```

A função `range` vai ser muito importante nas próximas aulas!

Os laços `for` de Python se podem ler como 

"por cada elemento de..."
```python
for x in "alo":
    print(x)
```

---
## Diferenças entre C++ e Python

O que imprime c++?
```cpp
cout<< (3 < 5 < 2 ) ;
```
---
## Diferenças entre C++ e Python

O Que imprimiria c++?
```cpp
cout<< (3 < 5 < 2 ) ;
```

Em Python funciona!
```python
print ( 3 < 5 < 2 ) #False!
```
---
## Tipos

Vamos utilizar [mypy](http://mypy-lang.org/) para verificar os tipos dos nossos programas

```python
def f(x,y):
  return x+y;
```
O que faz a função f?

---
## Tipos

Vamos utilizar [mypy](http://mypy-lang.org/) para verificar os tipos dos nossos programas

```python
def f(x,y):
  return x+y;
```
O que faz a função f?
 - Soma dois números (inteiros ou float)
 - Concatena duas strings
 - De fato, executa o método `__add__` de qualquer objeto que o implemente!

---
## Tipos

O que faz a função f?
```python
print(f(3,2))
print(f("alo ","mundo"))
print(f("alo ",2)) # Erro!
```

> Isso é uma forma muito poderosa de _polimorfismo_

Principio de Peter Parker: __"Com grandes poderes vêm grandes responsabilidades"__

---
### Linguagens compiladas e interpretadas 
O interpretador de Python reporta erros em uma linha 
  caso esta linha seja executada

```
def g(x):
    print(y)
```

Se `g` não é executada, o interpretador não vai saber que `y` não está declarada
na função `g`. 

C++, Haskell, Java, etc não vão deixar passar esse erro em tempo de compilação!

---
### Linguagens compiladas e interpretadas 

Outros erros mais sutis. 

```python
def soma(x,y):
    s = x+y

print(soma(3,2)) # Imprime None!
```

---
### Linguagens compiladas e interpretadas 

Outros erros mais sutis. 
```python
def soma(x,y):
    return str(x+y)
```

A função deveria retornar um número... não uma string!

---
## Tipos

Vamos utilizar "comentários" para informar os tipos das funções:

```python
def soma(x:int, y:int) -> int :
 s =  x + y

print(soma(3,2)) # None
```

O interpretador de Python simplesmente ignora as anotações de tipos

---
## Tipos

Mas mypy vai verificar se `soma` respeita as anotações dos tipos!

```
mypy soma.py

soma.py:8: error: Missing return statement
Found 1 error in 1 file (checked 1 source file)
```

Essa analise é feita em todas as funções (sem importar se elas foram chamadas no código ou não). 

---
## Tipos
```python
def imprimir(x:int, y:str) -> None:
 print(f'O número: {x}')
 print(f'A string: {y}')

imprimir(3, 5) #erro!!

x.py:20: error: Argument 2 to "imprimir" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```
  
---
### Como escrever código Python nesta disciplina?

1. Documentação
```python
def f():
  ''' Esta função implementa....
      parametro x: o valor de ...
      retorna .....
  '''
```

2. Tipos em *todas* as funções
```python
 def f(x:int) -> int:
```

3. Utilize Mypy em todos seus programas
---
## Jupyter Notebook

<a href="02-Python-Basico.ipynb">02-Python-Basico</a>
