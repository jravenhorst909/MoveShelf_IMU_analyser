# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:11:51 2020

@author: Joris Ravenhorst
"""

def investigateJoints(IMUs):
    joints = []
    
    if 'pelvis' in IMUs:
        joints.append('pelvis')
        
        
        if 'femur_r' in IMUs:
            joints.append('hip_r')
        if 'femur_l' in IMUs:
            joints.append('hip_l')
            
            
        if 'torso' in IMUs:
            joints.append('back')
      
            
    if 'femur_r' in IMUs:
        if 'tibia_r' in IMUs:
            joints.append('knee_r')
    if 'femur_l' in IMUs:
        if 'tibia_l' in IMUs:
            joints.append('knee_l')
            
            
    if 'tibia_r' in IMUs:
        if 'talus_r' in IMUs:
            joints.append('ankle_r')
    if 'tibia_l' in IMUs:
        if 'talus_l' in IMUs:
            joints.append('ankle_l')


    if 'talus_r' in IMUs:
        if 'calcn_r' in IMUs:
            joints.append('subtalar_r')
    if 'talus_l' in IMUs:
        if 'calcn_l' in IMUs:
            joints.append('subtalar_l')


    if 'calcn_r' in IMUs:
        if 'toes_r' in IMUs:
            joints.append('mtp_r')
    if 'calcn_l' in IMUs:
        if 'toes_l' in IMUs:
            joints.append('mtp_l')
            
            
    if 'torso' in IMUs:
        if 'humerus_r' in IMUs:
            joints.append('shoulder_r')          
        if 'humerus_l' in IMUs:
            joints.append('shoulder_l')
            
            
    if 'humerus_r' in IMUs:
        if 'ulna_r' in IMUs: 
            joints.append('elbow_r')
    if 'humerus_l' in IMUs:
        if 'ulna_l' in IMUs: 
            joints.append('elbow_l')            
    
    
    if 'radius_r' in IMUs:
        if 'ulna_r' in IMUs: 
            joints.append('radioulnar_r')
    if 'radius_l' in IMUs:
        if 'ulna_l' in IMUs: 
            joints.append('radioulnar_l')


    if 'radius_r' in IMUs:
        if 'hand_r' in IMUs: 
            joints.append('wrist_r')            
    if 'radius_l' in IMUs:
        if 'hand_l' in IMUs: 
            joints.append('wrist_l')            
            
    return(joints)