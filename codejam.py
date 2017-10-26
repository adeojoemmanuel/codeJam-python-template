import sys
count = 0
file_object = open("input_file.txt", "r")
thefile = open('test.txt', 'w')
for line in file_object:
	lines = int(line)
	if (count == 0):
		count += 1
		continue
	data = lines * 2

	# sys.stdout=open("test.txt","w")
	print("Case #{}: {}".format(count, lines))
	# sys.stdout.close()
