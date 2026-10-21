def jumlah_digit(n: int) -> int:
    """Mengembalikan banyaknya digit desimal dari nilai mutlak n."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n harus berupa int")
    return len(str(abs(n)))
