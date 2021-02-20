## Haskell: Tipos e Funções

--- 
## A Linguagem Haskell

Haskell é uma linguagem funcional _pura_

__Sem variáveis, sem estruturas de controle, sem atribuição__

Lembre: _Paciência!_ Pensar funcionalmente é como começar a programar de zero

Hoje: definiremos funções mais interessantes utilizando guardas e pattern-matching. 

---
## Na última aula ...
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
 - `True` é um _expressão_ do tipo `Bool`
 - `not` é uma __função__ que recebe um `Bool` e retorna um `Bool`

---
## Notação prefixa e infixa

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
## Definição de Funções
Uma função muito simples:

```haskell
Prelude> soma x y = x + y
Prelude> :t soma
soma :: Num a => a -> a -> a
Prelude> soma 3.2 5.4
8.600000000000001
```
Haskell determinou que `x` e `y` devem ser _números_! (tipos que pertencem a essa classe)
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
### Aplicação de Funções e Currying

- Lembre que ```multiplicar :: Int -> Int -> Int```

- Em Python: ```multiplicar(x:int, y:int) -> int```

- Em Python, precisamos de dois parâmetros: `multiplicar(3,2)`

- Em Haskell utilizamos a função assim: `multiplicar 3 2` 

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
### Funções Curried 

> Toda função em Haskell oficialmente recebe apenas um parâmetro

```haskell
Prelude> func a b c x = a * x * x + b * x + c 
Prelude> :t func
func :: Num a => a -> a -> a -> a -> a
Prelude> :t func 1
func 1 :: Num a => a -> a -> a -> a
Prelude> :t func 1 2
func 1 2 :: Num a => a -> a -> a
Prelude> :t func 1 2 3
func 1 2 3 :: Num a => a -> a
Prelude> :t func 1 2 3 4
func 1 2 3 4 :: Num a => a
```
---
## Listas

Se `l` é uma lista, `x:l` é a lista que resulta de adicionar `x` no começo de `l`.

Esse operador normalmente é conhecido como __`cons`__:

```haskell
*Main> l1 = [2,3,4]
*Main> 1:l1
[1,2,3,4]
```

---
## Tipos em listas

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
## "Ranges"

```haskell
Prelude> [1,3 .. 13]
[1,3,5,7,9,11,13]
```

Com isso, podemos testar facilmente se um caractere é uma letra minúscula: 
```haskell
ehLetraMin :: Char -> Bool 
ehLetraMin x = x `elem` ['a' .. 'z']
```
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

## A aula de hoje...

Na última aula utilizamos as funções da biblioteca padrão para implementar outras funções. 

De fato, isso é fundamental no paradigma funcional: 

>> Making basic functions that are _obviously correct_ and then __combining__ them into more complex functions

Hoje: implementaremos funções mais interessantes e conheceremos  melhor os tipos básicos. 

Extra: _Preguiça!_ Sim, é boa ;-)

---
### Objetivos

 - Definir funções utilizando pattern-matching
 - Definir funções utilizando guardas
 - Entender o conceito de computação preguiçosa 

---
### Tipos

Já sabemos que Haskell pode inferir alguns tipos:
```haskell
Prelude> s = "alo"
Prelude> :t s
s :: [Char]
Prelude> tupla1 = (3, "alo")
Prelude> :t tupla1
tupla1 :: Num a => (a, [Char])
```
---

### Tipos Numéricos 
Os tipos numéricos pertencem à classe `Num` (_class type_):

```haskell
Prelude> soma x y = x + y
Prelude> :t soma
soma :: Num a => a -> a -> a
```
Alguns tipos que pertencem à classe `Num`:

_`Int`_: números inteiros (limitados, como em C++)

_`Integer`_: números inteiros (sem limite)

A classe _`Integral`_ inclui os dois tipos de inteiros
---
### Tipos Numéricos
_`Int`_: números inteiros (limitados, como em C++)

_`Integer`_: números inteiros (sem limite)

```haskell
Prelude> x = 4
Prelude> :t x
x :: Num p => p
Prelude> y = 4 :: Int
Prelude> :t y
y :: Int
Prelude> z = 100000000000000000000000 :: Int
warning: [-Woverflowed-literals]
Prelude> z
200376420520689664
Prelude> w = 100000000000000000000000 :: Integer
Prelude> :t w
w :: Integer
```
---
### Tipos Numéricos

_`Float`_: Números de ponto flutuante (precisão simples)

_`Double`_: Números de ponto flutuante (precisão dupla)

A classe _`Fractional`_ inclui esses dois tipos. 

A classe _`Num`_ inclui *`Fractional` e `Integral`*

---
### Tipos Numéricos

```haskell
Prelude> soma x y = x + y
Prelude> :t soma
soma :: Num a => a -> a -> a
```

> Significa que `soma` é uma função do tipo `a -> a -> a ` para qualquer `a` que pertença à classe `Num`!

---
### Type Classes

- "classe" não significa o mesmo que em POO
- _TypeClass_: parece mais uma _interface_ em Java
- Uma TypeClass é como uma __interface__ que define um __comportamento__
- Se o tipo `a` _pertence à classe `C`_ (notação `(C a) `), `a` deve __implementar__ o comportamento de `C`
- A classe é uma forma de __classificar tipos__ quanto às funcionalidades a ele associadas.

---
### TypeClass Eq e Ord

À classe `Eq` pertencem os tipos cujos objetos podemos testar por igualdade. 

```haskell
Prelude> comparar x y = x == y
Prelude> :t comparar
comparar :: Eq a => a -> a -> Bool
```

Haskell determina que `x` e `y` devem ser de um tipo `a` que __implementa__ o operador `==` (e `/=`)

A classe `Ord` define tipos cujos elementos podem ser ordenados. Ou seja, o tipo deve implementar 
as relações  `<`, `<=`, etc.

---

## Guardas e Casamento de Padrões

---

## É par?
Vamos implementar uma função para determinar se um número é par ou não

_Tipo_: `ehPar :: Int -> Bool`

Se queremos ser mais genéricos:

_Tipo_: `ehPar' :: (Integral a) => a -> Bool`

---
## É par?

A implementação é simples:
```haskell
ehPar :: Int -> Bool
ehPar x = x `mod` 2 == 0

-- Mais geral
ehPar' :: (Integral a) =>  a -> Bool
ehPar' x = x `mod` 2 == 0
```

Tente `ehPar 2222222222222222222222222`... 

funciona com `ehPar'`?

---
## É par ... ou ímpar?

Agora uma função que, dado um número, retorna uma string: "par" / "ímpar"

Parece que precisamos de uma estrutura condicional... mas elas __não existem__....

Lembra do _operador ternário_ em C++?

```cpp
x = c ? valorTrue : valorFalse ;
```

Em Haskell:
```haskell
if C then valorTrue else valorFalse
```
---
## É par ... ou ímpar?

```haskell
tipoInt :: (Integral a) => a -> String
tipoInt x = if x `mod` 2 == 0
            then "par"
            else "impar"
```
---
## É par ... ou ímpar?
#### Guardas

Existe uma forma mais simples de escrever esse programa 

```haskell
tipoInt' :: (Integral a) => a -> String
tipoInt' x
  | x `mod` 2 == 0   =  "par"
  | otherwise        =  "impar"
```

>> `otherwise == True`
---
## Dias da semana

Vamos implementar uma função que, dado um número, retorna uma string com  o dia da semana
 - 1 -> Domingo
 - 2 -> Segunda, etc

> `if c then S1 else S2` não parece  uma boa alternativa
---
## Dias da semana

Podemos utilizar guardas!

```haskell
dia n
 | n == 1    =  "domingo"
 | n == 2    =  "segunda"
 | ...

```
Mas existe uma melhor alternativa!

---
## Dias da semana

```haskell
-- Dias da semana
dia :: Int -> String
dia 1   =  "domingo"
dia 2   =  "segunda"
dia 3   =  "terca"
dia 4   =  "quarta"
dia 5   =  "quinta"
dia 6   =  "sexta"
dia 7   =  "sabado"
dia x   =  "dia nao valido"
```
> As opções são avaliadas da primeira à última. Por isso, `x` casa qualquer 
opção. 
---
## Dias da semana

A mesma técnica trabalha com funções recursivas!

```haskell
-- Fatorial de um número
fatorial :: (Integral a) => a -> a
fatorial 0 =   1
fatorial n =   n * fatorial (n - 1)
```

---
## Exemplos com tuplas

A função a seguir inverte a ordem de uma tupla
```haskell
inv :: (a , b) -> (b , a)
inv (x, y) = (y , x)
```

E a função que retorna o primeiro elemento de uma tupla
```haskell
primeiro :: (a, b) -> a
primeiro (x,_) = x
```
Sublinhado: qualquer valor

---
## Exemplos com listas

Mais uma forma de definir funções: 
```haskell
ehVazia :: [a] -> Bool
ehVazia l =
  case l of
  [] -> True
  _:_ -> False
```
Lembre, o sublinhado casa qualquer valor

---
## Exemplos com listas

```haskell
ehVazia' :: [a] -> Bool
ehVazia' [] = True
ehVazia' _  = False

ehVazia'' :: [a] -> Bool
ehVazia'' l
  | null l     = True
  | otherwise  = False
```

---
## Expressões Where

Considere uma função que retorna o número de raizes de uma função quadrática

```haskell
numSol :: Float -> Float -> Float -> Int
numSol a b c
 | b * b - 4 * a * c <   0   =    0
 | b * b - 4 * a * c ==  0   =    1
 | b * b - 4 * a * c >   0   =    2
```

Um pouco feio... né?

---
## Expressões Where

Considere uma função que retorna o número de raizes de uma função quadrática
```haskell
numSol' :: Float -> Float -> Float -> Int
numSol' a b c
 | v  <   0   =    0
 | v  ==  0   =    1
 | v  >   0   =    2
 where
   v = b * b - 4 * a * c
```

`where`: expressões auxiliares

> `v` é visível só dentro da função `numSol'`

---
## Expressões Where
```haskell
saudacao :: Char -> String -> String
saudacao sexo nome = (titulo sexo) ++ " " ++ nome
  where
    titulo :: Char -> String
    titulo 'F'  =  "Dra. "
    titulo 'M'  =  "Dr. "
    titulo _    =  "Dr(a). "
```

Aqui utilizamos o `where` para definir a função (auxiliar) `titulo`

---
## Expressões Where
```haskell
saudacao' :: Char -> String -> String
saudacao' sexo nome = (titulo sexo) ++ " " ++ nome
  where
    titulo :: Char -> String
    titulo c
      | c == 'F'  =  "Dra. "
      | c == 'M'  =  "Dr. "
      | otherwise =  "Dr(a). "
```

---
## Erros

Sabemos que a função `head` só trabalha com listas não vazias.

Podemos implementar essa função assim:

```haskell
cabeca :: [a] -> a
cabeca (x:_) = x
cabeca [] = error "Cabeça não pode ser chamada com a lista vazia"

```

Também: 
```haskell
cabeca' :: [a] -> a
cabeca' l =
  case l of
    [] -> error "Cabeça não pode ser chamada com a lista vazia"
    x:xs -> x
```
---
## Exercícios

Considere o alias: 
```haskell
type Ponto = (Float, Float)
```

1. Defina uma função para calcular a distância entre dois pontos. A função
   `sqrt` calcula a raiz quadrada. Tente utilizar `where` na sua definição.

2. Dada a nota de um aluno, retorne o status do aluno:  "aprovado", "reprovado", "reposição" 

---
## Para Casa

1. Para representar um retângulo usamos as coordenadas cartesianas do seu canto
   inferior esquerdo e o valor da sua largura e da sua altura. Implemente um
   função que determine se um ponto P está ou não
   dentro de um retângulo. 

2. Faça uma função que, dadas duas datas D1 e D2 representadas como uma tupla `(dia, mes, ano)`, retorne:
 - 0 se as duas datas são iguais
 - (-1) se D1 é mais antiga
 - 1 caso contrário. 

3. Faça uma função que determine o número de elementos de uma lista (sem utilizar _length_) 

---
## Avaliação preguiçosa

O que faz a função a seguir?

```haskell
repetir :: a -> [a]
repetir x = x : repetir x
```

---
## Avaliação preguiçosa

O que faz a função a seguir?

```haskell
repetir :: a -> [a]
repetir x = x : repetir x
```

Será que isto gera um loop infinito?
```haskell
l = repetir '*'
```
---
## Avaliação preguiçosa

Será que isto gera um loop infinito?
```haskell
l = repetir '*'
```
>> __Não!__ Graças à _avaliação preguiçosa_  de Haskell, como `l` não foi (ainda) utilizada, `repetir` não é executada!

---
## Avaliação preguiçosa
```haskell
*Main> l = repetir '*'
*Main> take 3 l
"***"
*Main> head l
'*'
```
Note que podemos fazer tail:
```haskell
*Main> ltail = tail l
*Main>
```
Mas não podemos "imprimir" ltail (ou l) porque teremos um loop infinito. 

---
## Avaliação preguiçosa
Um exemplo mais interessante. 

```haskell
ackermann :: Integer -> Integer -> Integer
ackermann 0 y = y + 1
ackermann x 0 = ackermann (x-1) 1
ackermann x y = ackermann (x-1) (ackermann x (y-1))
```
Veja [Função de Ackermann](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_de_Ackermann)

---
## Avaliação preguiçosa

```haskell
*Main> la = [ackermann 1 1 , ackermann 4 4]
```
`ackermann 4 4` é um número enorme! Mas Haskell não precisa calculá-lo (por enquanto). 

---
## Avaliação preguiçosa
> Técnica de programação para atrasar a computação até um ponto em que o resultado é (realmente) necessário. 

Na maioria de linguagens, a estratégia de avaliação é _gulosa_: os parâmetros sempre são avaliados antes de executar a função. 
