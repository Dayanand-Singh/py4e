# Write a program to prompt the user for hours and rates per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# i made error in this code 
#hours = int(input("Enter Hours: "))
#rate = int(input("Enter Rate: "))      (2.75, 96.25 are float value enter by user they can't be int)
#pay = hours * rate
#print(pay)


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
print(pay)


