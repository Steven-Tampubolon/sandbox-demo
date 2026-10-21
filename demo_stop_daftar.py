def rata_rata(angka: list) -> float:
    """Mengembalikan rata-rata aritmetika elemen angka sebagai float."""
    if not isinstance(angka, list):
        raise TypeError("angka harus berupa list")
    if len(angka) == 0:
        raise ValueError("daftar tidak boleh kosong")
    return sum(angka) / len(angka)
