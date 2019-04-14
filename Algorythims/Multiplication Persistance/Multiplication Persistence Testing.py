from functools import reduce
from operator import mul
import time

x = 0
goal = input("Enter your desired goal:")
y = int(goal)
go = time.time()
while x * y != goal and y > 0:
    x += 1
    y -= 1
else: 
    print(x)
    print(y)
    end = time.time()
    ex_time = end - go
    print(f"Calculation has taken: {round(ex_time, 3)} seconds")