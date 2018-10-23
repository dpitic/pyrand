import random


def gen_rand(numbers=6, start=1, stop=45):
    """
    Generate a set of random numbers based on os.urandom() from the Python
    random module.
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
    rnd_seq = list(rnd_set)
    rnd_seq.sort()
    return rnd_seq
