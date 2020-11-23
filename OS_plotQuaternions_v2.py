# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:11:48 2020

@author: Joris Ravenhorst
"""

import matplotlib.pyplot as plt

def plotQuats_v2(time_s,Quat_w,Quat_x, Quat_y, Quat_z):
    quats = [0]*len(time_s)
    
    time_s = [float(index) for index in time_s]
    Quat_w = [float(index) for index in Quat_w]
    Quat_x = [float(index) for index in Quat_x]
    Quat_y = [float(index) for index in Quat_y]
    Quat_z = [float(index) for index in Quat_z] 
    for index in range(len(Quat_w)):
        quats[index] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]


      
    plt.figure()
    plt.plot(time_s,quats) #,Quat_x, Quat_y, Quat_z)
    
    plt.ylabel('quaternion')
    plt.xlabel('time [s]')
    plt.legend(['qx','qy','qz','qw'])
    # plt.title()