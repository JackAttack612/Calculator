import time

def quit1():
    print("closing in 5 seconds")
    time.sleep(1)
    print("closing in 4 seconds")
    time.sleep(1)
    print("closing in 3 seconds")
    time.sleep(1)
    print("closing in 2 seconds")
    time.sleep(1)
    print("closing in 1 second")
    time.sleep(1)
    print("closing")
    time.sleep(1)
    quit()

print("Operations/Info:")
print("+ = addition")
print("- = subtracion")
print("/ = division")
print("* = multiply")
print("** = exponent")
print("// = floor division")
print("% = modulus")
print("This calculator uses order of operation")
print("To get the list of Operators later type \"Operations\" ")
print("_______________________")

def calculator():
    try:
        calc = input("\nType calculation or type quit: ").lower()

        if calc == 'quit':
            verify = input("\nAre you sure you want to quit? (Yes or No): ").lower()
            if verify == 'no':
                calculator()
            elif verify == 'yes':
                quit1()
            else:
                calculator()
        elif calc == 'operations':
            print("\nOperations/Operators:")
            print("+ = addition")
            print("- = subtracion")
            print("/ = division")
            print("* = multiply")
            print("** = exponent")
            print("// = floor division")
            print("% = modulus")
            print("_______________________")
            time.sleep(3)
            calculator()
        else:
            print("Answer: " + str(eval(calc)))
            calculator()


    except ZeroDivisionError:
        print("\n!!!")
        print("Error: Divided by zero")
        print("Error type: ZeroDivisionError")
        print("!!!")
        time.sleep(3)
        calculator()
    except ValueError:
        print("\n!!!")
        print("Error: Invalid input")
        print("Error type: ValueError")
        print("!!!")
        time.sleep(3)
        calculator()
    except NameError:
        print("\n!!!")
        print("Error: Your calculation has to be numbers")
        print("Error type: NameError")
        print("!!!")
        time.sleep(3)
        calculator()
    except TypeError:
        print("\n!!!")
        print("Error: You tried to use parentheses")
        print("Error type: TypeError")
        print("!!!")
        time.sleep(3)
        calculator()
    except SyntaxError:
        print("\n!!!")
        print("Error: Could not complete calculation.\nMost likely due to an invalid operation; Refer to the top of the page to see all valid operations.")
        print("Error type: SyntaxError")
        print("!!!")
        time.sleep(3)
        calculator()

calculator()