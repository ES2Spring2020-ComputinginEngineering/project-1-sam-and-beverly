# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:04:29 2020

@author: sschr
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sp

def get_period(dataset, timeset, Length):
    dataset=np.array(dataset)
    timeset=np.array(timeset)
    peak, _ =sp.find_peaks(dataset)
    print(peak)
    plt.plot(timeset[peak], dataset[peak], 'r-')
    plt.title('Peaks '+ str(Length)+'cm')
    plt.tight_layout()
    plt.show()
    period=np.diff(timeset[peak])
    period=np.mean(period)
    return period

def update_system(acc,pos,vel,time1,time2,time1_5,L):
    # position and velocity update below
    dt = time2-time1
    d_t= time2-time1_5
    posNext = 90*math.cos(dt*math.sqrt(9.8/L))
    dp = posNext-pos
    velNext = dp/d_t
    dv = velNext-vel
    accNext = dv/d_t
    return posNext,velNext,accNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

def runsimulation(Length):
    # initial conditions
    pos = [90]
    vel = [0]
    acc = [0]
    time = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    #print_system(time[0],pos[0],vel[0])

    i = 1
    while i < len(time):
        # update position and velocity using previous values and time step
        posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[0],time[i],time[i-1],Length)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        #print_system(time[i],pos[i],vel[i])
        i += 1
        
    Length=Length*100   
    period=get_period(pos,time,Length)
    
    plt.subplot(3,1,1)
    plt.plot(time, pos, 'ro--') 

    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (Degrees)')
    plt.title('Position vs Time '+ str(Length)+'cm')
    plt.xlim((0, 35)) # set x range to -1 to 8
    plt.grid()


    plt.subplot(3,1,2)
    plt.plot(time, vel, 'ro--') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (degrees/s)')
    plt.title('Velocity vs Time '+ str(Length)+'cm')
    plt.xlim((0, 35)) # set x range to -1 to 8
    plt.grid()


    plt.subplot(3,1,3)
    plt.plot(time, acc, 'ro--') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration (degrees/s^2)')
    plt.title('Acceleration vs Time '+ str(Length)+'cm')
    plt.xlim((0, 35)) # set x range to -1 to 8
    plt.grid()
    plt.tight_layout()
    plt.show()
    return period

period_34=runsimulation(.34)
period_43=runsimulation(.43)
period_53=runsimulation(.53)
period_62=runsimulation(.62)
period_72=runsimulation(.72)
print(period_34)
print(period_43)
print(period_53)
print(period_62)
print(period_72)