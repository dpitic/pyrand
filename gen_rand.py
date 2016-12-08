import random


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
