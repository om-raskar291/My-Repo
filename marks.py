m1 = float(input("enter marks m1\n"))
m2 = float(input("enter marks m2\n"))
m3 = float(input("enter marks m3\n"))

print("the entered marks m1 is ",m1)
print("the entered marks m2 is ",m2)
print("the entered marks m3 is ",m3)
total = m1+ m2+ m3
per = total/3
print("the total marks is = ", total)
print("the percentage is = ", per)
if per >75 :
	print("Distinction")
elif per>65:
	print("First class")
elif per>55:
	print("second class")
elif per>45:
	print("pass class")
elif per>35:
	print("Fail")
else:
 	print("super fail")
print("bye  bye world !!")
print("!!")