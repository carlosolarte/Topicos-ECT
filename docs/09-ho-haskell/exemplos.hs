-- Funções de ordem superior
--

-- As funções recebem só um parâmetro
soma :: Int -> Int -> Int 
soma x y = x + y

inc' :: Int -> Int
inc' x  = soma 1 x

-- "soma 1" é uma função que ainda espera por um parâmetro
inc :: Int -> Int 
inc = soma 1

-- Seções

ehZero :: Int -> Bool
ehZero = (==0)

ehZero' :: Int -> Bool
ehZero' x = x == 0

mod2 :: Int -> Int
mod2 = (`mod`2)

ehPar :: Int -> Bool
ehPar x  = ehZero (mod2 x) 

ehMaiuscula :: Char -> Bool
ehMaiuscula = (`elem` ['A'..'Z'])

--- Funções de ordem superior
--

aplicar2 :: ( a -> a) -> a -> a
--- aplicar2 recebe :
---  - uma função f do tipo a -> a
--   - um valor n do tipo a
--   -- retorna f( f a)

aplicar2 f x = f( f x)

-- Por exemplo, plus2 pode ser definida como aplicar duas vezes a função inc
plus2 :: Int -> Int
plus2 = aplicar2 inc 

plus2' :: Int -> Int
plus2' x = aplicar2 inc x


-- Currying

meucurry :: ( (a,b) -> c) -> a -> b -> c
meucurry f x y = f (x,y)
meuuncurry :: ( a -> b -> c) -> (a, b) -> c
meuuncurry f (x, y) = f x y 



--- versão de multiplicação que recebe um par ordenado
multpar :: (Int , Int) -> Int
multpar (x,y) = x * y 

mult :: Int -> Int -> Int 
mult x y  = x * y 

--- Podemos converter multpar em mult e vice-versa 
multpar' :: (Int, Int) -> Int
multpar' = meuuncurry mult
mult'    :: Int -> Int -> Int
mult'    = meucurry multpar


--- Exemplo de Quicksort utilizado filter
--
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    menor ++ [x] ++ maior
    where
        menor = quicksort (filter (<=x) xs)
        maior = quicksort (filter (>x) xs)


--- Determinar se um número é primo
ehPrimo :: Int -> Bool
ehPrimo n
 | n < 2     = False
 | otherwise = [n] == [x | x <- [2..n], n `mod` x == 0]


seqPrimos :: [Int] 
seqPrimos = filter ehPrimo [1..]

primoIntervalo :: Int -> Int -> [Int]
primoIntervalo x y = filter ehPrimo [x..y]

primoMenor30000 :: Int
primoMenor30000 = head (filter ehPrimo [30000,29999 .. ])

quantosPrimos :: [Int] -> Int
quantosPrimos l = length (filter ehPrimo l)

primosMenores :: Int -> [Int]
primosMenores n = takeWhile (<= n) seqPrimos 

