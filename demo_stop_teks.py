def hitung_kata(teks: str) -> int:
    """Menghitung jumlah kata dalam teks yang dipisahkan spasi, tab, atau baris baru."""
    if not isinstance(teks, str):
        raise TypeError("teks harus berupa str")
    return len(teks.split())
