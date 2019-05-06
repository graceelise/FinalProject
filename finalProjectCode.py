#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:33:13 2019

@author: Bowton
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import pylab
from scipy import stats

def readFile():
    csv_file = open('RealWindData2.csv') # opens file
    total_row = sum(1 for row in csv_file)-1 #counts the rows
    csv_file.seek(0) #resets the bouncing ball
    
    csv_reader = csv.reader(csv_file, delimiter=',') #parsing at the commas
    line_count = -1 #index of all data in file
    #creating arrays the same length as our CSV file, filled with zeros
    sweptArea = np.zeros((total_row,))
    power = np.zeros((total_row,))
   
    #traverses the array and replaces the zeros with the actual values of power output and swept area
    for row in csv_reader:
        if line_count == -1:
            #print('Column names are '+ str(row))
            line_count += 1
        else:
            sweptArea[line_count] = float(row[0])
            power[line_count] = float(row[1])
            line_count += 1
            
    csv_file.close()
    
    return (sweptArea, power)


#ideal power output of a wind turbine is 1/2* swept area * wind velocity cubed * air density
def idealPower(sweptArea):
    idealPower = np.array((0.5*sweptArea*1728*1.225)/1000)#1728 is 12m/s wind velocity cubed, 1.225 is air density at sea level
    #print(idealPower)
    return idealPower

def efficiency(idealPower,power):
    efficiency = np.array(power/idealPower)
    #print(efficiency)
    return efficiency

def createTestTurbine():
    turbineSA = random.uniform(1,40000)
    turbineP = random.uniform(1,14000)
    maxP = idealPower(turbineSA)
    while(turbineP > maxP): #This makes sure the random power is not greater than the greatest possible
                            #power output of the turbine based on the ideal power equation
        turbineP = random.uniform(1,14000)
    idealPTurbine = idealPower(turbineSA)
    turbineCOP = turbineP/idealPTurbine
    print("swept area: " + str(turbineSA) + " power output: " + str(turbineP) +  " Ideal power: " + str(idealPTurbine) + " COP: " + str(turbineCOP))
    return turbineSA, turbineP, turbineCOP

def graphData(sweptArea, power, turbineSA, turbineP):
    plt.figure(1)
    plt.plot(sweptArea, power, "r.")
    plt.plot(turbineSA, turbineP, "k.")
    plt.xlabel('Swept Area in m^2')
    plt.ylabel('Power Output in kW')
    plt.show()
    return None

def bestFitSlope(sweptArea,power):
    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(sweptArea,power)
    line = slope*sweptArea+intercept
    plt.plot(sweptArea,power,'ko', sweptArea, line)
    pylab.title('Linear Fit of Swept Area Compared to Power Output')
    plt.xlabel('Swept Area in m^2')
    plt.ylabel('Power Output in kW')
    return None

def efficiencyGraphs(efficiency,sweptArea,power):
    plt.figure()
    plt.subplot()
    plt.plot((sweptArea), (efficiency), "r.")
    plt.xlabel('Swept Area in m^2')
    plt.ylabel('Efficiency Coefficient')
    plt.subplot()
    plt.plot((power), (efficiency), "r.")
    plt.xlabel('Power in Kw')
    plt.ylabel('Efficiency Coefficient')
    plt.show()
    plt.show()
    return None

def bestFitSlopeEfficiency(power,efficiency):
    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(efficiency,power)
    line = slope*efficiency+intercept
    plt.plot(efficiency,power,'ko', efficiency, line)
    pylab.title('Linear Fit of efficiency Compared to Power Output')
    plt.xlabel('Efficiency')
    plt.ylabel('Power Output in kW')
    return None
def efficiencyHistogram(efficiency):
    efficiencyCatagories = np.around(efficiency,1)
    plt.figure(3)
    plt.hist(efficiencyCatagories)
    plt.title("Efficiency Distribution")
    plt.xlabel("Catagories")
    plt.ylabel("Frequency")
    return None
def meanEfficiency(efficiency):
    sumEfficiency = np.sum(efficiency)
    length = np.prod(efficiency.shape)
    meanEfficiency = sumEfficiency/length
    meanEfficiency = round(meanEfficiency,2)
    print("mean efficiency of these wind turbines is " + str(meanEfficiency))
    return meanEfficiency
    