import sys
OCC = 1

fileContent = open("larg_input.txt", "r")
writeFile = open("output.txt", "w")
max= 0
for line in fileContent:
	newline = int(line)
	data = [int(i) for i in str(newline)]
    for i in data:
        if i > max:
            max=i
    print(max)

