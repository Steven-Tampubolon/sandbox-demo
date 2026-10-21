import pytest

from demo_stop_angka import jumlah_digit

def test_nol_punya_satu_digit():
    assert jumlah_digit(0) == 1

def test_digit_tunggal():
    assert jumlah_digit(7) == 1

def test_lima_digit():
    assert jumlah_digit(12345) == 5

def test_nilai_negatif_diabaikan_tanda_minya():
    assert jumlah_digit(-907) == 3

def test_sejuta_punya_tujuh_digit():
    assert jumlah_digit(1000000) == 7

def test_float_melempar_type_error():
    with pytest.raises(TypeError, match="n harus berupa int"):
        jumlah_digit(3.5)

def test_bool_melempar_type_error():
    with pytest.raises(TypeError, match="n harus berupa int"):
        jumlah_digit(True)
