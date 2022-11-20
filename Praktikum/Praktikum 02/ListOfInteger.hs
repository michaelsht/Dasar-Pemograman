module ListOfInteger where

-- Definisi dan Spesifikasi
elmtKeN :: [Int] -> Int -> Int 

-- Realisasi
elmtKeN l n = 
    if n == 1 then head l
    else elmtKeN (tail l) (n-1)

-- Aplikasi
-- elmtKeN [10] 1