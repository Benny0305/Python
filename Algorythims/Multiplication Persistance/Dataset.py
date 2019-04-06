start = 0
stop = 1000
n = 0

while n < stop:
    start = start + 1
    while "0" in str(start):
        start = start + 1
    while "5" in str(start) and "2" in str(start):
        start = start + 1
    n = n + 1
    print(start)
