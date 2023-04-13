#!/usr/bin/python3
"""append_write module"""

def append_write(filename="", text=""):
    """Appends text to a file and returns number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
