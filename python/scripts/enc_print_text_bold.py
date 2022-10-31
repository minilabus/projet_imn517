#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import argparse


from encoding.io.utils import print_text_in_bold


def _build_arg_parser():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument('in_text', choices=['Hello', 'World'], nargs='+',
                   help='Text to be printed in bold.')
    return p


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    print_text_in_bold(args.in_text)


if __name__ == '__main__':
    main()
