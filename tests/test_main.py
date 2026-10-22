import pytest
from main import calcular_area_triangulo

def test_calcular_area_triangulo():
    actual_result = calcular_area_triangulo(4, 5)
    assert actual_result == pytest.approx(9.98, abs=0.01)