def getTidy(input):
	tidy = 1
	for i in range(1, input):
		if(len(str(input)) < 2):
			tidy = input
			break
		tmp = list(str(i))
		sorted = "true"
		for j in range(1,len(tmp)):
			if(j > len(tmp) - 2):
				continue
			if(tmp[j+1] < tmp[j]):
				sorted = "false"
		if(sorted == "false"):
			continue
		else:
			if(i > tidy):
				tidy = i
	print tidy
getTidy(111111111111111110)
