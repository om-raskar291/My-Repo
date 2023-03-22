n = int(input("enter n"))
x = [ ]
for i in range(n):
	no = int(input("enter no"))
	x.append(no)
print(x)
while(i<n):
	j=j+1
	while(j<n):
 		if x[i]==x[j]:
		x.remove(j,x[j]):
		n=n-1
		else :
		j=j+1
	i=i+1
x.sort()
print(x)+