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

print("Operations/Operators:")
print("+ = addition")
print("- = subtracion")
print("/ = division")
print("* = multiply")
print("** = exponent")
print("// = floor division")
print("% = modulus")
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
        else:
            print("Answer: " + str(eval(calc)))
            calculator()


    except ZeroDivisionError:
        print("\nError: Divided by zero")
        print("Error type: ZeroDivisionError")
        time.sleep(3)
        calculator()
    except ValueError:
        print("\nError: Invalid input")
        print("Error type: ValueError")
        time.sleep(3)
        calculator()
    except NameError:
        print("\nError: Your calculation has to be numbers")
        print("Error type: NameError")
        time.sleep(3)
        calculator()
    except TypeError:
        print("\nError: You tried to use parentheses")
        print("Error type: TypeError")
        time.sleep(3)
        calculator()
    except SyntaxError:
        print("\nError: Could not complete calculation. Most likely used an invalid operation; Refer to the top of the page to see all valid operations.")
        print("Error type: SyntaxError")
        time.sleep(3)
        calculator()

calculator()