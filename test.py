n = int(input("enter the value of n "))
a = 0
b = 1
print(a,b, end=" ")
while n >= 0:
    c = a + b
    print(c,end=" ")
    n = n // 10
print("finished")