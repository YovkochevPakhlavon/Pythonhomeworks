#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:00:35 2024

@author: pahlavon
"""
#--------------------------------------------------------------------------------

from matplotlib import pyplot as plt
import numpy as np
import os
import math
#from tkinter import Tk
#from tkinter import filedialog

#--------------------------------------------------------------------------------

#Tk().withdraw() # 

#myfile = filedialog.askopenfilename(title = 'Select a *.txt-file containing Time-/Frequency coordinates of type II burst') # show an "Open" dialog box and return file

myfile = '/Users/pahlavon/Desktop/140907/Lasco.txt' # for testing only to avoid too many clicks...
fnam = os.path.basename(myfile) # extract filename only in case it contains also the path

"""
#Date      Time       Freq(MHz)  Xpix  Ypix
2010-06-13T05:37:14    298.1746   203   291
2010-06-13T05:38:20    222.2898   244   266
etc.
"""

MyTime    = [] # reserve a list for time
Height = [] # reserve a list for column Frequency

f = open(myfile)
i = 0  # counts the lines in the file   

for row in f:
    i = i + 1
    if (i > 1):  # skip header data, e.g. title
        Rows = repr(row) # force any input to become a printable string 
        Rows = Rows.strip()  # get rid of '\n' and similar control characters
        Row  = Rows.split() # split string into separate elements -> kind of vector or list
        dt = Row[0] # Date-/Time-string is the first element of the list 'Line'

        cm = dt[ 1: 2]
        if (cm == "2"):
            yy = dt[ 1: 5] # extract year
            MM = dt[ 6: 8] # extract month
            dd = dt[ 9:11] # extract day
            hh = dt[12:14] # get hours
            mm = dt[15:17] # get minutes
            ss = dt[18:20] # get seconds
            tx = float(hh) + float(mm)/60.0 + float(ss)/3600.0 # create decimal hour
#            tx = float(hh) + float(mm)*60.+ float(ss)/3600.0 # create decimal hour
            MyTime.append(tx) # fill up the list
            
            f0 = Row[1] # gte frequency out of the table
            Height.append(float(f0)) # Fill a list with frequency

f.close()

#--------------------------------------------------------------------------------



plt.figure(figsize=(10,7))
tmin = np.min(MyTime)
tx = (MyTime - tmin)*60.0 # convert absolute into relative time
plt.plot(tx[:20],Height[:20],'o',color='red', label='Type II data') #o,+,
plt.plot(tx[20:], Height[20:], 'X', color='blue', label='LASCO data')
plt.plot(11., 1.70, 'X', color='black', label='SDO data')
plt.plot(0., 1.23, 'X', color='black')
#plt.xlim(0,11.5)
#plt.ylim(1,2)
plt.title(fnam,fontsize=16)
plt.xlabel("Relative Time [min]",size=18)
plt.ylabel("Height [Rs]",size=18)
plt.title("SDO + Type II: " + yy + '-' + MM + '-' + dd, size=18)
plt.grid(True) # an option
plt.tick_params(labelsize=30)


#plt.yscale('log') # this is an option to checkout


# Uncomment lines below to perform the linear fitting. 

#tx = np.insert(tx, 29, 0.)
#tx = np.insert(tx, 30, 12.)
#Height=np.insert(Height, 29, 1.23)
#Height=np.insert(Height, 30, 1.70)
m, b = np.polyfit(tx, Height, 1)
speed=round(m*6.96e5/60.) # 1 solar radii = 6.96e5 km
plt.plot(tx, m*tx+b, 'k', label= 'linear fit - Type II')
plt.annotate('Speed = '+str(speed)+' km/s',xy=(300,10),fontsize=20)
#plt.legend()

# For advanced students: (1) obtain the CME onset by assuming the CME starts from Height=1 Rs.

# For advanced students: (2) obtain the CME acceleration (deceleration) using 2nd-order fitting

#projection effect

projected_speed = m / math.cos(math.pi / 4.4)
height = projected_speed*tx[20:]+b
plt.plot(tx[20:], height, 'X', color='green', label='projected LASCO data')
plt.plot(tx[20:],height,'--k',label='projected linear fit')
newspeed = round(projected_speed*6.96e5/60.)
plt.annotate('Speed = '+str(newspeed)+' km/s',xy=(0,15),fontsize=20)


# Assuming tx and Height are your data arrays

# Perform quadratic fit (2nd degree polynomial)
#coefficients = np.polyfit(tx[:20], Height[:20], 2)

# Extract the coefficients
#a, b, c = coefficients

# Calculate the fitted quadratic curve
#fitted_curve = a * tx[:20]**2 + b * tx[:20] + c

# Calculate speed as the first derivative of the quadratic fit
#speed = 2 * a * tx[:28] + b
#print("2*a*t+b")

# Calculate acceleration as the second derivative of the quadratic fit
#acceleration = 2 * a  # Since the second derivative is constant for a quadratic fit

# Convert speed to km/s (assuming speed is in solar radii per minute)
#speed_km_s = speed * 6.96e5 / 60.

# Convert acceleration to km/s^2
#acceleration_km_s2 = acceleration * 6.96e5 / 3600.  # Divide by 3600 to convert from per minute squared to per second squared

# Plot the original data points
#plt.plot(tx, Height, 'yo', label='Data')  # Yellow circles for data points

# Plot the fitted quadratic curve
#newtime = np.array([6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11])
#height = a * newtime**2 + b * newtime + c
#plt.plot(newtime, height, '--k', label='Shock extrapolation')
#plt.plot(tx[:20], fitted_curve, 'k', label='Quadratic fit')  # Black line for the fit

#plt.annotate(f'Acceleration = {round(acceleration_km_s2, 2)} km/s²',xy=(5, 1.2), fontsize=24)
plt.legend()
plt.show()

#plt.savefig('CMEHT_' + fnam + '.png')
#plt.savefig('CMEHT_' + fnam + '.pdf')
#plt.savefig('CMEHT_' + fnam + '.eps')

# other formats may be edded
#--------------------------------------------------------------------------------
# Here you analysis + plotting may start ..
#--------------------------------------------------------------------------------
