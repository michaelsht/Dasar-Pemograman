-- module Kinerja where
 
-- Penilaian Kinerja Karyawan 
                    
-- DEFINISI DAN SPESIFIKASI
   kinerja :: Int -> Int -> Int -> (Int, Int, Int, Int)
-- Fungsi menerima jam selesai pekerjaan karyawan dan mengembalikan berapa lama selisih waktu selesai pekerjaan dengan standar jam kerja dan menentukan apakah karyawan selesai tepat waktu/terlambat/lebih awal.

-- REALISASI
   kinerja j m d =
       let
           selisih_detik = (17*3600 + 30*60) - (j*3600 + m*60 + d)
       in
           (div (abs(selisih_detik)) 3600,
           div (mod (abs(selisih_detik)) 3600) 60,
           mod (mod (abs(selisih_detik)) 3600) 60,
           if (selisih_detik < 0) then -1
           else if (selisih_detik > 0) then 1
           else 0)

-- APLIKASI
-- kinerja 18 30 5
