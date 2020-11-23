# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:49:39 2020

@author: Joris Ravenhorst
"""

import matplotlib.pyplot as plt


def plotJointangles(trial_dir_path, trialID, angles2plot):
    with open(trial_dir_path + 'ik_' + trialID + '_orientations.mot') as file:
        lines = file.readlines()
        
        time = [line.split()[0] for line in lines[7:]]
        time = [float(x) for x in time]
        
        headers = lines[6].split()
        
        
        count = 0
        plt.figure()
        for x in angles2plot:
            col_angles = headers.index(angles2plot[count])
            angles = [line.split()[col_angles] for line in lines[7:]]
            angles = [float(x) for x in angles]            
            plt.plot(time,angles)
            count += 1

        plt.ylabel('joint angles [deg]')
        plt.xlabel('time [s]')
        plt.legend(angles2plot)
    