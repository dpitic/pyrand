import argparse
import math
import sys
import more_itertools as mit

"""
Script used to generate sets of random numbers based on the more_itertools
module. The sets are sorted in ascending order. This implementation uses the
argparse module.
"""


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='''Generate sets of random
    numbers sorted in ascending order.''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--total', type=int, default=1,
                        help='total number of sets to produce.')
    parser.add_argument('-n', '--numbers', type=int, default=6,
                        help='number of elements in the set.')
    parser.add_argument('-l', '--lower', type=int, default=1,
                        help='lower bound (inclusive) random number.')
    parser.add_argument('-u', '--upper', type=int, default=45,
                        help='upper bound (inclusive) random number.')
    args = parser.parse_args()

    # Sequence number output field width and format string
    seq_width = int(math.log10(args.total)) + 1
    # Sequence element output field width and format string
    elem_width = int(math.log10(args.upper)) + 1

    # Generate and output the random number sets to stdout
    for i in range(args.total):
        seq = mit.random_combination(
            [i + 1 for i in range(args.lower - 1, args.upper)], args.numbers)
        print(f'{i+1:{seq_width}d}:\t[ ', end='')
        for elem in seq:
            print(f'{elem:{elem_width}d} ', end='')
        print(']')


if __name__ == '__main__':
    # This code uses formatted string literals (f-string) which are only
    # supported in v3.6
    assert sys.version_info.major >= 3, "Require Python >= v3.6"
    assert sys.version_info.minor >= 6, "Require Python >= v3.6"
    main()
