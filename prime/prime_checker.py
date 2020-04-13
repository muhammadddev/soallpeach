import sys
import time
import math

file_name = sys.argv[1]


def is_prime(n: int):
    for m in range(3, round(math.sqrt(n))):
        if n % m == 0:
            return 0
    return 1

# start_time = time.time()

with open(file_name) as input_numbers:
    content = input_numbers.readlines()
    for c in content:
        print(is_prime(int(c.strip())))

# end_time = time.time()
# print(end_time - start_time)