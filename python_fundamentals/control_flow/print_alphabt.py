#!/usr/bin/env python3
alphabet = ""
for char in range(ord('a'), ord('z') + 1):
    letter = chr(char)
    if letter != 'q' and letter != 'e':
        alphabet += letter

print("{}".format(alphabet), end="")
