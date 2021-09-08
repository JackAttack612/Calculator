# Made by JackAttack612
# Version 4.3.5
# To check if you have the latest version visit https://github.com/JackAttack612/Calculator

import time
import tkinter
from playsound import playsound

print("Version 4.3.5")
print("To see latest version visit https://github.com/JackAttack612/Calculator")
print("Loading Calculator...")
time.sleep(5)
print("\nOperations/Info:")
print("+ = addition")
print("- = subtracion")
print("/ = division")
print("* = multiply")
print("** = exponent")
print("// = floor division")
print("% = modulus")
print("< = less than")
print("> = greater than")
print("This calculator uses order of operation")
print("To get the list of Operators later type \"Operations\" ")
print("_______________________")

def admin_panel():
    name = input("What is your name:").lower()
    if name == 'nuke':
        print("Okay, nuking")
        playsound(r'C:\Users\jetfl\Coding\Calculator-main\Audio\nuke.mp3')
        quit()
    elif name == 'audrey':
        audrey()
    else:
        print("Cool don't care")
        print("You wasted your time getting here it does nothing")
        calculator()

def audrey():
    audreyq = input("\nAre you audrey? DONT LIE (Yes or No): ").lower()
    if audreyq == 'yes':
        password = input("Enter your password: ")
        if password == 'Crossfield25':
            escape = input("click enter to play a song or type quit to exit: ").lower()
            if escape == 'quit':
                calculator()
            else:
                print("\nPlaying loverboy by A-Wall")
                playsound(r'C:\Users\jetfl\Coding\Calculator-main\Audio\audrey.mp3')
                calculator()
        else:
            print("\nIncorrect Password")
            time.sleep(2)
            calculator()
    elif audreyq == 'no':
        print("Well then why are you here???")
        time.sleep(3)
        calculator()
    else:
        print("You didn't say yes or no.")
        calculator()

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
            print("< = less than")
            print("> = greater than")
            print("_______________________")
            calculator()
        elif calc == 'admin':
            admin1 = input("\nEnter Password:")
            if admin1 == 'Madjack612!':
                admin_panel()
            else:
                print("Password Incorrect")
                calculator()
        elif calc == "audrey":
                audrey()
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
        print("Error: Could not complete calculation.\nMost likely due to an invalid operation; Refer to the top of the page to see all valid operations\nor type \"Operations\"")
        print("Error type: SyntaxError")
        print("!!!")
        time.sleep(3)
        calculator()

calculator()