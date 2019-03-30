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

start = int(input("Enter your starting Number: "))
run_until = int(input("Enter the desired persistence: "))

go = time.time()

while persistence(start) != run_until :
    start = start + 1
    while "0" in str(start):
        start = start + 1
    while "5" in str(start) and "2" in str(start):
        start = start + 1
else: 
    print("The closest Number with that persistence is: " + str(start))
    end = time.time()
    ex_time = end - go
    print("Calculation has taken: " + str(round(ex_time, 3)) + " seconds")
