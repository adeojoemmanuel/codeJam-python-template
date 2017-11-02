import sys
import numpy as np
import itertools
OCC = 1

fileContent = open("B-large-practice.in", "r")
writeFile = open("B_large-practice.out", "w")

# range = lambda stop: iter(itertools.count().next, stop)

def range(start=0,stop=None,step=1):
	if stop is None:
		stop = start
		start = 0
	i = start
	while i < stop:
		yield i
		i += step

mainArr = []
for line in itertools.islice(fileContent, 1, 101):
	currentLine = int(line)
	for i in range(1, currentLine + 1):
		val = list(str(i))
		res = list(map(int, val))
		mainSort = (int(e) for e in val)
		newData = sorted(mainSort)
		if(res == newData):
			mainArr.append(newData)
		dat = len(mainArr) - 1
	result =  mainArr[dat]
	# if(len(result) < 2):
	covert = int(''.join(str(v) for v in result)) 
	# else:
		# covert = int(''.join(str(v) for v in result))
	print("Case #{}: {}".format(OCC, covert))
	writeFile.write("Case #{}: {}".format(OCC, covert) + '\n')
	OCC += 1
