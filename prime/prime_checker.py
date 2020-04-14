import sys

file_name = sys.argv[1]


def is_prime(n: int):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

with open(file_name) as input_numbers:
    for line in input_numbers:
        print(1 if is_prime(int(line)) else 0)
