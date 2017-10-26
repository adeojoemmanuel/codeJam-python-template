import sys
OCC = 1

fileContent = open("larg_input.txt", "r")
writeFile = open("output.txt", "w")

for line in fileContent:
	currentLine = int(line)
	newData = currentLine * 2
	print("Case #{}: {}".format(OCC, newData))
	writeFile.write("Case #{}: {}".format(OCC, newData) + '\n')

	OCC += 1