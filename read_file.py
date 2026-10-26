#!/usr/bin/env python3
"""Módulo que contiene la función read_file."""


def read_file(filename=""):
    """Lee un archivo de texto en UTF-8 y lo imprime en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
