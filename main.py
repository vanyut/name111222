number = int(input("user"))
a1 = number %10
a2 = number // 10%10
a3 = number // 100%10
a4 = number // 1000%10
a5 = number // 10000%10
a6 = number // 100000
if (a1+a2+a3) == (a4+a5+a6)
    print("happy")
else:
    print("unhappy")
    


number = int(input("User"))

if len(str(number)) == 6:
    a1 = number %10
    a2 = number // 10%10
    a3 = number // 100%10
    a4 = number // 1000%10
    a5 = number // 10000%10
    a6 = number // 100000
    if (a1+a2+a3) == (a4+a5+a6):
        print("happy")
    else:
        print("unhappy")
else:
    print("invalid")