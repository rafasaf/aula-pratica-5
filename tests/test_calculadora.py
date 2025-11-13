import pytest
from src.calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(3, 5) == 8

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(6, 7) == 42

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)
