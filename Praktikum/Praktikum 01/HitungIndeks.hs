module HitungIndeks where

-- DEFINISI DAN SPESIFIKASI
hitungIndeks :: Float -> Float -> Float -> Int
{- Menghitung indeks mahasiswa berdasarkan nilai UTS, nilai UAS, dan nilai Tubes -}

-- REALISASI
hitungIndeks uts uas tubes
  | (uts == 0) || (uas == 0) || (tubes == 0) = 0
  | (uts < 40) || (uas < 40) = 1 
  | (uts >= 75) && (uas >= 75) && (tubes >= 75) = 4
  | (tubes < 40) && (uas >= 40) && (uts >= 40) = 2
  | (uts < 75) && (uas < 75) && (tubes < 75) = 2
  | otherwise = 3

-- APLIKASI
-- hitungIndeks 100 100 0
