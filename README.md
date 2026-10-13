# sandbox-demo

Kalkulator sederhana berbasis Python (lihat `calc.py`).

## Fungsi

- `add(a, b)` — mengembalikan jumlah `a + b`.
- `subtract(a, b)` — mengembalikan selisih `a - b`.
- `multiply(a, b)` — mengembalikan perkalian `a * b`.
- `divide(a, b)` — mengembalikan hasil pembagian `a / b`. Melempar `ValueError` dengan pesan "Pembagian dengan nol" jika `b` bernilai 0.

## Menjalankan tes

```bash
python -m pytest -q
```
