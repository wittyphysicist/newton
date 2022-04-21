#!/bin/python
# Project ID        : S12
# Project Title     : Root Finding
# Name              : Nazım Ege
# Surname           : Özmeral
# Version           : 3.6.3
# History
# Date 1: (I thought) I completed the code work.
# Date 2: Sinan Hoca has warned me that I needed to think a way to solve the problem for comparing a float to 0(zero). I tried to think the solution yet I couldn't find it for now.
# Date 3: I set a limit for comparing the equality of two floats with epsilon method


# I needed the math library in order to square the term b^2-4ac.
import math

def find_roots(a,b,c):
    gamma = -b/(2*a)
    delta = b**2 - 4*a*c
    if delta > 0:
        x_1 = gamma + math.sqrt(delta)/(2*a)
        x_2 = gamma - math.sqrt(delta)/(2*a)
        print("The roots of your quadratic polynomial are real and distinct:\n" + str(x_1) + "\n" + str(x_2))
    elif delta < 0:
        print("The roots of your quadratic polynomial are complex:\n" + str(gamma),"+","i*" + str(math.sqrt(-delta)) + "\n" + str(gamma),"-","i*" + str(math.sqrt(-delta)))
    else:
        x = gamma
        print("The roots of your quadratic polynomial are real and equal:\n" + str(x))

a = input("Enter three floats/integers by seperating with comma: ").split(',')

# This part is important because for the algorithm to work the number of floats/integers must be 3 and the first float/integers must be non-zero.
if len(a) == 3 and float(a[0]) != 0:
    find_roots(float(a[0]),float(a[1]),float(a[2]))
elif float(a[0]) == 0:
    print("Error: The factor of x^2 cannot be 0")
else:
    print("Error: You must enter three floats/integers")

