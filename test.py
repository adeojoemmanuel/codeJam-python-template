def range(start=0,stop=None,step=1):
	if stop is None:
		#handle single argument case. ugly...
		stop = start
		start = 0
	i = start
	while i < stop:
		yield i
		i += step

for i in range(1, 111111111111111110):
	print i