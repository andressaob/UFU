--Nome: Andressa Oliveira Bernardes
--Matrícula: 12121BSI201

import Data.Char

--exercicio 1a
numof :: Char -> String -> Int
numof caractere string = length (filter (== caractere) string)

--exercicio 1b
ellen :: [String] -> [Int]
ellen listaString = map length listaString

--exercicio 1c
ssp :: [Int] -> Int
ssp listaInt = foldr (+) 0 (filter even (map (^2) listaInt))

--exercicio 2
separa :: String -> (String, String)
separa string =  ((filter isAlpha string), (filter isDigit string))

{-
exercicio 3
a) const :: p1 -> p2 -> p1, retorna o primeiro número.
b) swap :: (b, a) -> (a, b), retorna uma tupla invertida.
c) apply :: (t1 -> t2) -> t1 -> t2, retorna os números na ordem em que foram escritos
d) flip :: (t1 -> t2 -> t3) -> t2 -> t1 -> t3, retorna o primeiro número e os dois últimos invertidos
-}

--exercicio 4a
type Nome = String
type Quantidade = Float
type PrecoUnitario = Float

data ShopItem = ShopItem Nome Quantidade PrecoUnitario


--exerecicio 4b
valorItem :: ShopItem -> Float
valorItem (ShopItem nome quant precoUnit) = quant * precoUnit

valorItens :: [ShopItem] -> Float
valorItens lsItens = foldr (+) 0 (map valorItem lsItens)

