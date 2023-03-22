import re
s=input("enter string")
m=re.findall("[AEIOUaeiou]",s)
r=" ".join(m)
print(r)