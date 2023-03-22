no = int(input("Enter Number\n"))
print("You have entered", no,"as number")
a = 0
b = 1
print(a,b,end=" ")
for i in range (1 , no-1):
    c = a + b
    print(c , end=" ")
    a = b
    b = c
print("\nfinished")