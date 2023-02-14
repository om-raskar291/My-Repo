while True:
    no = int(input("enter the value of no\n"))
    a = int(input("enter the value of a\n"))
    b = int(input("enter the value of b\n"))
    if no == 1:
        sum = a + b
        print("the sum of a and b is\n", sum)
    elif no == 2:
        sub = a - b
        print("the sub of a and b is\n", sub)
    elif no == 2:
        sub = a - b
        print("the sub of a and b is\n", sub)
    elif no == 3:
        mul = a - b
        print("the mul of a and b is\n", mul)
    elif no == 4:
        div = a / b
        print("the div of a and b is\n", div)
    elif no == 5:
        rem = a % b
        print("the rem of a and b is\n", rem)
    elif no == 6:
        power = a ** b
        print("the power of a and b is\n", power)
    elif no == 7:
        quit()
    else:
        print("invalid operation")
