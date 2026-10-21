import pytest

from demo_stop_daftar import rata_rata

def test_rata_rata_empat_angka():
    assert rata_rata([1, 2, 3, 4]) == 2.5

def test_rata_rata_satu_angka():
    assert rata_rata([10]) == 10.0

def test_rata_rata_positif_dan_negatif():
    assert rata_rata([-2, 2]) == 0.0

def test_rata_rata_angka_desimal():
    assert rata_rata([1.5, 2.5]) == 2.0

def test_daftar_kosong_melempar_value_error():
    with pytest.raises(ValueError, match="daftar tidak boleh kosong"):
        rata_rata([])

def test_bukan_list_melempar_type_error():
    with pytest.raises(TypeError, match="angka harus berupa list"):
        rata_rata("abc")
