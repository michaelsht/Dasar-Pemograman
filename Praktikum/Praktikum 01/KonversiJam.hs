module KonversiJam where
-- Definisi dan Spesifikasi
konversiJam :: Int -> Int -> Int -> (Bool,Int,Int,Int)
-- Realisasi
konversiJam j m d = 
    if j>=7 
    then (False,j-7,m,d)
    else (True, 24-(7-j), m, d)
