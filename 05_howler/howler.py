#!/usr/bin/env python3
"""
Author : tomioredein <tomioredein@localhost>
Date   : 2022-12-01
Purpose: Working with files and STDOUT
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", type=str, help="Input string or file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default="",
    )
    # Parse the command-line arguments into the variable args so that we can manually check the text argument.
    args = parser.parse_args()
    # Check if args.text is the name of an existing file.
    if os.path.isfile(args.text):
        # if so, overwrite the value of args.text with the results of reading the file Potential memory problem
        args.text = open(args.text).read().rstrip()
    # Return the arguments to the caller
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    # Call get_args() to get the arguments to the program.
    args = get_args()
    # use an if expression to choose either sys.stdout or a newly opened file handle to write the output.
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    # Use the opened file handle to write the output converted to uppercase.
    out_fh.write(args.text.upper() + "\n")
    # Close the file handle
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
