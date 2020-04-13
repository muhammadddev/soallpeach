import sys
import time
import math

file_name = sys.argv[1]


def is_prime(n: int):
    """
    Assumes that n is a positive natural number
    """
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# start_time = time.time()

with open(file_name) as input_numbers:
    for line in input_numbers:
        print(is_prime(int(line)))

# end_time = time.time()
# print(end_time - start_time)