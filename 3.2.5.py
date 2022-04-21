#!/bin/python
# Project ID        : S24
# Project Title     : Planetary Motion
# Name              : Nazım Ege
# Surname           : Özmeral
# Version           : 3.6.3
# History
# Date 1: For now, I just splitted the elements of array to make operation on the positions of the planets
# Date 2: To show the trajectory. I downloaded and learned numpy and matplotlib
# Date 3: After a really hard-working process, I wrote a code that work, yet, to find correct units is a little bit hard
# Date 4: I created a time unit called "Ege" to make G = 1
# Date 5: I changed the places of "if conditions" in order that the user can get the error message as soon as possible
# Date 6: I added a code that creates a file and puts the location values into the file.

import math
import numpy as np
import matplotlib.pyplot as plt

delta_time = 0.001
# G = (6.67408e-11)*((1/299792)**3)*(3600**2) * (1.989e30) # Gravitational Constant in the units (light second)^3*(solar mass)^-1*hour^-2
G = 1 # Gravitational Constant in the units (light minute)^3 * (solar mass)^-1 * Ege^-2, where 1 Ege = 132 hours approximately
number_steps = 100000 #1000000
mS = 1 # The mass of Sun in the solar mass unit. It is 1.989e30 kilogram

print("Suggestion:\n For an eliptic trajectory around the Sun, enter these values:\n Mass of X = 1\n Mass of Y = 0\n Initial position of X = 0.5,0\n Initial velocity of X = 0,1.63\n")

mX = float(input("Enter the mass value of the planet X in the solar mass unit: "))
mY = float(input("Enter the mass value of the planet Y in the solar mass unit: "))

if mX <= 0:
    print("Error: You cannot choose the mass value of the planet X to be non-positive") 
elif mY < 0:
    print("Error: You cannot choose the mass value of the planet Y to be negative") # Yet, i thought it was okay if the mass of the planet Y is zero(0).
else:
    xX_initial,yX_initial = map(float,input("Enter the initial x and y values of the planet X by seperating with comma in the light minute unit: ").split(','))
    if mY == 0:
        xY,yY = 0,0
    else:
        xY,yY = map(float,input("Enter the x and y values of the planet Y by seperating with comma in the light minute unit: ").split(','))

    if xX_initial == 0 and yX_initial == 0:
        print("Error: You cannot choose the planet X to be at the origin") # Yet, i thought it was okay if the planet Y is at the origin.
    elif xX_initial == xY and yX_initial == yY:
        print("Error: The locations of the planets are the same")
    else:
        vxX_initial,vyX_initial = map(float,input("Enter the initial velocity value of the planet X on x and y axis by seperating with comma in the light minute/Ege unit, where 1 Ege = 132 hours: ").split(','))

        # I created arrays for each .. that has the same numbers
        xX = [0]*number_steps
        yX = [0]*number_steps
        vxX = [0]*number_steps
        vyX = [0]*number_steps
        axX = [0]*number_steps
        ayX = [0]*number_steps
        rXY = [0]*number_steps
        rXS = [0]*number_steps
        
        xX[0] = xX_initial
        yX[0] = yX_initial
        
        rXY[0] = math.sqrt((xX[0]-xY)**2 + (yX[0]-yY)**2)
        rXS[0] = math.sqrt((xX[0])**2 + (yX[0])**2)
        rXY3 = rXY[0]**3
        rXS3 = rXS[0]**3

        # I used r^3 term instead of r^2 term since in vector notation, x component of the unit vector is û_x = x/|r|, and y component is û_y = y/|r|
        axX[0] = -G * ((xX[0]*mS/rXS3) + ((xX[0]-xY)*mY/rXY3))
        ayX[0] = -G * ((yX[0]*mS/rXS3) + ((yX[0]-yY)*mY/rXY3))
        
        vxX[0] = vxX_initial + (delta_time/2)*axX[0]
        vyX[0] = vyX_initial + (delta_time/2.0)*ayX[0]
        
        for i in range(1,number_steps):
            xX[i] = xX[i-1] + delta_time*vxX[i-1]
            yX[i] = yX[i-1] + delta_time*vyX[i-1]
            rXY[i] = math.sqrt((xX[i]-xY)**2 + (yX[i]-yY)**2)
            rXS[i] = math.sqrt((xX[i])**2 + (yX[i])**2)
            rXY3 = rXY[i]**3
            rXS3 = rXS[i]**3
            
            axX[i] = -G * ((xX[i]*mS/rXS3) + ((xX[i]-xY)*mY/rXY3))
            ayX[i] = -G * ((yX[i]*mS/rXS3) + ((yX[i]-yY)*mY/rXY3))
            
            vxX[i] = vxX[i-1] + delta_time*axX[i]
            vyX[i] = vyX[i-1] + delta_time*ayX[i]
        
        # I created a file with name "S24.dat" and put the location values of the planet X into it.
        file = open("S24.txt","w")
        for i in range(len(xX)):
            file.write(str(xX[i]) + " " + str(yX[i]) + "\n")
        file.close()
        
        plt.plot(xX,yX,'m-')
        if mY != 0:
            plt.plot(xY,yY,'bo')
            plt.text(xY-0.1,yY-0.1,'The planet Y')
        plt.plot(0,0,'yo')
        plt.grid()
        
        plt.xlabel('x-axis in the light minute unit')
        plt.ylabel('y-axis in the light minute unit')
        plt.title('Trajectory of the planet X around the Sun and the planet Y')
        
        plt.text(0,0,'The Sun')
        
        plt.show()
