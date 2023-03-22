import re
s=" java is oops and cpp is pos and oops"
p=re.match("is oops",s)
if p:
	print(p.group())
else:
	print("no match")