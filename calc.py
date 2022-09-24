

# for x in "banana":
#   print(x)

exit = False
while exit == False:
    userNumber1 = input("enter 1st number: ")

    # this if statement is designed to check if the user entered a digit instead of something else (i.e typo)
    if userNumber1.isdigit() == False:
        print("Can only use whole numbers")
        continue

    userOperator = input("+, -, * or /: ")
    userNumber2 = input("enter 2nd number: ")

    if userNumber2.isdigit() == False:
        print("Can only use whole numbers")
        continue

    if userOperator == "+":
        userResult = int(userNumber1) + int(userNumber2)
        exit = True

    if userOperator == "-":
        userResult = int(userNumber1) - int(userNumber2)
        exit = True

    if userOperator == "*":
        userResult = int(userNumber1) * int(userNumber2)
        exit = True

    if userOperator == "/":
        userResult = int(userNumber1) / int(userNumber2)
        exit = True

    else:
        userResult="I can only do + or -"
        
    print(userResult)
