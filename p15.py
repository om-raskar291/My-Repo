p = 'O'
for i in  range(5,0,-1):
	
	for j in range(i):
		print(p , end = " ")
		p = chr(ord(p) - 1)
	print()
	
