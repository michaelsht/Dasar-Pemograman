module SeleksiKerja where
    -- SELEKSI KERJA
    -- DEFINISI DAN SPESIFIKASI
    seleksi :: Int -> Int -> Char -> Bool
    {- seleksi(m, s, p) -}
    {- mengecek apakah seseorang dapat masuk ke perusahaan 'p' dengan pengalaman managerial 'm' dan software engineer 's' yang ia punya -}
    -- REALISASI
    seleksi m s p
        | (p == 'A') = (m >= 2) && (s >= 4)
        | (p == 'B') = (s >= 4)
        | (p == 'C') = True
        | (p == 'D') = (m >= 2)