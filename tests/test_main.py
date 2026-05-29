import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from main import saudacao, calcular_media
import pytest
from main import verificar_peso_carga

def test_carga_permitida():
    assert verificar_peso_carga(10.0) == "Peso dentro do limite seguro."

def test_carga_excedida():
    assert verificar_peso_carga(25.0) == "Carga Excedida! Risco de seguranca."

def test_erro_tipo_invalido():
    with pytest.raises(TypeError):
        verificar_peso_carga("vinte quilos")