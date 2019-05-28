"""
This module implements a function that returns a set of random numbers.  The
implementation is based on the random.SystemRandom class that uses the
os.urandom() function for generating random numbers from sources provided by
the operating system.
"""
import random


def gen_rand(numbers=6, start=1, stop=45):
    """Return a set of random numbers sorted in ascending order.

    Generate a set of random numbers based on os.urandom() function from the
    Python standard library random.SystemRandom class, and return as a list
    sorted in ascending order.

    :param numbers: Number of elements in the list.
    :param start: Lower bound random number (inclusive).
    :param stop: Upper bound random number (inclusive).
    :return: A list of unique random numbers sorted in ascending order.
    """
    rnd_gen = random.SystemRandom()
    rnd_set = set()
    while len(rnd_set) < numbers:
        rnd = rnd_gen.randint(start, stop)
        rnd_set.add(rnd)
    return sorted(list(rnd_set))
