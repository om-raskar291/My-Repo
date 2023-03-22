a=int(input("enter the value of a\n"))
print("the entered value of a is ",a)
b=int(input("enter the value of b\n"))
print("the entered value of b is ",b)
c=int(input("enter the value of c\n"))
print("the entered value of c is ",c)
d=int(input("enter the value of d\n"))
print("the entered value of d is ",d)
if a>b and a>c and a>d:
    print("maximum number is a =",a)
elif b>c and b>d:
    print("maximum number is b =",b)
elif c>d:
    print("maximum number is c =",c)
else:
    print("maximum number is d =",d)