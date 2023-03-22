import re
s="JavaCpplanguage"
m=re.split("[AEIOUaeiou]",s)
print(m)
p=re.findall("[AEIOUaeiou]",s)
print(p)