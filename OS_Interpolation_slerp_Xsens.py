# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:51:46 2020

@author: Joris Ravenhorst
"""

import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp

def Xsens_interpolation_slerp(t_range,t_calib,freq, PacketCounter,SampleTimeFine,Quat_w,Quat_x, Quat_y, Quat_z):

    PacketCounter = [int(index) for index in PacketCounter]
    SampleTimeFine = [float(index) for index in SampleTimeFine]
    Quat_w = [float(index) for index in Quat_w]
    Quat_x = [float(index) for index in Quat_x]
    Quat_y = [float(index) for index in Quat_y]
    Quat_z = [float(index) for index in Quat_z]
    
    gap = []
    
    time_original = SampleTimeFine
    
    i_start = freq*(t_calib)
     
    
    
    #--->plot------------------------------------------------------------------
    quats_pre = [0]*len(SampleTimeFine[i_start:])
    time = [0]*len(SampleTimeFine[i_start:])
    
    for index in range(i_start,len(Quat_w)):
        quats_pre[index-i_start] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]
        time[index-i_start] = (SampleTimeFine[index] - SampleTimeFine[0])/1000000  - (t_calib) 
        
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
        
    for x in range(PacketCounter[-1]-2):
        if PacketCounter[x+1]-PacketCounter[x] != 1:
            
            gap_length = PacketCounter[x+1]-PacketCounter[x]
            
            intpl_PC = (PacketCounter[x+1]-PacketCounter[x])/gap_length #magnitude of interpolation step
            intpl_ST = (SampleTimeFine[x+1]-SampleTimeFine[x])/gap_length #magnitude of interpolation step
              
            for x2 in range(int(gap_length)-1):
                fill = PacketCounter[x] + (x2+1)*intpl_PC
                PacketCounter.insert(x+1+x2,fill)
                
                fill = SampleTimeFine[x] + (x2+1)*intpl_ST
                SampleTimeFine.insert(x+1+x2,fill)
    
            gap.append(gap_length)
            
    orientations_intpl = slerp(SampleTimeFine)
    quats_intpl = orientations_intpl.as_quat()    
    
    Quat_x = quats_intpl[:,0]
    Quat_y = quats_intpl[:,1]
    Quat_z = quats_intpl[:,2]
    Quat_w = quats_intpl[:,3]



    #--->plot------------------------------------------------------------------
    quats_post = [0]*len(SampleTimeFine[i_start:])
    time = [0]*len(SampleTimeFine[i_start:])
    
    for index in range(i_start,len(Quat_w)):
        quats_post[index-i_start] = [Quat_x[index],Quat_y[index],Quat_z[index],Quat_w[index]]
        time[index-i_start] = (SampleTimeFine[index] - SampleTimeFine[0] - (t_range[0]+t_calib) )/1000000  - (t_calib) 
        
    plt.figure()
    plt.plot(time,quats_post) 
    
    plt.ylabel('quaternion')
    plt.xlabel('time [s]')
    plt.legend(['qx','qy','qz','qw'])
    plt.title('post intpl')
    #---<plot------------------------------------------------------------------


    
    if gap != []:
        print('   max gap = {}'.format(max(gap)))
        print('   mean gap = {}'.format(sum(gap)/len(gap)))
        print('   gap/value ratio = {}'.format(len(gap)/len(PacketCounter)))  
        
    else:
        print('   max gap = 0')
        print('   mean gap = 0')
        print('   gap/value ratio = 0')
        
    return(PacketCounter, SampleTimeFine, Quat_w, Quat_x, Quat_y, Quat_z)
        
            
            
