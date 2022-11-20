module LamaTidur where

-- SPESIFIKASI
hmstoSeconds :: Int -> Int -> Int -> Int
lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)

-- REALISASI
hmstoSeconds j m d = j * 3600 + m * 60 + d
lamaTidur j m d = 
    let 
        waktuTidur = 
            if j < 5 then (hmstoSeconds 5 0 0) - (hmstoSeconds j m d)
            else (hmstoSeconds 24 0 0) - (hmstoSeconds j m d) + (hmstoSeconds 5 0 0)
        jam = div waktuTidur 3600
        menit = div (waktuTidur - jam * 3600) 60
        detik = waktuTidur - hmstoSeconds jam menit 0
    in (waktuTidur >= 6 * 3600, jam, menit, detik)