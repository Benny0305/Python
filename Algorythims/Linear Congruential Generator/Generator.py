import time

a = 23209
x = int(round(time.time() * 1000))
c = 9739
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