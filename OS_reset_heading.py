# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:05:44 2020

@author: Joris Ravenhorst
"""

import numpy as np
from numpy import math


# reset heading using xyz rotmat decomposition
def reset_heading(sensor,freq,delay, Mat11,Mat21,Mat31,Mat12,Mat22,Mat32,Mat13,Mat23,Mat33):
    if sensor == 'Xsens':
        rotmat = [[Mat11[0],Mat12[0],Mat13[0]],[Mat21[0],Mat22[0],Mat23[0]],[Mat31[0],Mat32[0],Mat33[0]]]    
    if sensor == 'Vicon':
        rotmat = [[Mat11[delay*freq],Mat12[delay*freq],Mat13[delay*freq]],[Mat21[delay*freq],Mat22[delay*freq],Mat23[delay*freq]],[Mat31[delay*freq],Mat32[delay*freq],Mat33[delay*freq]]] 
    
    
    # decomposition
    yaw = math.atan2(-rotmat[0][1],rotmat[0][0])
    print('   yaw correction = {} [rad]'.format(-yaw))
    
    Ryaw_reset = [[math.cos(-yaw), -math.sin(-yaw), 0], [math.sin(-yaw), math.cos(-yaw), 0], [0, 0, 1]]
    
    length = len(Mat11)
    Mat11new,Mat21new,Mat31new,Mat12new,Mat22new,Mat32new,Mat13new,Mat23new,Mat33new = [0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length
    
    
    count = 0
    for x in Mat11:
        rotmat = [[Mat11[count],Mat12[count],Mat13[count]],[Mat21[count],Mat22[count],Mat23[count]],[Mat31[count],Mat32[count],Mat33[count]]]
        rotmat_new = np.dot(Ryaw_reset,rotmat)
        Mat11new[count] = rotmat_new[0][0]
        Mat12new[count] = rotmat_new[0][1]
        Mat13new[count] = rotmat_new[0][2]
        Mat21new[count] = rotmat_new[1][0]
        Mat22new[count] = rotmat_new[1][1]
        Mat23new[count] = rotmat_new[1][2]
        Mat31new[count] = rotmat_new[2][0]
        Mat32new[count] = rotmat_new[2][1]
        Mat33new[count] = rotmat_new[2][2]
        count += 1
        
    
    
    
    return(Mat11new,Mat21new,Mat31new,Mat12new,Mat22new,Mat32new,Mat13new,Mat23new,Mat33new)