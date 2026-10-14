import pytest

from calc import add, subtract, multiply, divide, power, modulo, square, cube

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

def test_square():
    assert square(4) == 16

def test_square_zero():
    assert square(0) == 0

def test_square_one():
    assert square(1) == 1

def test_square_negative():
    assert square(-3) == 9

def test_square_negative_fraction():
    assert square(-0.5) == 0.25

def test_square_fraction():
    assert square(2.5) == 6.25

def test_cube():
    assert cube(2) == 8

def test_cube_zero():
    assert cube(0) == 0

def test_cube_one():
    assert cube(1) == 1

def test_cube_negative():
    assert cube(-3) == -27

def test_cube_negative_fraction():
    assert cube(-0.5) == -0.125

def test_cube_fraction():
    assert cube(2.5) == 15.625
