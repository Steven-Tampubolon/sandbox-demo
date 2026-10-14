import pytest

from calc import add, subtract, multiply, divide, power, modulo

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_fraction():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Pembagian dengan nol"):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_zero_base():
    assert power(0, 3) == 0

def test_power_negative_exponent():
    assert power(2, -2) == 0.25

def test_power_one():
    assert power(7, 1) == 7

def test_modulo():
    assert modulo(10, 3) == 1

def test_modulo_exact_division():
    assert modulo(9, 3) == 0

def test_modulo_larger_divisor():
    assert modulo(3, 10) == 3

def test_modulo_negative_dividend():
    assert modulo(-7, 3) == 2

def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Pembagian dengan nol"):
        modulo(10, 0)
