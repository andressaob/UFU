--Nome: Andressa Oliveira Bernardes
--Matrícula: 12121BSI201

--exercicio 1
imprimeNVezes :: Int -> IO ()
imprimeNVezes n    
    | n == 1 = putStrLn "Frase"
    | n > 1 = do putStrLn "Frase"
                 imprimeNVezes (n -1)
    | otherwise = putStrLn "ERRO!"

--exercicio 2
eLogico :: Bool -> Bool -> Bool
eLogico a b 
    | (a == True && b == True) = True
    | otherwise = False

--exercicio 3
eLogico2 :: Bool -> Bool -> Bool
eLogico2 a b
    | a == True = b
    | a == False = False

--exercicio 4
comb :: (Int, Int) -> Int
comb (n, k)
    | k == 1 = n
    | k == n = 1
    | (1 < k && k < n) = comb(n-1, k-1) + comb(n-1, k)