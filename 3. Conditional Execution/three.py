#todo Exercise 3: Write a program to prompt for score b/w 0.0  and 1.0. If the score is out of range
#       print an Error message. If the score is b/w 0.0 and 1.0, print a grade using the following table
#       score               Grade
#       >= 0.9              A
#       >= 0.8              B
#       >= 0.7              C
#       >= 0.6              D
#       <  0.6              F
#

try:
    score = float(input("Enter Score: "))
    if score >= 0.9 and score < 1.0:
        print("A")
    elif score >= 0.8 and score < 1.0:
        print("B")
    elif score >= 0.7 and score < 1.0:
        print("C")
    elif score >= 0.6 and score < 1.0:
        print("D")
    elif score < 0.6 and score > 0.0:
        print("F")
    else:
        print("please enter number b/w (1.0 and 0.0)")

except:
    print("please enter numeric value")

# todo another way
#score= input()
#try:
#    s=float(score)
#except:
#   s = 11
