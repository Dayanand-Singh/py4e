# todo Exercise 2: Rewrite your pay program using try and except so that your program handles
#       non-numeric input gracefully by printing a message and exiting the program.
#       The following shows two executions of the program
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours <= 40:
        pay = rate * hours
        print(pay)

    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
        print(pay)


except:
    print("Error, please enter numeric input")

