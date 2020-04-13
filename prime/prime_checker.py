import sys
import time

file_name = sys.argv[1]


def is_prime(n: int):
    for m in range(3, n - 1):
        if n % m == 0:
            return 0
    return 1


with open(file_name) as input_numbers:
    start_time = time.time()
    numbers = list()
    for line in input_numbers:
        number = int(line)
        numbers.append(number)

    results = map(is_prime, numbers)
        
    for r in results:
        print(r)
    end_time = time.time()
    # print(end_time - start_time)