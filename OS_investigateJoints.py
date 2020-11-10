# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:11:51 2020

@author: Joris Ravenhorst
"""

def investigateJoints(IMUs):
    joints = []
    
    if 'pelvis' in IMUs:
        if 'femur_r' in IMUs:
            joints.append('hip_r')
            
        if 'femur_l' in IMUs:
            joints.append('hip_l')
            
    if 'femur_r' in IMUs:
        if 'tibia_r' in IMUs:
            joints.append('knee_r')
            
    if 'femur_l' in IMUs:
        if 'tibia_l' in IMUs:
            joints.append('knee_l')
            
    if 'tibia_r' in IMUs:
        if 'calcn_r' in IMUs:
            joints.append('ankle_r')

    if 'tibia_l' in IMUs:
        if 'calcn_l' in IMUs:
            joints.append('ankle_l')

    return(joints)