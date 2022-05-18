#
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Darwin White
# Section:      563
# Assignment:   Lab 10b Activity 2
# Date:         14 November 2021
#

import csv
import numpy as np
import matplotlib.pyplot as plt

#Opening the CSV file for reading
with open("CLLWeatherData.csv", "r") as wData:
    weatherRead = csv.reader(wData, delimiter = ",")

    #Initializing needed variables
    iterator = 0
    numDates = np.array([], dtype = int)
    avgTemps = np.array([], dtype = int)
    windSpeeds = np.array([], dtype = float) 
    precipitations = np.array([], dtype = float)
    minTemps = np.array([], dtype = int)
    maxTemps = np.array([], dtype = int)
    
    #Variables for the 4th graph of month calculations
    sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mins = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    
    firstRow = True
    
    #Reading in the data
    for row in weatherRead:
    
        #Skipping the first line with names
        if (firstRow):
            firstRow = False
            continue
    
        #Getting the average temperatures
        dailyTemp = int(row[3])
        avgTemps = np.append(avgTemps, dailyTemp)

        #Getting the wind speeds
        dailyWindSpeed = float(row[1])
        windSpeeds = np.append(windSpeeds, dailyWindSpeed)
        
        #Getting the daily precipitations
        dailyPrecipitation = float(row[2])
        if (dailyPrecipitation > 0):
            precipitations = np.append(precipitations, dailyPrecipitation)
            
        #Getting the minimum temperatures
        dailyMinTemp = int(row[5])
        minTemps = np.append(minTemps, dailyMinTemp)
        
        #Getting the maximum temperatures
        dailyMaxTemp = int(row[4])
        maxTemps = np.append(maxTemps, dailyMaxTemp)
        
        #Getting the average temperature for each month across all 3 years
        # as well as the maximum and minimum temperatures. Each if statement
        # filters so only the data from that corresponding month is grabbed.
        # Sum list has the sums of the average temperatures. Maxes are the 
        # highest temps for each month. Mins are the lowest
        date = row[0].split("/")
        if (int(date[0]) == 1):
            sums[0] += int(row[3])
            counts[0] += 1
            if (int(row[4]) > maxes[0]):
                maxes[0] = int(row[4])
            if (int(row[5]) < mins[0]):
                mins[0] = int(row[5])
        
        if (int(date[0]) == 2):
            sums[1] += int(row[3])
            counts[1] += 1
            if (int(row[4]) > maxes[1]):
                maxes[1] = int(row[4])
            if (int(row[5]) < mins[1]):
                mins[1] = int(row[5])
        
        if (int(date[0]) == 3):
            sums[2] += int(row[3])
            counts[2] += 1
            if (int(row[4]) > maxes[2]):
                maxes[2] = int(row[4])
            if (int(row[5]) < mins[2]):
                mins[2] = int(row[5])
        
        if (int(date[0]) == 4):
            sums[3] += int(row[3])
            counts[3] += 1
            if (int(row[4]) > maxes[3]):
                maxes[3] = int(row[4])
            if (int(row[5]) < mins[3]):
                mins[3] = int(row[5])
        
        if (int(date[0]) == 5):
            sums[4] += int(row[3])
            counts[4] += 1
            if (int(row[4]) > maxes[4]):
                maxes[4] = int(row[4])
            if (int(row[5]) < mins[4]):
                mins[4] = int(row[5])
        
        if (int(date[0]) == 6):
            sums[5] += int(row[3])
            counts[5] += 1
            if (int(row[4]) > maxes[5]):
                maxes[5] = int(row[4])
            if (int(row[5]) < mins[5]):
                mins[5] = int(row[5])
        
        if (int(date[0]) == 7):
            sums[6] += int(row[3])
            counts[6] += 1
            if (int(row[4]) > maxes[6]):
                maxes[6] = int(row[4])
            if (int(row[5]) < mins[6]):
                mins[6] = int(row[5])
        
        if (int(date[0]) == 8):
            sums[7] += int(row[3])
            counts[7] += 1
            if (int(row[4]) > maxes[7]):
                maxes[7] = int(row[4])
            if (int(row[5]) < mins[7]):
                mins[7] = int(row[5])
        
        if (int(date[0]) == 9):
            sums[8] += int(row[3])
            counts[8] += 1
            if (int(row[4]) > maxes[8]):
                maxes[8] = int(row[4])
            if (int(row[5]) < mins[8]):
                mins[8] = int(row[5])
        
        if (int(date[0]) == 10):
            sums[9] += int(row[3])
            counts[9] += 1
            if (int(row[4]) > maxes[9]):
                maxes[9] = int(row[4])
            if (int(row[5]) < mins[9]):
                mins[9] = int(row[5])
        
        if (int(date[0]) == 11):
            sums[10] += int(row[3])
            counts[10] += 1
            if (int(row[4]) > maxes[10]):
                maxes[10] = int(row[4])
            if (int(row[5]) < mins[10]):
                mins[10] = int(row[5])
        
        if (int(date[0]) == 12):
            sums[11] += int(row[3])
            counts[11] += 1
            if (int(row[4]) > maxes[11]):
                maxes[11] = int(row[4])
            if (int(row[5]) < mins[11]):
                mins[11] = int(row[5])
        
        iterator += 1
        numDates = np.append(numDates, iterator)
        
    i = 0
    avgTempMonth = []
    for Sum in sums:
        avgTempMonth.append(Sum / counts[i])
        i += 1

#Plotting the first plot, Average Temperature and Wind Speed for each day
# over the interval on a line graph
plt.figure(1)
plt.suptitle("Average Temperature and Wind Speed")
tempL = plt.plot(numDates, avgTemps, color = "r", label = "Temp avg")
plt.xlabel("Date")
plt.ylabel("Average Temperature, F")
plt.twinx()
windL = plt.plot(numDates, windSpeeds, color = "b", label = "Wind avg")
plt.ylabel("Average Wind Speed, mph")
lines = tempL + windL
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc = "lower left")

#Plotting the second plot, Daily Precipitation in inches for each day over the
# interval represented by a histogram
xRange = 5
nBins = np.linspace(0, xRange, xRange * 10)
plt.figure(2)
plt.suptitle("Histogram of Precipitation")
plt.hist(precipitations, color = "purple", bins = nBins)
plt.xlabel("Precipitation, in")
plt.ylabel("Number of Days")
        
#Plotting the third plot, a scatterplot showing the relationship between
# Wind Speeds and minimum temperature
plt.figure(3)
plt.suptitle("Average Wind Speed vs. Minimum Temperature")
plt.scatter(minTemps, windSpeeds, color = "c", s = 10)
plt.xlabel("Minimum Temperature, F")
plt.ylabel("Average Wind Speed, mph")

#Plotting the fourth plot, a bar chart for each calendar month showing
# the average temperatures for each as well as the high and low temperature
# averages as lines over the interval
x = np.arange(1, 13)
plt.figure(4)
plt.suptitle("Average Temperature by Month")
plt.bar(x, avgTempMonth, color = "y")
plt.plot(x, maxes, color = "r", label = "High T")
plt.plot(x, mins, color = "b", label = "Low T")
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.legend(loc = "upper left")