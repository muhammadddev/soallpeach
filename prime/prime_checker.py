import sys
import math
# import time

file_name = sys.argv[1]


def is_prime(n: int):
    if n <= 1:
        return False

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False

    if n % 5 == 0:
        return False
    
    if n % 7 == 0:
        return False

    for i in range(11, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # start_time = time.time()
    with open(file_name) as input_numbers:
        for line in input_numbers:
            print(1 if is_prime(int(line)) else 0)
    # stop_time = time.time()
    # print(stop_time - start_time)