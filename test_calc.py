import pytest

from calc import add, subtract, multiply, divide, power, modulo, square
from calc import average
from calc import parse_number
from calc import percentage
from calc import negate

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

def test_average():
    assert average(2, 4) == 3

def test_average_same_numbers():
    assert average(5, 5) == 5

def test_average_fraction_result():
    assert average(1, 2) == 1.5

def test_average_negative_operand():
    assert average(-4, 2) == -1

def test_average_both_negative():
    assert average(-3, -5) == -4

def test_average_cancel_out():
    assert average(-2, 2) == 0

def test_average_zero():
    assert average(0, 0) == 0

def test_average_floats():
    assert average(2.5, 3.5) == 3.0

def test_parse_number_integer():
    assert parse_number("42") == 42
    assert isinstance(parse_number("42"), int)

def test_parse_number_decimal():
    assert parse_number("3.5") == 3.5
    assert isinstance(parse_number("3.5"), float)

def test_parse_number_negative_int():
    assert parse_number("-7") == -7

def test_parse_number_negative_decimal():
    assert parse_number("-2.5") == -2.5

def test_parse_number_invalid_text():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("abc")

def test_parse_number_partial_digits():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("12abc")

def test_parse_number_empty_string():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("")

def test_parse_number_non_string():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number(None)

def test_parse_number_nan():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("nan")

def test_parse_number_nan_uppercase():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("NaN")

def test_parse_number_inf():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("inf")

def test_parse_number_inf_uppercase():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("INF")

def test_parse_number_negative_inf():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("-inf")

def test_parse_number_infinity():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("infinity")

def test_parse_number_infinity_mixed_case():
    with pytest.raises(ValueError, match="Bukan angka"):
        parse_number("Infinity")

def test_percentage():
    assert percentage(25, 100) == 25.0

def test_percentage_decimal():
    assert percentage(1, 3) == pytest.approx(33.33333333333333)

def test_percentage_zero_part():
    assert percentage(0, 50) == 0.0

def test_percentage_negative_part():
    assert percentage(-10, 50) == -20.0

def test_percentage_zero_total():
    with pytest.raises(ValueError, match="Pembagian dengan nol"):
        percentage(10, 0)

def test_negate():
    assert negate(5) == -5

def test_negate_positive():
    assert negate(3) == -3

def test_negate_negative():
    assert negate(-7) == 7

def test_negate_zero():
    assert negate(0) == 0
