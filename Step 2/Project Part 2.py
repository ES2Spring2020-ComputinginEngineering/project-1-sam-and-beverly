# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:19:46 2020

@author: sschr
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def period_pendulum(length):
    period_array=[0,0,0,0,0]
    counter=0
    for element in length:
        period=(2*math.pi)*math.sqrt(element/9.8)#in seconds
        period_array[counter]=period
        counter=counter+1
    return period_array
length=[25,30,37,40,46]#in cm
print(period_pendulum(length))

period_array=period_pendulum(length)
np.random.seed(19680801)
x=length
y=period_array
colors='c'
area=10
plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.title("Length vs Period")
plt.xlabel("Length(cm)")
plt.ylabel("Period(s)")
plt.show()