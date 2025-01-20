"""Autograding script."""

import os

import pandas as pd  # type: ignore

from homework import pregunta_01 as pregunta


def test_01():
    """Test homework"""

    pregunta.pregunta_01()

    # Test: Check if the output file exists
    assert os.path.exists("files/output/solicitudes_de_credito.csv")

   