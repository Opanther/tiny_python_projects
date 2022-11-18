#!/usr/bin/env python3
"""
Author : tomioredein <tomioredein@localhost>
Date   : 2022-11-17
Purpose: Working with list
"""

import argparse


# --------------------------------------------------

# The get_args() function is placed first so i can easily see what the program accepts when we read it.
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # The item argument uses nargs='+' so that it will accept one or more positional arguments, which will be strings.
    parser.add_argument("items", metavar="str", help="Item(s) to bring", nargs="+")
    # The dashes in the short (-s) and long (--sorted) names make this an option. There is no value associated with this argument. It’s either present (in which case it will be True) or absent (False).
    parser.add_argument(
        "-s",
        "--sorted",
        action="store_true",
        help="Sort the items",
    )
    # Process the command-line arguments and return them to the caller.
    return parser.parse_args()


# --------------------------------------------------


# The main() function is where the program will start.


def main():
    """Make a jazz noise here"""
    # Call the get_args() function and put the returned value into the variable args. If there is a problem parsing the arguments, the program will fail before the values are returned.
    args = get_args()
    # Copy the item list from args into the new variable items.
    items = args.items
    # Use the length function len() to get the number of items in the list. There can never be zero items because we defined the argument using nargs='+', which always requires at least one value.
    num = len(items)
    # The args.sorted value will be either True or False.
    # If we are supposed to sort the items, call the items.sort() method to sort them in place.
    if args.sorted:
        items.sort()
    # Use an empty string to initialize a variable to hold the items we are bringing.
    bringing = ""
    # If the number of items is 1, we will assign the one item to bringing.
    if num == 1:
        bringing = items[0]
    # If the number of items is 2, put the string ' and ' in between the items
    elif num == 2:
        bringing = " and ".join(items)
    # Otherwise, alter the last element in items to append the string 'and ' before whatever is already there.
    else:
        items[-1] = "and " + items[-1]
        # Join the items on a string of comma and space.
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
