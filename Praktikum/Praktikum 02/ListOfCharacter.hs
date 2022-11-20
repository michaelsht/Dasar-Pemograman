module ListOfCharacter where

konso :: Char -> [Char] -> [Char]
{- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
   dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
-- REALISASI
konso e lc = [e] ++ lc

inverse :: [Char] -> [Char]

inverse l = 
    if isEmpty l then []
    else konso (last l) (inverse (init l))