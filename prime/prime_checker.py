from __future__ import print_function
import sys
import math
import time
from multiprocessing import Pool


file_name = sys.argv[1]


def is_prime(n):
    flag = -1
    for m in range(2, int(math.sqrt(n)) + 1):
        if n % m == 0:
            flag = 0
    
    if flag == -1:
        flag = 1
    
    print(flag)


if __name__ == "__main__":
    p = Pool(5)
    start_time = time.time()
    with open(file_name) as input_numbers:
        l =tuple([int(line) for line in input_numbers])

    p.map(is_prime, l)

    stop_time = time.time()
    print(stop_time - start_time)