# todo Exercise 6.  Rewrite your pay computation with time-and-a-half for overtime and create
#       a function called 'computepay' which takes two parameters (hours and rate).

def computepay(h,r):
    "function for compute pay"
    if h>40:
        p= 40*r + (h-40)*1.5*r
    else:
        p = 40*r
    return p

pay=computepay(45,10)
print(pay)
print(computepay(45,10))
