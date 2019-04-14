from functools import reduce
from operator import mul
import time

def get_digits(number):

    while number:
        digit = number % 10
        yield digit
        number //= 10


def persistence(number, count=0):

    if number < 10:
        return count
    new_number = reduce(mul, get_digits(number))
    return persistence(new_number, count + 1)

def run(start, run_until):
    while persistence(start) != desired_persistence:
        start += 1
        while "0" in str(start) and desired_persistence != 1 and desired_persistence != 2:
            start +=  1
        while "5" in str(start) and "2" in str(start) and desired_persistence != 1 and desired_persistence != 2:
            start +=  1
    else:
        return start

start = int(input("Enter your starting Number: "))
desired_persistence = int(input("Enter the desired persistence: "))
amount = int(input("Enter the amount of the desired numbers:"))
print()

go = time.time()

while amount > 0:
    start = run(start, desired_persistence)
    print(start, end=" ")
    amount -= 1
    start  += 1
else:
    print("\n")
    end = time.time()
    ex_time = end - go
    print(f"Calculation has taken: {round(ex_time, 3)} seconds")