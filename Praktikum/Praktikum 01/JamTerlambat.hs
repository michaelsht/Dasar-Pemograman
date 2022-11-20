module JamTerlambat where
    -- DEFINISI DAN SPESIFIKASI
    convert :: Int -> Int -> Int -> Int
    jamTerlambat :: Int -> Int -> Int -> (Int, Int, Int, Bool, Int)

    -- REALISASI
    convert h m d = (h*3600 + m*60 + d)
    jamTerlambat h m d =
        let jamMulaiToDetik = (convert 8 30 0)
            jamMasukToDetik = (convert h m d)
            selisihDetik = if jamMulaiToDetik < jamMasukToDetik then jamMasukToDetik - jamMulaiToDetik
            else jamMulaiToDetik - jamMasukToDetik
        in (div selisihDetik 3600,
            div (mod selisihDetik 3600) 60,
            mod (mod selisihDetik 3600) 60,
            jamMulaiToDetik < jamMasukToDetik,
            if jamMulaiToDetik < jamMasukToDetik then selisihDetik*10 else 0)