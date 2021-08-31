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
    time.sleep(2)
    quit()

try:
    print("+ = addition")
    print("- = subtracion")
    print("/ = division")
    print("* = multiply")
    print("** = exponent")
    print("// = floor division")
    print("% = modulus")

    def calculator():
        
        time.sleep(2)

        calc = input("\nType calculation or type quit: ").lower()

        if calc == 'quit':
            verify = input("Are you sure you want to quit? (Yes or No): ").lower()
            if verify == 'no':
                calculator()
            elif verify == 'yes':
                quit1()
            else:
                calculator()
        else:
            print("Answer: " + str(eval(calc)))
            calculator()

    calculator()

except ZeroDivisionError:
    print("\nError: Divided by zero")
    print("Error type: ZeroDivisionError")
    calculator()
except ValueError:
    print("\nInvalid input")
    print("Error type: ValueError")
    calculator()
except NameError:
    print("\nError: Your calculation has to be numbers")
    print("Error type: NameError")
    calculator()
except TypeError():
    print("Error: You tried to use parentheses")
    print("Error type: TypeError")
    calculator()