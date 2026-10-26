#!/usr/bin/env python3
"""Module that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename: path of the text file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
