module SumOfDigits where

-- DEFINISI DAN SPESIFIKASI
sumOfDigits :: Int -> Int
{- 
sumOfDigits(n)
Menerima masukkan n
Mengeluarkan jumlah setiap digit pada n
-}

-- REALISASI
sumOfDigits n
    | n == 0 = 0                                    -- Basis
    | otherwise = mod n 10 + sumOfDigits(div n 10)  -- Rekurens