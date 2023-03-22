p = 'A'
for i in  range(5,0,-1):
	
	for j in range(i):
		print(p , end = " ")
		
	print()
	p = chr(ord(p) + 1)
