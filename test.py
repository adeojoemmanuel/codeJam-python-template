list1 = [[1,2,3],[4,5,6],[7,8,9]]

def joinAll(Mulist):
	index_all=[]
	for i in list1:
		for u in i:
			index_all.append(u)
	return index_all

print joinAll(list1)
