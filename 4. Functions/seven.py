# todo Exercise 7.  Rewrite the grade programe from the previous chapter using a function
#       called computegrade that takes a score as its parameter and return a grade as a string


def computegrade(score):
    "A function for compute grage"



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



grade = input("Enter Grades: ")
try:
    g = float(grade)
except:
    g = 11.0

computegrade(g)