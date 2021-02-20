-- Exemplos Funções, Casamento de Padrões
--

-- Determinar se um número é par

ehPar :: Int -> Bool
ehPar x = x `mod` 2 == 0

-- Podemos ser mais genéricos. A função pode trabalhar com Int e Integer

ehPar' :: (Integral a) =>  a -> Bool 
ehPar' x = x `mod` 2 == 0

-- Retornar a string "par" / "ímpar"

tipoInt :: (Integral a) => a -> String 
tipoInt x = if x `mod` 2 == 0 
            then "par"
            else "impar"


-- Utilizando Guardas

tipoInt' :: (Integral a) => a -> String
tipoInt' x
  | x `mod` 2 == 0   =  "par"
  | otherwise        =  "impar"


-- Notas de alunos
--

nota :: Float -> String
nota n
 | n >= 5      =  "aprovado"
 | n >=3       =  "repo"
 | otherwise   =  "reprovado"


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


-- Fatorial de um número
fatorial :: (Integral a) => a -> a
fatorial 0 =   1
fatorial n =   n * fatorial (n - 1)

-- Inverter a ordem dos elementos de uma tupla
inv :: (a , b) -> (b , a) 
inv (x, y) = (y , x)

-- Primeiro elemento
primeiro :: (a, b) -> a
primeiro (x,_) = x

-- Determinar se uma lista é vazia
ehVazia :: [a] -> Bool
ehVazia l =
  case l of
  [] -> True
  _:_ -> False


ehVazia' :: [a] -> Bool
ehVazia' [] = True
ehVazia' _  = False


ehVazia'' :: [a] -> Bool
ehVazia'' l
  | null l     = True
  | otherwise  = False


-- Função quadrática (número de soluções)

numSol :: Float -> Float -> Float -> Int
numSol a b c
 | b * b - 4 * a * c <   0   =    0
 | b * b - 4 * a * c ==  0   =    1
 | b * b - 4 * a * c >   0   =    2


numSol' :: Float -> Float -> Float -> Int
numSol' a b c
 | v  <   0   =    0
 | v  ==  0   =    1
 | v  >   0   =    2
 where 
   v = b * b - 4 * a * c 

-- Saudação (para um médico)

saudacao :: Char -> String -> String
saudacao sexo nome = (titulo sexo) ++ " " ++ nome
  where
    titulo :: Char -> String
    titulo 'F'  =  "Dra. "
    titulo 'M'  =  "Dr. "
    titulo _    =  "Dr(a). "
     
    
saudacao' :: Char -> String -> String
saudacao' sexo nome = (titulo sexo) ++ " " ++ nome
  where
    titulo :: Char -> String
    titulo c
      | c == 'F'  =  "Dra. "
      | c == 'M'  =  "Dr. "
      | otherwise =  "Dr(a). "
     

-- Implementação de Head
-- Erros
cabeca :: [a] -> a
cabeca (x:_) = x
cabeca [] = error "Cabeça não pode ser chamada com a lista vazia"

cabeca' :: [a] -> a
cabeca' l = 
  case l of
    [] -> error "Cabeça não pode ser chamada com a lista vazia"
    x:xs -> x

-- Avaliação Preguiçosa 

-- Lista infinita

repetir :: a -> [a]
repetir x = x : repetir x

-- Note que take 5 (repetir '*') 
-- funciona! 
-- Definição da função de Ackermann
ackermann :: Integer -> Integer -> Integer
ackermann 0 y = y + 1
ackermann x 0 = ackermann (x-1) 1
ackermann x y = ackermann (x-1) (ackermann x (y-1))

-- ackermann 4 4 (não vai terminar neste século)
-- l = [ackermann 1 1, ackermann 4 4 ]
-- é instantâneo (os elementos da lista não são calculados)
