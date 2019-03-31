import time

a = 187
x = 1
c = 197
m = 10000

amount = 100
go = time.time()
print("Generating Randomized Sequence:""\n")
while amount > 0:
    x = (a * x + c) % m 
    print(str(round(x)), end=" ");
    amount -= 1 

end = time.time()
ex_time = end - go
print("\n")
print(f"Done. took {round(ex_time, 3)} seconds")
