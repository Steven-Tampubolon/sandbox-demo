# sandbox-demo

Kalkulator sederhana berbasis Python (lihat `calc.py`).

## Fungsi

- `add(a, b)` — mengembalikan jumlah `a + b`.
- `subtract(a, b)` — mengembalikan selisih `a - b`.
- `multiply(a, b)` — mengembalikan perkalian `a * b`.
- `divide(a, b)` — mengembalikan hasil pembagian `a / b`. Melempar `ValueError` dengan pesan "Pembagian dengan nol" jika `b` bernilai 0.
- `power(a, b)` — mengembalikan hasil `a` pangkat `b`.
- `modulo(a, b)` — mengembalikan sisa bagi `a % b`. Melempar `ValueError` dengan pesan "Pembagian dengan nol" jika `b` bernilai 0.
- `square(a)` — mengembalikan hasil `a` dikali `a`.
- `average(a, b)` — mengembalikan rata-rata dari `a` dan `b`, dihitung sebagai `(a + b) / 2`. Menerima bilangan bulat maupun pecahan (float), dan hasilnya selalu bertipe float; operan negatif pun didukung (misal `average(-4, 2)` menghasilkan `-1.0`).
- `parse_number(teks)` — mengubah teks menjadi angka: teks bulat menjadi `int` (misal `"42"` → `42`), teks desimal menjadi `float` (misal `"3.5"` → `3.5`); angka negatif didukung (misal `"-7"` → `-7`). Teks yang tidak merepresentasikan angka (termasuk string kosong dan input non-string) melempar `ValueError` dengan pesan "Bukan angka".

## Menjalankan tes

```bash
python -m pytest -q
```
