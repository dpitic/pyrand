import random
import sys


"""
Script used to generate lists of random numbers based on os.urandom(). The lists
are sorted in ascending order.
"""


def gen_rand(numbers=6, start=1, stop=45):
    rnd_gen = random.SystemRandom()
    rnd_seq = []
    while len(rnd_seq) < numbers:
        rnd = rnd_gen.randint(start, stop)
        if rnd not in rnd_seq:
            rnd_seq.append(rnd)
    return rnd_seq


def main():
    total = int(1 if (len(sys.argv) < 2) else sys.argv[1])
    numbers = int(6 if (len(sys.argv) < 3) else sys.argv[2])
    start = int(1 if (len(sys.argv) < 4) else sys.argv[3])
    stop = int(45 if (len(sys.argv) < 5) else sys.argv[4])
    for i in range(total):
        seq = gen_rand(numbers, start, stop)
        seq.sort()
        print("{}:\t{}".format(i + 1, seq))


if __name__ == '__main__':
    main()
