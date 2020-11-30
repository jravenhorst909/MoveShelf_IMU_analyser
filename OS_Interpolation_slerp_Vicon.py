# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:51:46 2020

@author: Joris Ravenhorst
"""

import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp

def Vicon_interpolation_slerp(freq,time_s,delay,t_calib,Quat_w,Quat_x, Quat_y, Quat_z):

    time_s = [float(index) for index in time_s]
    Quat_w = [float(index) for index in Quat_w]
    Quat_x = [float(index) for index in Quat_x]
    Quat_y = [float(index) for index in Quat_y]
    Quat_z = [float(index) for index in Quat_z]
    
    gap = []
    
    time_original = time_s
    
    i_start = (0)*freq # (delay-(t_calib))*freq
    t_start = time_s[i_start]    



    #--->plot------------------------------------------------------------------
    quats_pre = [0]*len(time_s[i_start:])
    time = time_s[time_s.index(t_start):]
    
    for index in range(i_start,len(Quat_w)):
        quats_pre[index-i_start] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]
    
    plt.figure()
    plt.plot(time,quats_pre) 
    
    plt.ylabel('quaternion')
    plt.xlabel('time [s]')
    plt.legend(['qx','qy','qz','qw'])
    plt.title('pre intpl')   
    #---<plot------------------------------------------------------------------
    
    
    
    quats_pre = [0]*len(time_original)
    for index in range(len(time_original)):
        quats_pre[index] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]
    
    orientations_pre = R.from_quat(quats_pre)
    
    slerp = Slerp(time_original,orientations_pre)
    
    x = 0
    while time_s[x] < time_original[-1]:
        if time_s[x+1]-time_s[x] >= 1.5/freq:
            
            gap_length = round( (time_s[x+1]-time_s[x])*freq )
            gap.append(gap_length)
            
            intpl_ts = (time_s[x+1]-time_s[x])/gap_length #magnitude of interpolation step
            
            for x2 in range(int(gap_length)-1):
                fill = time_s[x] + (x2+1)*intpl_ts
                time_s.insert(x+1+x2,fill)
        x += 1 
    
    orientations_intpl = slerp(time_s)
    
    quats_intpl = orientations_intpl.as_quat() 
    Quat_x = quats_intpl[:,0]
    Quat_y = quats_intpl[:,1]
    Quat_z = quats_intpl[:,2]
    Quat_w = quats_intpl[:,3]
    
    euler_intpl = orientations_intpl.as_euler('xyz',degrees=True)
    euler_roll = euler_intpl[:,0]       # x
    euler_pitch = euler_intpl[:,1]      # y
    euler_yaw = euler_intpl[:,2]        # z
    
    
    #--->plot------------------------------------------------------------------
    quats_post = [0]*len(time_s[time_s.index(t_start):])
    euler_post = [0]*len(quats_post)
    time = time_s[time_s.index(t_start):]
    
    for index in range(time_s.index(t_start),len(Quat_w)):
        quats_post[index-time_s.index(t_start)] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]
        euler_post[index-time_s.index(t_start)] = [euler_roll[index],euler_pitch[index],euler_yaw[index]]
        
    plt.figure()
    plt.plot(time,quats_post) 
    
    plt.ylabel('quaternion')
    plt.xlabel('time [s]')
    plt.legend(['qx','qy','qz','qw'])
    plt.title('quats post intpl') 
    
    plt.figure()
    plt.plot(time,euler_post) 
    
    plt.ylabel('Euler angle [deg]')
    plt.xlabel('time [s]')
    plt.legend(['roll','pitch','yaw'])
    plt.title('euler post intpl')     
    
    
    #---<plot------------------------------------------------------------------        
        
    

    if gap != []:
        print('   max gap = {}'.format(max(gap)))
        print('   mean gap = {}'.format(sum(gap)/len(gap)))
        print('   gap/value ratio = {}'.format(len(gap)/len(time_s)))  
        
    else:
        print('   max gap = 0')
        print('   mean gap = 0')
        print('   gap/value ratio = 0')
        
    return(time_s ,Quat_w, Quat_x, Quat_y, Quat_z)
        
            
            
