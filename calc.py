import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol")
    return a % b

def square(a):
    return a * a

def average(a, b):
    """Mengembalikan rata-rata dari a dan b, yaitu (a + b) / 2."""
    return (a + b) / 2

def parse_number(teks):
    try:
        return int(teks)
    except (ValueError, TypeError):
        pass
    try:
        hasil = float(teks)
    except (ValueError, TypeError):
        raise ValueError("Bukan angka")
    if not math.isfinite(hasil):
        raise ValueError("Bukan angka")
    return hasil
