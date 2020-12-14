# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:50:14 2020

@author: Joris Ravenhorst
"""

import matplotlib.pyplot as plt


def plotQuats(trial_dir_path, trialID):
    with open(trial_dir_path + trialID + '_orientations.sto') as file:
        lines = file.readlines()
        
        time = [line.split()[0] for line in lines[6:]]
        time = [float(x) for x in time]
        
        headers = lines[5].split()
        quats = [0]*len(time)
        
    
        
        for imu in range(1,len(headers)):
            
            plt.figure()
    
            count = 0
            for line in lines[6:]:
                quats[count] = line.split()[imu].split(',')
                for quat in range(len(quats[count])):
                    quats[count][quat] = float(quats[count][quat])
                count += 1
               
            plt.plot(time,quats)
    
            plt.ylabel('quaternion')
            plt.xlabel('time [s]')
            plt.legend(['qx','qy','qz','qw'])
            plt.title(headers[imu])