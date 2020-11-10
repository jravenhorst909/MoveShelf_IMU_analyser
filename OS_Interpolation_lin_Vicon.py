# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:51:46 2020

@author: Joris Ravenhorst
"""



def TS_interpolation_lin(freq,time_s,Quat_w,Quat_x, Quat_y, Quat_z):

    time_s = [float(index) for index in time_s]
    Quat_w = [float(index) for index in Quat_w]
    Quat_x = [float(index) for index in Quat_x]
    Quat_y = [float(index) for index in Quat_y]
    Quat_z = [float(index) for index in Quat_z]
    
    time_original = time_s
    
    gap = []
    
    x = 0
    while time_s[x] < time_original[-1]:
        if time_s[x+1]-time_s[x] >= 1.5/freq:
            
            gap_length = round( (time_s[x+1]-time_s[x])*freq )
            gap.append(gap_length)
            
            intpl_ts = (time_s[x+1]-time_s[x])/gap_length #magnitude of interpolation step
            intpl_Qw = (Quat_w[x+1]-Quat_w[x])/gap_length #magnitude of interpolation step
            intpl_Qx = (Quat_x[x+1]-Quat_x[x])/gap_length #magnitude of interpolation step
            intpl_Qy = (Quat_y[x+1]-Quat_y[x])/gap_length #magnitude of interpolation step
            intpl_Qz = (Quat_z[x+1]-Quat_z[x])/gap_length #magnitude of interpolation step
            
            for x2 in range(int(gap_length)-1):
                fill = time_s[x] + (x2+1)*intpl_ts
                time_s.insert(x+1+x2,fill)
    
                fill = Quat_w[x] + (x2+1)*intpl_Qw
                Quat_w.insert(x+1+x2,fill)
                
                fill = Quat_x[x] + (x2+1)*intpl_Qx
                Quat_x.insert(x+1+x2,fill)
                
                fill = Quat_y[x] + (x2+1)*intpl_Qy
                Quat_y.insert(x+1+x2,fill)
                
                fill = Quat_z[x] + (x2+1)*intpl_Qz
                Quat_z.insert(x+1+x2,fill)

        x += 1 
        
        

    if gap != []:
        print('   max gap = {}'.format(max(gap)))
        print('   mean gap = {}'.format(sum(gap)/len(gap)))
        print('   gap/value ratio = {}'.format(len(gap)/len(time_s)))  
        
    else:
        print('   max gap = 0')
        print('   mean gap = 0')
        print('   gap/value ratio = 0')
        
    return(time_s ,Quat_w, Quat_x, Quat_y, Quat_z)
        
            
            
