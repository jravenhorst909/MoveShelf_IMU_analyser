# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:50:22 2020

@author: Joris Ravenhorst
"""

def sync_tridents(time_s,t0,PacketCounter, Mat11,Mat21,Mat31,Mat12,Mat22,Mat32,Mat13,Mat23,Mat33):
    t0_latest = max(t0)
                
    t0_ind = time_s.index(min(time_s, key=lambda x:abs(x-t0_latest)))

    if t0_ind != 0:
        del PacketCounter[-t0_ind:]
        del time_s[:t0_ind]
        del Mat11[:t0_ind]
        del Mat21[:t0_ind]
        del Mat31[:t0_ind]
        del Mat12[:t0_ind]
        del Mat22[:t0_ind]
        del Mat32[:t0_ind]
        del Mat13[:t0_ind]
        del Mat23[:t0_ind]
        del Mat33[:t0_ind]
    
    return time_s,PacketCounter, Mat11,Mat21,Mat31,Mat12,Mat22,Mat32,Mat13,Mat23,Mat33



        
        
        
        
        
        