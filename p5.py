print("hello Rolex..")
n = int(input("enter the value of n \n"))

for i in range(n):
	p = "A"
	for j in range(i):
		print(p , end = " ")
		p=chr(ord(p) + 1)
	print()
print("bye bye world")