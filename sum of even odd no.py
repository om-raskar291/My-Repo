no = int(input("enter the value of no"))
x = 0
y = 0
while no > 0:
    a = no % 10
    if a % 2 == 0:
        x = x + a
    else:
        y = y + a
    no = no // 10
print("the value of even number is ",x)
print("the value of even number is ",y)

