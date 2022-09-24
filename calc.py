

# for x in "banana":
#   print(x)

exit = False
while exit == False:
    userNumber1=input("enter 1st number")
    userNumber2=input("enter 2nd number")
    userOperator=input("+ or -")

    if userOperator == "+":
        userResult=int(userNumber1)+int(userNumber2)
        exit = True
    if userOperator == "-":
        userResult=int(userNumber1)-int(userNumber2)
        exit = True
    else:
        userResult="I can only do + or -"
    print(userResult)
