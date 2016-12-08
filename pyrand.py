import random
import sys
import getopt


"""
Script used to generate sets of random numbers based on os.urandom(). The sets
are sorted in ascending order.
"""


def gen_rand(numbers=6, start=1, stop=45):
    """
    Generate a set of random numbers based on os.urandom().
    :param numbers: Number of elements in the list.
    :param start: Lower bound random number (inclusive).
    :param stop: Upper bound random number (inclusive).
    :return: A list of unique random numbers sorted in ascending order.
    """
    rnd_gen = random.SystemRandom()
    rnd_seq = []
    while len(rnd_seq) < numbers:
        rnd = rnd_gen.randint(start, stop)
        # Ensure the list contains unique random numbers
        if rnd not in rnd_seq:
            rnd_seq.append(rnd)
    return rnd_seq


def usage():
    """
    Display the command line argument usage.
    :return: None
    """
    print("Usage: pyrand.py [OPTION]")
    print("Generate sets of random numbers sorted in ascending order.")
    print()
    print("Optional arguments:")
    print("\t-t, --total=1\tTotal number of sets to produce.")
    print("\t-n, --numbers=6\tNumber of elements in the set.")
    print("\t-l, --lower=1\tLower bound (inclusive) random number.")
    print("\t-u, --upper=45\tUpper bound (inclusive) random number.")
    print("\t-h, --help\tDisplay this help and exit.")
    print()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "t:n:l:u:h",
                                   ["total=", "numbers=", "lower=", "upper=",
                                    "help"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    total = 1
    numbers = 6
    lower = 1
    upper = 45

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-t", "--total"):
            total = int(arg)
        elif opt in ("-n", "--numbers"):
            numbers = int(arg)
        elif opt in ("-l", "--lower"):
            lower = int(arg)
        elif opt in ("-u", "--upper"):
            upper = int(arg)

    for i in range(total):
        seq = gen_rand(numbers, lower, upper)
        seq.sort()
        print("{}:\t{}".format(i + 1, seq))


if __name__ == '__main__':
    main()
