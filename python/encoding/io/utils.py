# -*- coding: utf-8 -*-

"""
"""


def print_text_in_bold(text):
    if isinstance(text, list):
        text = " ".join(text)
    print('\033[1m'+text+'\033[0m')
