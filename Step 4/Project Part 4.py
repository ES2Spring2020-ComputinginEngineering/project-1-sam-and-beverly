# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:27:16 2020

@author: sschr
"""
import numpy as np
def get_data(pendulum):
    counter_array=0
    counter_index=0
    pendulum_file=open(pendulum)
    for line in pendulum_file:
        counter_array=counter_array+1
    data=np.zeros([counter_array, 4])
    for line in pendulum_file:
        line=line.replace('(','')
        line=line.replace(')','')
        line=line.replace(',','')
        line=line.split()
        for i in range(4):
            value=float(line(i))
            data[counter_index, i-1]=value
        counter_index=counter_index+1
    return data
pendulum_25=get_data('Pendulum Data 25cm.txt')
print(pendulum_25)
#def get_data(pendulum):
    #pendulum_file=open(pendulum)
    #pendulum_data=np.loadtxt(pendulum_file)
    #return pendulum_data
#pendulum_25=get_data('Pendulum Data 25cm.txt')
#pendulum_30=get_data('Pendulum Data 30cm.txt')
#pendulum_37=get_data('Pendulum data 37cm.txt')
#pendulum_40=get_data('Pendulum data 40cm.txt')
#Pendulum_46=get_data('Pendulum Data 46cm.txt')
    