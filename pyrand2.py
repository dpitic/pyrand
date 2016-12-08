import argparse
from gen_rand import gen_rand

"""
Script used to generate sets of random numbers based on os.urandom(). The sets
are sorted in ascending order. This implementation uses the argparse module.
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

    # Generate the random number sets
    for i in range(args.total):
        seq = gen_rand(args.numbers, args.lower, args.upper)
        seq.sort()
        print('{}:\t{}'.format(i + 1, seq))


if __name__ == '__main__':
    main()
