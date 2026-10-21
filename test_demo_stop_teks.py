import pytest

from demo_stop_teks import hitung_kata

def test_dua_kata_biasa():
    assert hitung_kata("halo dunia") == 2

def test_spasi_berulang_di_awal_akhir_dan_antar_kata():
    assert hitung_kata("  satu   dua  tiga ") == 3

def test_pemisah_tab_dan_baris_baru():
    assert hitung_kata("a\tb\nc") == 3

def test_string_kosong():
    assert hitung_kata("") == 0

def test_hanya_spasi():
    assert hitung_kata("   ") == 0

def test_input_bukan_str_melempar_type_error():
    with pytest.raises(TypeError, match="teks harus berupa str"):
        hitung_kata(123)
