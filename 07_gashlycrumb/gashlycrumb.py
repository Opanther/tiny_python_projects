#!/usr/bin/env python3
"""
Author : tomioredein <tomioredein@localhost>
Date   : 2023-01-03
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", nargs="*", help="Letters(s)", type=str
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE",
        default="gashlycrumb.txt",
        type=argparse.FileType("rt"),
        help="Input file",
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
