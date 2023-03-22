for i in  range(5,0,-1):
	p = 'A'
	for j in range(i):
		print(p , end = " ")
		p = chr(ord(p) + 1)
	print()
