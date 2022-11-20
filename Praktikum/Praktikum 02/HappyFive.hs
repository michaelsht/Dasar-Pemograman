module HappyFive where

-- HAPPY FIVE

-- DEFINISI DAN SPESIFIKASI
happyFive :: [Int] -> [Int]
    -- happyFive menerima sebuah list of integer
    -- lalu memilih angka-angka yang merupakan
    -- kelipatan 5

kelipatanLima :: Int -> Bool 
    -- kelipatanLima mengecek apakah elemen dari list
    -- merupakan kelipatan 5 atau bukan

-- Untuk mengecek list kosong
isEmpty :: [Int] -> Bool
isEmpty l = null l

-- Untuk konso
konso :: Int -> [Int] -> [Int]
konso e l = [e] ++ l

-- Realisasi
kelipatanLima n =
    if mod n 10 == 5 then True
    else if div n 10 == 5 then True
    else False 

happyFive a =
    if isEmpty a then []
    else 
        if mod (head a) 5 == 0 || kelipatanLima (head a) then konso (head a) (happyFive (tail a))
        else happyFive (tail a)