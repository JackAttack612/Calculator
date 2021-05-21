print("\nUse +, -, *, or / as the operator")
print('This calculator uses order of operation')

option = input("\nChoose ammount of variables (2/3/4): ")

if option == "2":
    num1 = float(input("\nEnter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator. Please use +, -, /, or *")

if option == "3":
    num12 = float(input("\nEnter first number: "))
    op2 = input("Enter operator: ")
    num22 = float(input("Enter second number: "))
    op3 = input("Enter second operator: ")
    num32 = float(input("Enter third number: "))

    if op2 and op3 == "+":
        print(num12 + num22 + num32)
    elif op2 == "+" and op3 == "-":
        print(num12 + num22 - num32)
    elif op2 == "+" and op3 == "*":
        print(num12 + num22 * num32)
    elif op2 == "+" and op3 == "/":
        print(num12 + num22 / num32)
    elif op2 == "-" and op3 == "-":
        print(num12 - num22 - num32)
    elif op2 == "-" and op3 == "+":
        print(num12 - num22 + num32)
    elif op2 == "-" and op3 == "*":
        print(num12 - num22 * num32)
    elif op2 == "-" and op3 == "/":
        print(num12 - num22 / num32)
    elif op2 == "/" and op3 == "/":
        print(num12 / num22 / num32)
    elif op2 == "/" and op3 == "+":
        print(num12 / num22 + num32)
    elif op2 == "/" and op3 == "-":
        print(num12 / num22 - num32)
    elif op2 == "/" and op3 == "*":
        print(num12 / num22 * num32)
    elif op2 == "*" and op3 == "*":
        print(num12 * num22 * num32)
    elif op2 == "*" and op3 == "+":
        print(num12 * num22 + num32)
    elif op2 == "*" and op3 == "-":
        print(num12 * num22 - num32)
    elif op2 == "*" and op3 == "/":
        print(num12 * num22 / num32)

if option == "4":
    num13 = float(input("\nEnter first number: "))
    op4 = input("Enter operator: ")
    num23 = float(input("Enter second number: "))
    op5 = input("Enter second operator: ")
    num33 = float(input("Enter third number: "))
    op6 = input("Enter Third operation: ")
    num43 = float(input("Enter fourth number: "))

    if op4 == "+" and op5 == "+" and op6 == "+":
        print(num13 + num23 + num33 + num43)
    elif op4 == "+" and op5 == "+" and op6 == "-":
        print(num13 + num23 + num33 - num43)
    elif op4 == "+" and op5 == "+" and op6 == "/":
        print(num13 + num23 + num33 / num43)
    elif op4 == "+" and op5 == "+" and op6 == "*":
        print(num13 + num23 + num33 * num43)
    elif op4 =="+" and op5 =="-" and op6 == "+":
        print(num13 + num23 - num33 + num43)
    elif op4 =="+" and op5 =="-" and op6 == "-":
        print(num13 + num23 - num33 - num43)
    elif op4 =="+" and op5 =="-" and op6 == "/":
        print(num13 + num23 - num33 / num43)
    elif op4 =="+" and op5 =="-" and op6 == "*":
        print(num13 + num23 - num33 * num43)
    elif op4 =="-" and op5 =="+" and op6 == "+":
        print(num13 - num23 + num33 + num43)
    elif op4 =="-" and op5 =="+" and op6 == "-":
        print(num13 - num23 + num33 - num43)
    elif op4 =="-" and op5 =="+" and op6 == "/":
        print(num13 - num23 + num33 / num43)
    elif op4 =="-" and op5 =="+" and op6 == "*":
        print(num13 - num23 + num33 * num43)
    elif op4 =="-" and op5 =="-" and op6 == "+":
     print(num13 - num23 - num33 + num43)
    elif op4 =="-" and op5 =="-" and op6 == "-":
        print(num13 - num23 - num33 - num43)
    elif op4 =="-" and op5 =="-" and op6 == "/":
        print(num13 - num23 - num33 / num43)
    elif op4 =="-" and op5 =="-" and op6 == "*":
        print(num13 - num23 - num33 * num43)
    elif op4 =="/" and op5 =="+" and op6 == "+":
        print(num13 / num23 + num33 + num43)
    elif op4 =="/" and op5 =="+" and op6 == "-":
        print(num13 / num23 + num33 - num43)
    elif op4 =="/" and op5 =="+" and op6 == "/":
        print(num13 / num23 + num33 / num43)
    elif op4 =="/" and op5 =="+" and op6 == "*":
        print(num13 / num23 + num33 * num43)
    elif op4 =="/" and op5 =="-" and op6 == "+":
        print(num13 / num23 - num33 + num43)
    elif op4 =="/" and op5 =="-" and op6 == "-":
        print(num13 / num23 - num33 - num43)
    elif op4 =="/" and op5 =="-" and op6 == "/":
        print(num13 / num23 - num33 / num43)
    elif op4 =="/" and op5 =="-" and op6 == "*":
        print(num13 / num23 - num33 * num43)
    elif op4 =="*" and op5 =="+" and op6 == "+":
        print(num13 * num23 + num33 + num43)
    elif op4 =="*" and op5 =="+" and op6 == "-":
        print(num13 * num23 + num33 - num43)
    elif op4 =="*" and op5 =="+" and op6 == "/":
        print(num13 * num23 + num33 / num43)
    elif op4 =="*" and op5 =="+" and op6 == "*":
        print(num13 * num23 + num33 * num43)
    elif op4 =="*" and op5 =="-" and op6 == "+":
        print(num13 * num23 - num33 + num43)
    elif op4 =="*" and op5 =="-" and op6 == "-":
        print(num13 * num23 - num33 - num43)
    elif op4 =="*" and op5 =="-" and op6 == "/":
        print(num13 * num23 - num33 / num43)
    elif op4 =="*" and op5 =="-" and op6 == "*":
        print(num13 * num23 - num33 * num43)
    elif op4 =="+" and op5 =="/" and op6 == "+":
        print(num13 + num23 / num33 + num43)
    elif op4 =="+" and op5 =="/" and op6 == "-":
        print(num13 + num23 + num33 - num43)
    elif op4 =="+" and op5 =="/" and op6 == "/":
        print(num13 + num23 / num33 / num43)
    elif op4 =="+" and op5 =="/" and op6 == "*":
        print(num13 + num23 / num33 * num43)
    elif op4 =="+" and op5 =="*" and op6 == "+":
        print(num13 + num23 * num33 + num43)
    elif op4 =="+" and op5 =="*" and op6 == "-":
        print(num13 + num23 * num33 - num43)
    elif op4 =="+" and op5 =="*" and op6 == "/":
        print(num13 + num23 - num33 / num43)
    elif op4 =="+" and op5 =="*" and op6 == "*":
        print(num13 + num23 - num33 * num43)
    elif op4 =="-" and op5 =="/" and op6 == "+":
        print(num13 - num23 / num33 + num43)
    elif op4 =="-" and op5 =="/" and op6 == "-":
        print(num13 - num23 / num33 - num43)
    elif op4 =="-" and op5 =="/" and op6 == "/":
        print(num13 - num23 / num33 / num43)
    elif op4 =="-" and op5 =="/" and op6 == "*":
        print(num13 - num23 / num33 * num43)
    elif op4 =="-" and op5 =="*" and op6 == "+":
        print(num13 - num23 * num33 + num43)
    elif op4 =="-" and op5 =="*" and op6 == "-":
        print(num13 - num23 * num33 - num43)
    elif op4 =="-" and op5 =="*" and op6 == "/":
        print(num13 - num23 * num33 / num43)
    elif op4 =="-" and op5 =="*" and op6 == "*":
        print(num13 - num23 * num33 * num43)
    elif op4 =="/" and op5 =="/" and op6 == "+":
        print(num13 / num23 / num33 + num43)
    elif op4 =="/" and op5 =="/" and op6 == "-":
        print(num13 / num23 / num33 - num43)
    elif op4 =="/" and op5 =="/" and op6 == "/":
        print(num13 / num23 / num33 / num43)
    elif op4 =="/" and op5 =="/" and op6 == "*":
        print(num13 / num23 / num33 * num43)
    elif op4 =="/" and op5 =="*" and op6 == "+":
        print(num13 / num23 * num33 + num43)
    elif op4 =="/" and op5 =="*" and op6 == "-":
        print(num13 / num23 * num33 - num43)
    elif op4 =="/" and op5 =="*" and op6 == "/":
        print(num13 / num23 - num33 / num43)
    elif op4 =="/" and op5 =="*" and op6 == "*":
        print(num13 / num23 * num33 * num43)
    elif op4 =="*" and op5 =="/" and op6 == "+":
        print(num13 * num23 / num33 + num43)
    elif op4 =="*" and op5 =="/" and op6 == "-":
        print(num13 * num23 / num33 - num43)
    elif op4 =="*" and op5 =="/" and op6 == "/":
        print(num13 * num23 / num33 / num43)
    elif op4 =="*" and op5 =="/" and op6 == "*":
        print(num13 * num23 / num33 * num43)
    elif op4 =="*" and op5 =="*" and op6 == "+":
        print(num13 * num23 * num33 + num43)
    elif op4 =="*" and op5 =="*" and op6 == "-":
        print(num13 * num23 * num33 - num43)
    elif op4 =="*" and op5 =="*" and op6 == "/":
        print(num13 * num23 * num33 / num43)
    elif op4 =="*" and op5 =="*" and op6 == "*":
        print(num13 * num23 * num33 * num43)

    
cont = input("Press Enter to continue: ")


while cont <= "":
    option = input("\nChoose ammount of variables (2/3/4): ")

    if option == "2":
        num1 = float(input("\nEnter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
            print("Invalid operator. Please use +, -, /, or *")

    if option == "3":
        num12 = float(input("\nEnter first number: "))
        op2 = input("Enter operator: ")
        num22 = float(input("Enter second number: "))
        op3 = input("Enter second operator: ")
        num32 = float(input("Enter third number: "))

        if op2 and op3 == "+":
            print(num12 + num22 + num32)
        elif op2 == "+" and op3 == "-":
            print(num12 + num22 - num32)
        elif op2 == "+" and op3 == "*":
            print(num12 + num22 * num32)
        elif op2 == "+" and op3 == "/":
            print(num12 + num22 / num32)
        elif op2 == "-" and op3 == "-":
            print(num12 - num22 - num32)
        elif op2 == "-" and op3 == "+":
            print(num12 - num22 + num32)
        elif op2 == "-" and op3 == "*":
            print(num12 - num22 * num32)
        elif op2 == "-" and op3 == "/":
            print(num12 - num22 / num32)
        elif op2 == "/" and op3 == "/":
            print(num12 / num22 / num32)
        elif op2 == "/" and op3 == "+":
            print(num12 / num22 + num32)
        elif op2 == "/" and op3 == "-":
            print(num12 / num22 - num32)
        elif op2 == "/" and op3 == "*":
            print(num12 / num22 * num32)
        elif op2 == "*" and op3 == "*":
            print(num12 * num22 * num32)
        elif op2 == "*" and op3 == "+":
            print(num12 * num22 + num32)
        elif op2 == "*" and op3 == "-":
            print(num12 * num22 - num32)
        elif op2 == "*" and op3 == "/":
            print(num12 * num22 / num32)

    if option == "4":
        num13 = float(input("\nEnter first number: "))
        op4 = input("Enter operator: ")
        num23 = float(input("Enter second number: "))
        op5 = input("Enter second operator: ")
        num33 = float(input("Enter third number: "))
        op6 = input("Enter Third operation: ")
        num43 = float(input("Enter fourth number: "))

        if op4 =="+" and op5 =="+" and op6 == "+":
            print(num13 + num23 + num33 + num43)
        elif op4 =="+" and op5 =="+" and op6 == "-":
            print(num13 + num23 + num33 - num43)
        elif op4 =="+" and op5 =="+" and op6 == "/":
            print(num13 + num23 + num33 / num43)
        elif op4 =="+" and op5 =="+" and op6 == "*":
            print(num13 + num23 + num33 * num43)
        elif op4 =="+" and op5 =="-" and op6 == "+":
            print(num13 + num23 - num33 + num43)
        elif op4 =="+" and op5 =="-" and op6 == "-":
            print(num13 + num23 - num33 - num43)
        elif op4 =="+" and op5 =="-" and op6 == "/":
            print(num13 + num23 - num33 / num43)
        elif op4 =="+" and op5 =="-" and op6 == "*":
            print(num13 + num23 - num33 * num43)
        elif op4 =="-" and op5 =="+" and op6 == "+":
            print(num13 - num23 + num33 + num43)
        elif op4 =="-" and op5 =="+" and op6 == "-":
            print(num13 - num23 + num33 - num43)
        elif op4 =="-" and op5 =="+" and op6 == "/":
            print(num13 - num23 + num33 / num43)
        elif op4 =="-" and op5 =="+" and op6 == "*":
            print(num13 - num23 + num33 * num43)
        elif op4 =="-" and op5 =="-" and op6 == "+":
            print(num13 - num23 - num33 + num43)
        elif op4 =="-" and op5 =="-" and op6 == "-":
            print(num13 - num23 - num33 - num43)
        elif op4 =="-" and op5 =="-" and op6 == "/":
            print(num13 - num23 - num33 / num43)
        elif op4 =="-" and op5 =="-" and op6 == "*":
            print(num13 - num23 - num33 * num43)
        elif op4 =="/" and op5 =="+" and op6 == "+":
            print(num13 / num23 + num33 + num43)
        elif op4 =="/" and op5 =="+" and op6 == "-":
            print(num13 / num23 + num33 - num43)
        elif op4 =="/" and op5 =="+" and op6 == "/":
            print(num13 / num23 + num33 / num43)
        elif op4 =="/" and op5 =="+" and op6 == "*":
            print(num13 / num23 + num33 * num43)
        elif op4 =="/" and op5 =="-" and op6 == "+":
            print(num13 / num23 - num33 + num43)
        elif op4 =="/" and op5 =="-" and op6 == "-":
            print(num13 / num23 - num33 - num43)
        elif op4 =="/" and op5 =="-" and op6 == "/":
            print(num13 / num23 - num33 / num43)
        elif op4 =="/" and op5 =="-" and op6 == "*":
            print(num13 / num23 - num33 * num43)
        elif op4 =="*" and op5 =="+" and op6 == "+":
            print(num13 * num23 + num33 + num43)
        elif op4 =="*" and op5 =="+" and op6 == "-":
            print(num13 * num23 + num33 - num43)
        elif op4 =="*" and op5 =="+" and op6 == "/":
            print(num13 * num23 + num33 / num43)
        elif op4 =="*" and op5 =="+" and op6 == "*":
            print(num13 * num23 + num33 * num43)
        elif op4 =="*" and op5 =="-" and op6 == "+":
            print(num13 * num23 - num33 + num43)
        elif op4 =="*" and op5 =="-" and op6 == "-":
            print(num13 * num23 - num33 - num43)
        elif op4 =="*" and op5 =="-" and op6 == "/":
            print(num13 * num23 - num33 / num43)
        elif op4 =="*" and op5 =="-" and op6 == "*":
            print(num13 * num23 - num33 * num43)
        elif op4 =="+" and op5 =="/" and op6 == "+":
            print(num13 + num23 / num33 + num43)
        elif op4 =="+" and op5 =="/" and op6 == "-":
            print(num13 + num23 + num33 - num43)
        elif op4 =="+" and op5 =="/" and op6 == "/":
            print(num13 + num23 / num33 / num43)
        elif op4 =="+" and op5 =="/" and op6 == "*":
            print(num13 + num23 / num33 * num43)
        elif op4 =="+" and op5 =="*" and op6 == "+":
            print(num13 + num23 * num33 + num43)
        elif op4 =="+" and op5 =="*" and op6 == "-":
            print(num13 + num23 * num33 - num43)
        elif op4 =="+" and op5 =="*" and op6 == "/":
            print(num13 + num23 - num33 / num43)
        elif op4 =="+" and op5 =="*" and op6 == "*":
            print(num13 + num23 - num33 * num43)
        elif op4 =="-" and op5 =="/" and op6 == "+":
            print(num13 - num23 / num33 + num43)
        elif op4 =="-" and op5 =="/" and op6 == "-":
            print(num13 - num23 / num33 - num43)
        elif op4 =="-" and op5 =="/" and op6 == "/":
            print(num13 - num23 / num33 / num43)
        elif op4 =="-" and op5 =="/" and op6 == "*":
            print(num13 - num23 / num33 * num43)
        elif op4 =="-" and op5 =="*" and op6 == "+":
            print(num13 - num23 * num33 + num43)
        elif op4 =="-" and op5 =="*" and op6 == "-":
            print(num13 - num23 * num33 - num43)
        elif op4 =="-" and op5 =="*" and op6 == "/":
            print(num13 - num23 * num33 / num43)
        elif op4 =="-" and op5 =="*" and op6 == "*":
            print(num13 - num23 * num33 * num43)
        elif op4 =="/" and op5 =="/" and op6 == "+":
            print(num13 / num23 / num33 + num43)
        elif op4 =="/" and op5 =="/" and op6 == "-":
            print(num13 / num23 / num33 - num43)
        elif op4 =="/" and op5 =="/" and op6 == "/":
            print(num13 / num23 / num33 / num43)
        elif op4 =="/" and op5 =="/" and op6 == "*":
            print(num13 / num23 / num33 * num43)
        elif op4 =="/" and op5 =="*" and op6 == "+":
            print(num13 / num23 * num33 + num43)
        elif op4 =="/" and op5 =="*" and op6 == "-":
            print(num13 / num23 * num33 - num43)
        elif op4 =="/" and op5 =="*" and op6 == "/":
            print(num13 / num23 - num33 / num43)
        elif op4 =="/" and op5 =="*" and op6 == "*":
            print(num13 / num23 * num33 * num43)
        elif op4 =="*" and op5 =="/" and op6 == "+":
            print(num13 * num23 / num33 + num43)
        elif op4 =="*" and op5 =="/" and op6 == "-":
            print(num13 * num23 / num33 - num43)
        elif op4 =="*" and op5 =="/" and op6 == "/":
            print(num13 * num23 / num33 / num43)
        elif op4 =="*" and op5 =="/" and op6 == "*":
            print(num13 * num23 / num33 * num43)
        elif op4 =="*" and op5 =="*" and op6 == "+":
            print(num13 * num23 * num33 + num43)
        elif op4 =="*" and op5 =="*" and op6 == "-":
            print(num13 * num23 * num33 - num43)
        elif op4 =="*" and op5 =="*" and op6 == "/":
            print(num13 * num23 * num33 / num43)
        elif op4 =="*" and op5 =="*" and op6 == "*":
            print(num13 * num23 * num33 * num43)

    
cont = input("Press Enter to continue: ")