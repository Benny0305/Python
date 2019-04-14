#This Generates a list of numbers for testing purposes
n = input("How many Numbers should your Dataset have:")
method = input("Which Method do you want to use? All = All Numbers | Narrowed = Only Numbers without 0 and 2&5 :")
filename = str(input("Enter your desired filename:"))
start = 0
stop  = 0

output = open(filename + "_dataset.txt", "w")

if method == str("Narrowed") :
    while int(start) < int(n):
        start += 1
        while "0" in str(start):
            start +=  1
        while "5" in str(start) and "2" in str(start):
            start +=  1
        output.write(str(start) + "\n")
    else:
        output.close()
    
elif method == str("All"):
    while int(start) < int(n):
        start += 1
        output.write(str(start) + "\n")
    else:
        output.close()
else:
    print("Invalid Method!")

