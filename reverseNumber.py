no = int(input("enter the value of no\n"))
s = 0
while no > 0:
     rem = no % 10
     no = no // 10
     s = s * 10 + rem
print("the reverse of number is",s)