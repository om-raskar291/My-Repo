q = 5 
for i in range(1,6):
	p = q
	for j in range(i):
		print(p , end = " ")
		p = p + 1
	print()
	q = q - 1