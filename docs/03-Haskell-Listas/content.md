## Haskell: Primeiros passos

--- 

### Objetivos

 - Terminal interativo de comandos `ghci`
 - Definição e uso de funções
 - Aplicação de funções
 - Currying 
 - Listas 

 ---

## A Linguagem Haskell

Haskell é uma linguagem funcional _pura_

__Sem variáveis, sem estruturas de controle, sem atribuição__

Lembre: _Paciência!_ Pensar funcionalmente é como começar a programar de zero

Hoje os primeiros conceitos: aplicação, abstração e currying 

---

## Terminal Iterativo

Depois de executar `ghci` podemos executar alguns comandos:

```
Prelude> 3 + 2
5
Prelude> print "alo"
"alo"
```
---
### Expressões artiméticas

Funcionam como esperado:
- `3 / 2` *não* é divisão inteira 
- Teste `3 / 0`
- Números negativos: `4 * (-1)` (_note os parênteses_)

```
Prelude> 6 * (-2)
-12
Prelude> 3 / 2
1.5
Prelude> 3 / 0
Infinity
```
---
### Expressões booleanas 
Também como esperado:

```
Prelude> True && False
False
Prelude> False || True
True
Prelude> not False
True
```

Note que não precisamos parênteses em `not False`!

---
## Tipos de expressões

O comando `:t` permite consultar os tipos das expressões

```
Prelude> :t True
True :: Bool
Prelude> :t not
not :: Bool -> Bool
```

Faz sentido! :
 - `True` é um expressão do tipo `Bool`
 - `not` é uma função que recebe um `Bool` e retorna um `Bool`

---
## Tipos de expressões

Lembra de `3 < 5 < 2`?: 
 - C++: `3 < 5 < 2 => 1 < 2 => true`
 - Python: a exp. é interpretada como `3<5 and 5<2`
 - Haskell.... vamos ver:

```haskell
Prelude> 3 < 5 < 2

< interactive >:20:1: error:
    Precedence parsing error

Prelude> 3 < 5 && 5 < 2
False
```

---
## Teste de igualdade

O teste `==` é como em quase toda linguagem (bom, o tipo deve implementar `==`... uma instância de `Eq`)

```haskell
Prelude> True == False
False
Prelude> 3 == 2
False
Prelude> "alo" == "alo"
True
Prelude> :t (==)
(==) :: Eq a => a -> a -> Bool
```

Note que não podemos comparar expressões de tipos diferentes:
```haskell
Prelude> 3 == "alo"

< interactive >:28:1: error:
```

---
## Notação prefixa e infixa

Já sabemos que `3 / 2 == 1.5`

Em Haskell, a função `div` calcula a divisão inteira

```haskell
Prelude> div 3 2
1
```

Por que não escrevemos `3 div 2`?

Notação infixa (note o crase)
```haskell
Prelude> 3 `div` 2
1
```

Notação prefixa
```haskell
Prelude> div 3 2
1
```
---

## Notação prefixa e infixa

O que acontece com `&&` e `||`?

Notação prefixa (note os parênteses)
```haskell
Prelude> :t (&&)
(&&) :: Bool -> Bool -> Bool
Prelude> (&&) True False
False
```

Notação infixa
```haskell
Prelude> True && False
False
```

---
## Algumas outras funções simples

```haskell
Prelude> :t min
min :: Ord a => a -> a -> a
```
Informalmente: min funciona com qualquer tipo que seja 'ordenável', ou seja, 
que pertença à __classe `Ord`__

Isso significa que o tipo `a` deve implementar coisas como `<`, `<=`, etc

Depois veremos como fazer isso. 

Inteiros e strings pertencem a essa classe:

```haskell
Prelude> min "mundo" "alo"
"alo"
Prelude> min 3 2
2
Prelude> max 5.5 3.4
5.5
```

---
## Definição de Funções
Vamos definir a primeira função:

```haskell
Prelude> soma x y = x + y
Prelude> :t soma
soma :: Num a => a -> a -> a
Prelude> soma 3.2 5.4
8.600000000000001
```
Haskell determinou que `x` e `y` devem ser números! (tipos que pertencem a essa classe)

---
## Definição de funções

- _Nome de funções e parâmetros sempre em minúscula_

Uma função constante (sem parâmetros)
```haskell
Prelude> cinco = 5
Prelude> cinco + 3
8
```
---
## Scripts

Copie o arquivo um.hs
```haskell
-- Meu primeiro programa em Haskell!

-- Definição da função que multiplica dois números inteiros
multiplicar :: Int -> Int -> Int
multiplicar a b = a * b

-- Dobro
dobro :: Int -> Int
dobro x = multiplicar 2 x

-- Depois veremos que é mais simples!
-- Utilizando o conceito de Currying
dobroV2 :: Int -> Int
dobroV2 = multiplicar 2
```
---

## Scripts

Carregue o arquivo no interpretador

```haskell
Prelude> :l um.hs
[1 of 1] Compiling Main             ( um.hs, interpreted )
Ok, one module loaded.
```

Podemos testar as funções:
```haskell
*Main> dobro 5
10
*Main> dobroV2 5
10
```
---
## Scripts

Tipicamente, modificaremos o script e precisamos carregar de novo:
```haskell
*Main> :r
Ok, one module loaded.
```
---
### Aplicação de Funções e Currying

- Lembre que ```multiplicar :: Int -> Int -> Int```

- Em Python: ```multiplicar(x:int, y:int) -> int```

- Em Python, precisamos de dois parâmetros: `multiplicar(3,2)`

- Em Haskell utilizamos a função assim: `multiplicar 3 2` (onde 3 é o primeiro parâmetro e 2 é o segundo)

---
### Aplicação de Funções e Currying

Mas em Haskell podemos definir a função `m3` como a seguir:
```haskell
m3 = multiplicar 3
```

O que significa isso? Porque o compilador não se quixa que falta um parâmetro?

---
### Aplicação de Funções e Currying
```haskell
m3 = multiplicar 3
:t m3
m3 :: Int -> Int
```

Ou seja: `m3` é uma função que espera um argumento (Int) para retornar um inteiro!

```
m3 4
12
```

_Currying_: Informar para uma função os parâmetros de forma parcial.

---
### Aplicação de Funções e Currying

De forma geral: 

Se `f :: a1 -> a2 -> ... -> an -> b`

Então `f x ::  a2 -> ... -> an -> b`

Outro exemplo:
```haskell
Prelude> :t (+)
(+) :: Num a => a -> a -> a
Prelude> inc = (+) 1
Prelude> inc' = (+1)
Prelude> inc 3
4
Prelude> inc' 5
6
```

---
## Listas

 Uma lista é uma estrutura de dados que armazena elementos de um mesmo tipo 
 de forma  sequencial.

```haskell
*Main> l = [1,2,3,4,5]
```

Podemos concatenar 2 listas com `++`

```haskell
*Main> *Main> l++[6,7]
[1,2,3,4,5,6,7]
```

Segue o tipo de `l`:
```haskell
*Main> :t l
l :: Num a => [a]
```

---
## Listas
De fato, as strings em Haskell são listas de Char!
```haskell
*Main> :t "alo"
"alo" :: [Char]
*Main> "alo " ++ "mundo"
"alo mundo"
```


---
## Listas

Aproveitando o exemplo... Currying de novo:

```haskell
Prelude> exclamar    = (++ "!")
Prelude> exclamar' s = s ++ "!"
Prelude> :t exclamar
exclamar :: [Char] -> [Char]
Prelude> :t exclamar'
exclamar' :: [Char] -> [Char]
Prelude> exclamar "alo"
"alo!"
Prelude> exclamar' "alo"
"alo!"
```
---
## Listas
A lista mais simples que podemos considerar é a lista vazia:
```haskell
*Main> lvazia = []
*Main> lvazia ++ [1]
[1]
```

---
## Listas

Se `l` é uma lista, `x:l` é a lista que resulta de adiciona `x` no começo de `l`.

Esse operador normalmente é conhecido como __`cons`__:

```haskell
*Main> l1 = [2,3,4]
*Main> 1:l1
[1,2,3,4]
```

De fato, podemos ver uma lista como uma aplicação sucessiva de `cons`:
```
*Main> [1,2,3] == 1:2:3:[]
True
```
---
## Listas
As listas são tão úteis que existem atalhos para construí-las. 

```haskell
*Main> [1,3 .. 13]
[1,3,5,7,9,11,13]
*Main> ['a' .. 'z']
"abcdefghijklmnopqrstuvwxyz"
*Main> [100,80 .. 0]
[100,80,60,40,20,0]
*Main>
```
Lembra do `range` em Python? Esse aqui é mais poderoso ;-)

---
## Listas

As listas podem ser aninhadas. Por exemplo:

```haskell
*Main> lan = [ [1,2],[3,4],[],[5,7]]
*Main> :t lan
lan :: Num a => [[a]]
```

Nota: Se `a` é um tipo, `[a]` denota uma lista de elemento tipo `a`
- `[Int]` é o tipo das listas de inteiros
- `[[Int]]` é o tipo das listas de listas de inteiros
---
## Operação utilizando Listas

Acessar um elemento utilizando índices:
```haskell
*Main> [1,2,3] !! 2
3
```

Determinar se a lista está vazia
```haskell
*Main> null [1,2,3]
False
*Main> null []
True
```

Tamanho da lista
```haskell
*Main> length "mundo"
5
```

---
## Operação utilizando Listas
Retornar o primeiro elemento (de uma lista _não vazia_)
```haskell
*Main> head "alo"
'a'
```

Retornar a lista sem o primeiro elemento (de uma lista _não vazia_)
```haskell
*Main> tail [1,2,3]
[2,3]
*Main> tail [1]
[]
*Main> tail []
*** Exception: Prelude.tail: empty list
```

---
## Operação utilizando Listas

Último elemento e a lista sem o último elemento:
```haskell
*Main> last [1,2,3]
3
*Main> init [1,2,3]
[1,2]
```

---
## Operação utilizando Listas

Retornar os n primeiros elementos da lista
```haskell
*Main> take 0 [1,2,3,4]
[]
*Main> take 2 [1,2,3,4]
[1,2]
*Main> take 20 [1,2,3,4]
[1,2,3,4]
```
---
## Operação utilizando Listas

Descartar os n primeiros elementos
```haskell
*Main> drop 0 [1,2,3,4]
[1,2,3,4]
*Main> drop 2 [1,2,3,4]
[3,4]
*Main> drop 20 [1,2,3,4]
[]
```
---
## Operação utilizando Listas

Lista em ordem reversa:
```
*Main> reverse [1,2,3,4]
[4,3,2,1]
```

Verificar se um elemento pertence à lista
```haskell
*Main> 3 `elem` [1,2,3,4]
True
*Main> elem 5 [1,2,3,4]
False
```

---
## Tipos em listas

Lembre: as listas são tão importantes que existe uma notação especial para 
os tipos das listas

`[a]` é o tipo das listas cujos elementos são do tipo `a`

```haskell
*Main> :t "mundo"
"mundo" :: [Char]
*Main> :t ['a','l','o']
['a','l','o'] :: [Char]
*Main> :t [1,2,3]
[1,2,3] :: Num a => [a]
``` 
---
## Operação utilizando Listas
- Concatenar: `l1 ++ l2`
- Cons: `a:l`
- Acessar índice: `l !! 3`
- É vazia? `null l`
- Número de elementos: `length l`
- Primeiro elemento: `head l`
- Remover primeiro elemento: `tail l`
- Último elemento: `last l`
- Remover o último elemento: `init l`
- `n` primeiros elementos: `take n l`
- Descartar `n` primeiros elementos: `drop n l`
- Ordem reversa: `reverse l`
- `e` está em `l`: `elem e l`

---
## Exercício No 1
Utilizando as funções de listas, escreva funções para:
- Determinar se uma string é um palíndromo
```
ehPalindromo :: [Char] -> Bool
```

- Determinar se o primeiro e último elemento de uma lista de inteiros são iguais
```
primUltimoIgual :: [Int] -> Bool
```

---
## Para casa

- Determinar se o primeiro caractere de uma string ocorre mais de uma vez
```
"alo" --> False     "ana" --> True
```

- Determinar se os `n` primeiros elementos de uma lista de inteiros 
são iguais aos últimos `n` elementos. Dica: você pode comparar listas
de inteiros com `==`

```
iguaisIniFim 3 [1,2,3,4,5,6,1,2,3] --> True
```
- Determinar se um caractere representa uma letra maiúscula 

---
## Tuplas

Utilizadas para guardar vários valores agrupados

Os tipos dos elementos não precisam ser os mesmos

```haskell
Prelude> x = (3, "alo")
Prelude> :t x
x :: Num a => (a, [Char])
Prelude> t1 = (["alo", "mundo"], 3)
Prelude> :t t1
t1 :: Num b => ([[Char]], b)
```
---
## Tuplas
Podemos utilizar tuplas para representar pontos no plano cartesiano

```haskell
-- Exemplo utilizando tuplas

-- Ponto (simplesmente um alias)  é uma tupla com 2 floats
type Ponto = (Float, Float)

-- Origem no plano cartesiano
-- Note que isto é uma função constante
origem :: Ponto
origem = (0.0, 0.0)

-- Mover em X. O primeiro parâmetro é um ponto
-- Note a forma de utilizar o parâmetro (pattern matching)
moverX :: Ponto -> Float -> Ponto
moverX (x1,y1) x = (x1 + x, y1)

-- Mover em Y
moverY :: Ponto -> Float -> Ponto
moverY (x1,y1) y = (x1 , y1 + y)

p1 = moverY ( moverX origem 5) 3
```
---
## Exercício No 2
Implemente uma função para retornar a coordenada x de um ponto

Implemente uma função para retornar a coordenada y de um ponto

Reimplemente moverX sem utilizar pattern matching

```haskell
moverX' :: Ponto -> Float -> Float
moverX' p f = ???
```
---
## Para casa No 2
Implemente uma função para retornar um ponto espelhado no eixo X (ex. (3,2) --> (-3,2))

Implemente uma função para retornar um ponto espelhado no eixo Y (ex. (3,2) --> (3,-2))
