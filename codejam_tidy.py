import sys
import numpy as np
import itertools
OCC = 1
store = []
fileContent = open("B-large-practice.in", "r")
writeFile = open("B_large-practice.out", "w")
# nOTC = fileContent[0]
def convertInt(intVal):
	data = int("".join(map(str, intVal)))
	return data

def check(num):
	split = list(str(num))
	if(len(split) > 10):
		getNlist = list(str(num))
		getNlist.pop(0)
		covert = int(''.join(str(v) for v in getNlist))
		subtractor = covert + 1 
		tidy = num-subtractor
		print tidy
	else:	
		sort = sorted(split)
		covert = int(''.join(str(v) for v in sort)) 
		if(covert == num):
			tidy =num
			print tidy
		else:
			newList = split[-1]
			store.append(newList)
			getter = convertInt(store)+1
			nextTidy = num - getter
			print  nextTidy
# print check(150)

for line in itertools.islice(fileContent, 1, 100):
	result =  check(line)
	print("Case #{}: {}".format(OCC, result))
	writeFile.write("Case #{}: {}".format(OCC, covert) + '\n')
	OCC += 1