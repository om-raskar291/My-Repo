print("hello world")
n = int(input("enter the value of n \n"))
for i in range(n):
	for j in range(i):
		print(" * ", end=" ")
	print()
print(" bye bye world")