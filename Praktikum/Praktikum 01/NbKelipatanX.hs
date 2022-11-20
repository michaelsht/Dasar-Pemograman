module NbKelipatanX where

-- DEFINISI DAN SPESIFIKASI
nbKelipatanX :: Int -> Int -> Int -> Int
--{Prekondisi: m <= n dan x <= n}
--{Menerima masukan m, n, x}
--{Mengeluarkan jumlah kelipatan x dalam rentang m sampai dengan n (inklusif)}

-- REALISASI
nbKelipatanX m n x
	|m == n && mod m x == 0 = 1
	|m == n && mod m x /= 0 = 0
	|m /= n && mod m x == 0 = 
	    1 + nbKelipatanX (m+1) n x
	|otherwise =
		nbKelipatanX (m+1) n x