import sys
import numpy as np
from iteration_utilities import all_monotone
import itertools
OCC = 1
store = []
fileContent = open("B-large-practice.in", "r")
writeFile = open("B_large-practice.out", "w")
# nOTC = fileContent[0]

def magicDecrypt(numList):
	s = map(str, numList)
	s = ''.join(s)
	s = int(s)
	return s
	

# print magicDecrypt(['7'])

def rule1(num):
	getNlist = list(str(num))
	if(len(getNlist) == 1):
		getNlist.insert(0, '0')
	getNlist.pop(0)
	param = map(int, getNlist)
	convert = magicDecrypt(param)
	subtractor = int(convert) + 1 
	tidy = int(num)-subtractor
	result = list(str(tidy))
	return result

def rule2(num):
	split = list(str(num))
	sort = sorted(split)
	covert = int(''.join(str(v) for v in sort)) 
	if(covert == num):
		nextTidy =num
		result = list(str(nextTidy))
		return result
	elif(len(split) == 1):
		nextTidy = num
		result = list(str(nextTidy))
		return result
	else: 
		newList = split[-1]
		additor = int(newList) + 1
		nextTidy = num - additor
		result = list(str(nextTidy))
		return  result
# print rule2(132)
# print magicDecrypt(['1', '2', '9'])

def main(fr1, fr2):
	arr = []
	firstResult = all_monotone(fr1)
	secondResult = all_monotone(fr2)
	if (firstResult == True and secondResult == False):
		data = map(str, fr1)
		covert1 = int(''.join(data)) 
		return covert1

	elif(firstResult == False and secondResult == True):
		data = map(str, fr2)
		covert2 = int(''.join(data)) 
		return covert2

	elif(firstResult == True and secondResult == True):
		data = map(str, fr1)
		covert1 = int(''.join(data)) 
		data2 = map(str, fr2)
		covert2 = int(''.join(data2)) 
		if(covert1 > covert2):
			return covert1
		if(covert2 > covert1):
			return covert2
		if(covert1 == covert2):
			return covert1
		else:
			return "not equal"
	elif(firstResult == False and secondResult == False):
		return "both false"

	else:
		return "catching noting"
		
# print main(['9','1'], ['1','2','9'])

for line in itertools.islice(fileContent, 1, 101):
	lineConvert = int(line)
	firstResult =  rule1(lineConvert)
	secondResult =  rule2(lineConvert)
	tidyNum = main(firstResult, secondResult)
	print("Case #{}: {}".format(OCC, tidyNum))
	writeFile.write("Case #{}: {}".format(OCC, tidyNum) + '\n')
	OCC += 1
