#Initial Values
start = 0
stop = 1000000
n = 0

#Splitting up the lines Values
colons = 10
count = colons



#Just removing all numbers containing 0 and 2&5 in 
while n < stop:
    start = start + 1
    while "0" in str(start):
        start = start + 1
    while "5" in str(start) and "2" in str(start):
        start = start + 1
    n = n + 1

#Splitting it up into colons of 10 for the output
    if count > 0:
        print(str(start), end=" ")
        count -= 1
    else:
        print()
        count = colons


