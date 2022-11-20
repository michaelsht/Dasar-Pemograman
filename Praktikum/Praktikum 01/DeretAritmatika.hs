module DeretAritmatika where
 
    -- DEFINISI DAN SPESIFIKASI
    deretAritmatika :: Int -> Int -> Int -> Float
    {- Menghitung jumlah n suku pertama dari deret 
     aritmatika dengan suku pertama a dan beda b-}
 
    -- REALISASI
    deretAritmatika n a b = fromIntegral((n * (2 * a + (n - 1) * b))) / fromIntegral(2)
 
-- Aplikasi
-- deretAritmatika 4 4 5