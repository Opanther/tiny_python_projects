#!/usr/bin/env python3
"""
Author : tomioredein <tomioredein@localhost>
Date   : 2022-11-29
Purpose: Jump the five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jump = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }
    # Solution 1
    # for char in args.text:
    #     print(jump.get(char, char), end="")
    #
    # print()

    # List comprehension solution

    # print("".join([jump.get(char, char) for char in args.text]))

    # Using the str.translate function
    print(args.text.translate(str.maketrans(jump)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
