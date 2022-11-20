module ListIndex where

-- Definisi dan Spesifikasi
listIndex :: [Int] -> (Int -> Char) -> [Char]
skor :: Int -> Char 

-- Realisasi
listIndex li f =
    if null li then []
    else [f (head li)] ++ listIndex (tail li) (f)

skor x = 
    if (x >= 80) && (x <= 100) then 'A'
    else if (x >= 70) && (x < 80) then 'B'
    else if (x >= 65) && (x < 70) then 'C'
    else if (x >= 55) && (x < 65) then 'D'
    else 'E'