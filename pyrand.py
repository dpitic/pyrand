import getopt
import sys
import math
from gen_rand import gen_rand

"""
Script used to generate sets of random numbers based on os.urandom(). The sets
are sorted in ascending order. This implementation uses the getopt module.
"""


def usage():
    """
    Display the command line argument usage.
    :return: None
    """
    print('Usage: pyrand.py [OPTION]')
    print('Generate sets of random numbers sorted in ascending order.')
    print('This implementation uses os.urandom() standard library function.')
    print()
    print('Optional arguments:')
    print('\t-t, --total=1\ttotal number of sets to produce.')
    print('\t-n, --numbers=6\tnumber of elements in the set.')
    print('\t-l, --lower=1\tlower bound (inclusive) random number.')
    print('\t-u, --upper=45\tupper bound (inclusive) random number.')
    print('\t-h, --help\tdisplay this help and exit.')
    print()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   't:n:l:u:h',
                                   ['total=', 'numbers=', 'lower=', 'upper=',
                                    'help'])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    total = 1
    numbers = 6
    lower = 1
    upper = 45

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-t', '--total'):
            total = int(arg)
        elif opt in ('-n', '--numbers'):
            numbers = int(arg)
        elif opt in ('-l', '--lower'):
            lower = int(arg)
        elif opt in ('-u', '--upper'):
            upper = int(arg)

    # Sequence number output field width for format string
    seq_width = int(math.log10(total)) + 1
    # Sequence element output field width for format string
    elem_width = int(math.log10(upper)) + 1

    for i in range(total):
        seq = gen_rand(numbers, lower, upper)
        print(f'{i+1:{seq_width}d}:\t[ ', end='')
        for elem in seq:
            print(f'{elem:{elem_width}d} ', end='')
        print(']')


if __name__ == '__main__':
    # This code uses formatted string literals (f-string) which are only
    # supported in v3.6 and above.
    assert sys.version_info.major >= 3, "Require Python >= v3.6"
    assert sys.version_info.minor >= 6, "Require Python >= v3.6"
    main()
