q = "A"
for i in range(1,5):
	p = q
	for  k in range(4,i-1,-1):
		print(" ", end = " ")
	for j in range(i):
		print(p , " " ,end = " ")
		p = chr(ord(p)-1)
	print()
	q =chr(ord(p)+1)