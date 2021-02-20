-- Exemplos de Funções recursivas
--

-- Fatorial 
fat :: (Integral a) => a -> a
fat 0    = 1
fat n    = n * fat (n - 1)

-- Utilizando guardas
fat' :: (Integral a) => a -> a
fat' n
 | n == 0      =  1
 | otherwise   =  n * fat' (n - 1)


-- Fibonacci
fib :: Int -> Int
fib 1    = 1
fib 2    = 1
fib n    = fib (n-1) + fib (n-2)

fib' :: Int -> Int
fib' n
 | n == 1  || n == 2    = 1
 | otherwise            = fib (n-1) + fib (n-2)


-- Algoritmo de Euclides para calcular o MDC
mdc :: (Integral a) => a -> a -> a
mdc x 0     =  x
mdc x y     = mdc y (x `mod` y)

-- Busca binaria
buscar :: (Ord a) => a -> [a]  -> Bool

buscar _ []    = False
buscar n l   
  | n == x      =  True
  | n < x       =  buscar n l1
  | otherwise   = buscar n l2
  where 
    mid  = div (length l) 2 -- Índice do meio 
    (l1, x:l2) = splitAt mid l -- Quebrar a lista em 2

-- Maior elemento
maior :: (Ord a) => [a] -> a 
maior []       = error "Maior não funciona com listas vazias!"
maior [x]      = x
maior (x:xs)   = max x (maior xs)

maior' :: (Ord a) => [a] -> a
maior' l = 
  case l of 
   []   -> error "Maior não funciona com listas vazias!"
   [x]  -> x
   x:xs -> max x (maior' xs)

-- Reverso
reverso :: [a] -> [a]
reverso []       =  []
reverso (x:xs)   =  reverso xs ++ [x]

--------------------
-- Recursão de cauda
--------------------
--

fatorial :: (Integral a) => a -> a
fatorial n  = fatrec n 1
  where fatrec :: (Integral a) => a -> a -> a
        fatrec 0 resultado    =  resultado
        fatrec n resultado    = fatrec (n-1) (resultado * n)

main  = print (fat 40000)


fibonacci :: (Integral a) => a -> a
fibonacci n   = fiborec n 1 1
  where fiborec :: (Integral a) => a -> a -> a -> a
        fiborec 1 _ ultimo      = ultimo
        fiborec 2 _ ultimo      = ultimo
        fiborec n pen ultimo    = fiborec (n-1) 
                                          ultimo (pen + ultimo)


rev :: [a] -> [a]
rev l = revrec l []
 where revrec :: [a] -> [a] -> [a]
       revrec [] res     =  res
       revrec (x:xs) res =  revrec xs (x:res)


-- Quicksort

quicksort :: (Ord a) => [a] -> [a]
quicksort []    =    []
quicksort (x:xs) = lmenores ++ [x] ++ lmaiores
   where lmenores = quicksort [i | i<- xs, i <= x ]
         lmaiores = quicksort [i | i<- xs, i >  x ]
      

-- Implementação de ZIP
--
meuzip :: [a] -> [b] -> [(a,b)]
meuzip [] _    =  []
meuzip _  []   =  []
meuzip (x:xs) (y:ys) = (x,y) : meuzip xs ys


-- De uma lista de tuplas a uma tupla de duas listas

meuunzip :: [(a,b)] -> ([a], [b])
meuunzip [] = ([], [])
meuunzip ((e1,e2):xs) = (e1:l1 , e2:l2)
  where
    (l1, l2) = unzip xs
  
