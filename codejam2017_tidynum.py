import sys
import numpy as np
import itertools
OCC = 1

fileContent = open("B-small-practice.in", "r")
writeFile = open("BOutput.in", "w")
# listContent = str(fileContent[1:100])
# for line in itertools.islice(text_file, 19, 52):

mainArr = []
for line in itertools.islice(fileContent, 1, 101):
	currentLine = int(line)
	for i in range(1, currentLine):
		val = list(str(i))
		res = list(map(int, val))
		mainSort = (int(e) for e in val)
		newData = sorted(mainSort)
		if(res == newData):
			mainArr.append(newData)
		dat = len(mainArr) - 1
# print mainArr
# # print mainArr[dat]
	result =  mainArr[dat]
	covert = int(''.join(str(v) for v in result))
	print("Case #{}: {}".format(OCC, covert))
	writeFile.write("Case #{}: {}".format(OCC, covert))
	OCC += 1
