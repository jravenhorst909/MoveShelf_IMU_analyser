# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:19:29 2020

@author: Joris Ravenhorst
"""


import csv

def findFirst_t(sensor, trial_dir_path, csvfilename, device):
    
#------------------------------------------------------------------------------
#---import csv data------------------------------------------------------------
    with open(trial_dir_path+csvfilename) as csvfile:
        data = csv.reader(csvfile)

#-------sensor Xsens-----------------------------------------------------------
        if sensor == 'Xsens':               
            PacketCounter, SampleTimeFine, OriInc_w, OriInc_x, OriInc_y, OriInc_z, VelInc_x, VelInc_y, VelInc_z, Mag_X, Mag_Y, Mag_Z, Quat_w, Quat_x, Quat_y, Quat_z, FreeAcc_X, FreeAcc_Y, FreeAcc_Z, Statusword = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

#-----------Android Device-----------------------------------------------------
            if device == 'android':
                print('not validated yet')
                
                count = 0
                for row in data:
                    if count > 6:
                        PacketCounter.append(row[0])
                        SampleTimeFine.append(row[1])
                        OriInc_w.append(row[2])
                        OriInc_x.append(row[3])
                        OriInc_y.append(row[4])
                        OriInc_z.append(row[5])
                        VelInc_x.append(row[6])
                        VelInc_y.append(row[7])
                        VelInc_z.append(row[8])
                        Mag_X.append(row[9])
                        Mag_Y.append(row[10])
                        Mag_Z.append(row[11])
                        Quat_w.append(row[12])
                        Quat_x.append(row[13])
                        Quat_y.append(row[14])
                        Quat_z.append(row[15])
                        FreeAcc_X.append(row[16])
                        FreeAcc_Y.append(row[17])
                        FreeAcc_Z.append(row[18])
                        Statusword.append(row[19])            
                    count += 1

#-----------Apple Device-------------------------------------------------------
            if device == 'apple':
                
                count = 0
                for row in data:
                    if count > 8:
                        PacketCounter.append(row[0])
                        SampleTimeFine.append(row[1])
                        Quat_w.append(row[2])
                        Quat_x.append(row[3])
                        Quat_y.append(row[4])
                        Quat_z.append(row[5])
                    count += 1           
                    
                
#-------sensor Vicon-----------------------------------------------------------
        if sensor == 'Vicon':
            time_s, type_, Acc_x, Acc_y, Acc_z, Angvel_x, Angvel_y, Angvel_z, Mag_x, Mag_y, Mag_z, Quat_x, Quat_y, Quat_z, Quat_w = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
        
#-----------Android Device-----------------------------------------------------           
            if device == 'android':
                print('the vicon trident is not compatible with android')

#-----------Apple Device-------------------------------------------------------
            if device == 'apple':
                
                count = 0
                for row in data:
                    if count > 0:
                        time_s.append(row[0])
                        type_.append(row[1])
                        Acc_x.append(row[2])
                        Acc_y.append(row[3])
                        Acc_z.append(row[4])
                        Angvel_x.append(row[5])
                        Angvel_y.append(row[6])
                        Angvel_z.append(row[7])
                        Mag_x.append(row[8])
                        Mag_y.append(row[9])
                        Mag_z.append(row[10])
                        Quat_x.append(row[11])
                        Quat_y.append(row[12])
                        Quat_z.append(row[13])
                        Quat_w.append(row[14])
                    count += 1
    
    

#---interpolation--------------------------------------------------------------


        if sensor == 'Xsens':
            t0 = float(SampleTimeFine[0])             
        if sensor == 'Vicon':
            t0 = float(time_s[0])
            

    return t0    
        
        
        