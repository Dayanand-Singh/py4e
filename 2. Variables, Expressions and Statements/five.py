# Write a program which prompts the user for a 'Celsius temperature', convert the temperature  
# to Fahrenheit, and print out the converted temperature

# to convert Celsius -> Fahrenheit
#       T('f)= T('c) * 9/5 + 32
#       T('f)= T('c) * 1.8 + 32

#celsius = float(input("Enter temperature in Celsius: "))
#fahrenheit = (celsius*1.8)+32
#print(fahrenheit, "Fahrenheit")

# todo - if user enter text
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit, "Fahrenheit")

except:
    print("Please Enter a number")