#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:21:19 2019

@author: Bowton
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def getArea(): #gets user input for the length of the wind farm
               #then calculates the area and returns length and area
    length = input('What is the length of the wind farm in km?')
    length = float(length)#makes sure length isn't a string
    length = length * 1000 #makes length in meters
    area = (length**2)#our area is a grid (could be adapted to different shapes later on) 
    return area, length

def getSweptArea():#gets user input for swept area, same as function above
    sweptArea = input('What is the swept area of the wind turbine in meters squared?')
    sweptArea = float(sweptArea)
    return sweptArea

def getRotorDiameter(sweptArea):#calculates the rotor diameter based on the A = pi*r^2
    diameter = 2*math.sqrt(sweptArea/math.pi)
    return diameter

def getMaxTurbines(diameter,length):#gets maximum number of turbines that will fit in the wind farm 
    diameter = round(diameter)#rounds the diameter
    maxTurbines = (length / (7*diameter))**2#divides the length of the farm by 7 diameters of the wind turbine
    maxTurbines = math.floor(maxTurbines)#rounds down to nearest int because you can't go over this amount of turbines
    return maxTurbines

def getTurbineCoordinates(maxTurbines,diameter,length):#gets the coordinates of the turbines
    xCoordinates = np.zeros(maxTurbines)#array of zeros, length is max number of turbines because we need the locations of all of them, for x values
    yCoordinates = np.zeros(maxTurbines)#this array is for the y values 
    x = 0
    y = 7.5*diameter #makes sure it isn't too close to the start in case there are obstacles right on the edge of the wind farm that must be avoided
    i = 0#counter
    while y < length: #makes sure it doesn't go out of bounds based on the length of the wind farm
        x = 7.5*diameter
        while x < (length): #adds values to their respective arrays incrementally
            
            xCoordinates[i] = x
            yCoordinates[i] = y
            x = x + 7.5*diameter
            i = i + 1
        y = y + 7.5*diameter
    return xCoordinates, yCoordinates

def graphCoordinateList(xCoordinates,yCoordinates,diameter,length):#graphs the arrays of coordinates
    j = 0
    totalTurbines = 0#number of turbines that are not at location (0,0)
    while (xCoordinates[j] != 0):#this gets the number of turbines that are not at location (0,0) and graphs them
        plt.plot(xCoordinates[j], yCoordinates[j], "b.")
        totalTurbines = totalTurbines + 1
        j = j+1 #increments
    plt.xlim(0, length+(7.5*diameter))#setting x limit of the graph
    plt.ylim(0, length+(7.5*diameter))#setting y limit of the graph
    plt.xlabel('xCoordinates')
    plt.ylabel('yCoordinates')
    plt.show()
    return totalTurbines

def totalPowerOutput(sweptArea, totalTurbines):#calculates the total power output of the wind farm
    totalPower =0
    totalPower = (0.5*(sweptArea)*(1728*1.225))/1000
    totalPower = (totalPower*totalTurbines)/1000
    print("The total power output of this wind farm is " + str(totalPower) + " Mega Watts")
    return totalPower