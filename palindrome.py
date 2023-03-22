while  True:
    no = int(input("enter the value of no\n"))
    s = 0
    t = no
    while no > 0:
        rem = no % 10
        no = no // 10
        s = s * 10 + rem
    print("reverse number =", s)
    if s == t:
        print("Palindrome number")
    else:
        print("not palindrome number")
