print("hello Rolex..")
n = int(input("enter the value of n \n"))
p=1
for i in range(n):
	for j in range(i):
		print(p, end = " ")
		p = p + 1
	print()
print("bye bye world") 