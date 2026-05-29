# flake8: noqa: E402
import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import saudacao, calcular_media


def test_saudacao():
    assert saudacao("Mundo") == "Olá, Mundo!"


def test_calcular_media():
    assert calcular_media([10, 8, 6]) == 8
    assert calcular_media([]) == 0