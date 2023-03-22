r=" "
s = input("enter string\n")
v="AEIOUaeiou"
for p in s:
	if p in v:
		r=r+p

print(r)
	