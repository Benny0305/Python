#You can use this to take the Difference between two lines of a text document
filename = str(input("Enter your filename:"))

n = 0

file = open(filename + ".txt", "r")
output = open(filename + "_difference.txt", "w")

file_text=file.readlines()
while str(file_text[n]) != "0":
    a = int(file_text[n])
    b = int(file_text[n+1])
    result = b - a
    n += 1
    output.write(str(result) + "\n")
else:
    print("Done.")


