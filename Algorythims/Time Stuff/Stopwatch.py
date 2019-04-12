import sys
import time

duration = 0

input("Hit Enter to start counting. (Ctrl + c to stop)")

try:
    while True:
        duration += 1
        time.sleep(1)
        print(duration,"seconds", end='\r')
except KeyboardInterrupt:
    pass
