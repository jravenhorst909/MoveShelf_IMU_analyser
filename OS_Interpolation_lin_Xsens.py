# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:51:46 2020

@author: Joris Ravenhorst
"""



def DOT_interpolation_lin(PacketCounter,SampleTimeFine,Quat_w,Quat_x, Quat_y, Quat_z):

    PacketCounter = [int(index) for index in PacketCounter]
    SampleTimeFine = [float(index) for index in SampleTimeFine]
    Quat_w = [float(index) for index in Quat_w]
    Quat_x = [float(index) for index in Quat_x]
    Quat_y = [float(index) for index in Quat_y]
    Quat_z = [float(index) for index in Quat_z]
    
    gap = []
    
    for x in range(PacketCounter[-1]-2):
        if PacketCounter[x+1]-PacketCounter[x] != 1:
            
            gap_length = PacketCounter[x+1]-PacketCounter[x]
            
            intpl_PC = (PacketCounter[x+1]-PacketCounter[x])/gap_length #magnitude of interpolation step
            intpl_ST = (SampleTimeFine[x+1]-SampleTimeFine[x])/gap_length #magnitude of interpolation step
            intpl_Qw = (Quat_w[x+1]-Quat_w[x])/gap_length #magnitude of interpolation step
            intpl_Qx = (Quat_x[x+1]-Quat_x[x])/gap_length #magnitude of interpolation step
            intpl_Qy = (Quat_y[x+1]-Quat_y[x])/gap_length #magnitude of interpolation step
            intpl_Qz = (Quat_z[x+1]-Quat_z[x])/gap_length #magnitude of interpolation step
                    
            
            
            for x2 in range(int(gap_length)-1):
                fill = PacketCounter[x] + (x2+1)*intpl_PC
                PacketCounter.insert(x+1+x2,fill)
                
                fill = SampleTimeFine[x] + (x2+1)*intpl_ST
                SampleTimeFine.insert(x+1+x2,fill)
    
                fill = Quat_w[x] + (x2+1)*intpl_Qw
                Quat_w.insert(x+1+x2,fill)
                
                fill = Quat_x[x] + (x2+1)*intpl_Qx
                Quat_x.insert(x+1+x2,fill)
                
                fill = Quat_y[x] + (x2+1)*intpl_Qy
                Quat_y.insert(x+1+x2,fill)
                
                fill = Quat_z[x] + (x2+1)*intpl_Qz
                Quat_z.insert(x+1+x2,fill)
            
            gap.append(gap_length)
    
    if gap != []:
        print('   max gap = {}'.format(max(gap)))
        print('   mean gap = {}'.format(sum(gap)/len(gap)))
        print('   gap/value ratio = {}'.format(len(gap)/len(PacketCounter)))  
        
    else:
        print('   max gap = 0')
        print('   mean gap = 0')
        print('   gap/value ratio = 0')
        
    return(PacketCounter, SampleTimeFine, Quat_w, Quat_x, Quat_y, Quat_z)
        
            
            
