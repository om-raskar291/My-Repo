p = 'A'
for i in range(5,0,-1):
	for k in range(4,i-1,-1):
		print(" ", end = " ")		
	
	for j in range(i):
		print(p ," ", end = " ")
		p =  chr(ord(p) + 1)
	print()