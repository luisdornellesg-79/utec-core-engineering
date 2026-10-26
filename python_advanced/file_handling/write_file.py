#!/usr/bin/env python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the characters written.

    Creates the file if it does not exist and overwrites it if it does.

    Args:
        filename: path of the file to write.
        text: string to write into the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
