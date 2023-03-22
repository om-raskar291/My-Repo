print("hello world")
n = int(input("enter the value of n \n"))
for i in range(n):
	p = 100
	for j in range(i):
		print(p, end = " ")
		p = p - 1	
	print()