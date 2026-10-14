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

## Menjalankan tes

```bash
python -m pytest -q
```
