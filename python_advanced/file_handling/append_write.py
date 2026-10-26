#!/usr/bin/env python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to the end of a UTF-8 file.

    Creates the file if it does not exist.

    Args:
        filename: path of the file to append to.
        text: string to add at the end of the file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
