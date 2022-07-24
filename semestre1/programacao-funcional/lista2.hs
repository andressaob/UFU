{-
Nome: Andressa Oliveira Bernardes
Matrícula: 12121BSI201
-}
--exercicio 1a 
ordena2a :: Int -> Int -> (Int, Int)
ordena2a x y = if x<y then (x, y) else (y, x)

--exercicio 1b
ordena2b :: Int -> Int -> (Int, Int)
ordena2b x y
    | x<y = (x, y)
    | otherwise = (y, x)

--exercicio 2a
mesA :: Int -> String
mesA x
    | x == 1 = "Janeiro"
    | x == 2 = "Fevereiro"
    | x == 3 = "Março"
    | x == 4 = "Abril"
    | x == 5 = "Maio"
    | x == 6 = "Junho"
    | x == 7 = "Julho"
    | x == 8 = "Agosto"
    | x == 9 = "Setembro"
    | x == 10 = "Outubro"
    | x == 11 = "Novembro"
    | x == 12 = "Dezembro"
    | otherwise = "Erro!"

--exercicio 2b
mesB :: Int -> String
mesB x =
    case x of
        1 -> "Janeiro"
        2 -> "Fevereiro"
        3 -> "Março"
        4 -> "Abril"
        5 -> "Maio"
        6 -> "Junho"
        7 -> "Julho"
        8 -> "Agosto"
        9 -> "Setembro"
        10 -> "Outubro"
        11 -> "Novembro"
        12 -> "Dezembro"
        _ -> "Erro!"
{-
Sim, é possível utilizar if then else nesse caso, mas não é interessante pois ficaria muito longo e 
passível de confusão.
-}

--exercicio 3
triangulo :: Int -> Int -> Int -> String
triangulo x y z
    | existente = resultado
    | otherwise = "Nao existe um triangulo com essas medidas!"
    where
        existente = x>0 && y>0 && z>0 && x+y > z && x+z > y && y+z > x
        resultado
            | x==y && y==z = "Equilatero"
            | x==y || x==z || y==z = "Isosceles"
            | otherwise = "Escaleno"

--exercicio 4
maiorSoma :: Int -> Int -> Int
maiorSoma x y = let quadradoSoma = (x+y) ^ 2
                    somaQuadrado = (x^2) + (y^2)
                in if quadradoSoma > somaQuadrado then quadradoSoma else somaQuadrado

--exercicio 5
menu = do putStr "Nome: "
          nome <- getLine
          putStr "\nNúmero de Matrícula: "
          matricula <- getLine
          putStr "\nNota: "
          nota <- getLine
          putStrLn ("\nNome: " ++ nome ++ ", número de matrícula: " ++ matricula ++ " e nota: " ++ nota)