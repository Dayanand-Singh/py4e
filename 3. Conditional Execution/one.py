# todo  Exercise: 1  Rewrite your pay computation to give the employee (1.5) times the hourly rate
#  for hours worked above 40h.
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours<=40:
    pay = rate*hours
    print(pay)

else:
    pay = 40*rate + (hours-40)*1.5*rate
    print(pay)

