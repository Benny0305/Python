import time

a = int(input("Enter your a value: "))
x = int(round(time.time()))
c = int(input("Enter your c value: "))
m = int(input("Enter your m value: "))
generated = 0

go = time.time()
print("Generating Randomized Sequence:""\n")

check = x = (a * x + c) % m
x = (a * x + c) % m 

while x != check:
    x = (a * x + c) % m
    print(str(round(x)), end=" ")
    generated += 1

end = time.time()
ex_time = end - go
print("\n")
print(f"Done. took {round(ex_time, 3)} seconds and generated {generated} values.")