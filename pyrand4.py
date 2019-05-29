"""
Script used to generate sets of random numbers based on the Python standard
library secrets module. The sets are sorted in ascending order. This
implementation uses the argparse module.
"""
import argparse
import math
import secrets
import sys


def main():
    """Script entry function."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='''Generate sets of consecutive random numbers between
        specified bounds, sorted in ascending order.  This implementation uses
        Python standard library secrets module, which generates secure
        random numbers.''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t',
                        '--total',
                        type=int,
                        default=1,
                        help='total number of sets to produce.')
    parser.add_argument('-n',
                        '--numbers',
                        type=int,
                        default=6,
                        help='number of elements in the set.')
    parser.add_argument('-l',
                        '--lower',
                        type=int,
                        default=1,
                        help='lower bound (inclusive) random number.')
    parser.add_argument('-u',
                        '--upper',
                        type=int,
                        default=45,
                        help='upper bound (inclusive) random number.')
    args = parser.parse_args()

    # Sequence number output field width for format string
    seq_width = int(math.log10(args.total)) + 1
    # Sequence element output field width for format string
    elem_width = int(math.log10(args.upper)) + 1

    # Secure random number generator
    srng = secrets.SystemRandom()

    # Generate and output the random number sets to stdout
    for i in range(args.total):
        # Population sequence
        pop_seq = range(args.lower, args.upper + 1)
        # Random sampling without replacement, sorted ascending
        sample_seq = sorted(srng.sample(pop_seq, args.numbers))
        print(f'{i+1:{seq_width}d}:\t[ ', end='')
        for elem in sample_seq:
            print(f'{elem:{elem_width}d} ', end='')
        print(']')


if __name__ == '__main__':
    # This code uses formatted string literals (f-string) which are only
    # supported in v3.6 and above.
    assert sys.version_info.major >= 3, "Require Python >= v3.6"
    assert sys.version_info.minor >= 6, "Require Python >= v3.6"
    main()
