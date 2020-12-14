# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:00:52 2020

@author: Joris Ravenhorst
"""

import csv
import os.path
from OS_Interpolation_slerp_Xsens import Xsens_interpolation_slerp
from OS_Interpolation_slerp_Vicon import Vicon_interpolation_slerp
from OS_sync_tridents import sync_tridents
from OS_reset_heading import reset_heading
from scipy.spatial.transform import Rotation as R


def csv_to_txt(sensor,trial_dir_path, csvfilename, device, t_calib, freq, delay, t_range, t0):
    
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
    
    
#------------------------------------------------------------------------------
#---interpolation--------------------------------------------------------------


        if sensor == 'Xsens':
            PacketCounter,SampleTimeFine,Quat_w,Quat_x, Quat_y, Quat_z = Xsens_interpolation_slerp(t_range,t_calib,freq, PacketCounter,SampleTimeFine,Quat_w,Quat_x, Quat_y, Quat_z)            
            length = len(PacketCounter)               
        if sensor == 'Vicon':
            time_s ,Quat_w, Quat_x, Quat_y, Quat_z = Vicon_interpolation_slerp(freq,time_s,delay,t_calib,Quat_w,Quat_x, Quat_y, Quat_z)
            PacketCounter = list(range(1,len(time_s)+1))
            length = len(time_s)
            
            
#---creating rotation matrices-------------------------------------------------
        Mat11raw,Mat21raw,Mat31raw,Mat12raw,Mat22raw,Mat32raw,Mat13raw,Mat23raw,Mat33raw = [0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length,[0]*length
        
        count = 0
        for x in range(length):
            
            Matraw = R.as_matrix(R.from_quat([Quat_x[count],Quat_y[count],Quat_z[count],Quat_w[count]]))
            Mat11raw[count] = Matraw[0][0]
            Mat12raw[count] = Matraw[0][1]
            Mat13raw[count] = Matraw[0][2]
            Mat21raw[count] = Matraw[1][0]
            Mat22raw[count] = Matraw[1][1]
            Mat23raw[count] = Matraw[1][2]
            Mat31raw[count] = Matraw[2][0]
            Mat32raw[count] = Matraw[2][1]
            Mat33raw[count] = Matraw[2][2]
                        
            count+=1
            
#---sync Tridents--------------------------------------------------------------
        if sensor == 'Vicon':
            time_s,PacketCounter, Mat11raw,Mat21raw,Mat31raw,Mat12raw,Mat22raw,Mat32raw,Mat13raw,Mat23raw,Mat33raw = sync_tridents(time_s,t0,PacketCounter, Mat11raw,Mat21raw,Mat31raw,Mat12raw,Mat22raw,Mat32raw,Mat13raw,Mat23raw,Mat33raw)
            length = len(time_s)

#---reset heading--------------------------------------------------------------        
        Mat11,Mat21,Mat31,Mat12,Mat22,Mat32,Mat13,Mat23,Mat33 = reset_heading(sensor,freq,delay, Mat11raw,Mat21raw,Mat31raw,Mat12raw,Mat22raw,Mat32raw,Mat13raw,Mat23raw,Mat33raw)    
        

#---create .txt files----------------------------------------------------------
        if sensor == 'Xsens':
            txtfilename = '{}_{}.txt'.format(csvfilename[13:28],csvfilename[0:12])
        if sensor == 'Vicon':
            TSindex = csvfilename.index('TS')
            csvfilename_short = csvfilename.replace('-','')
            txtfilename = '{}_{}_Vicon_TS_{}.txt'.format(csvfilename_short[TSindex+8:TSindex+16],csvfilename_short[TSindex+16:TSindex+22],csvfilename_short[TSindex+2:TSindex+7])
        
        
        txtfilepath = trial_dir_path
        completename = os.path.join(txtfilepath,txtfilename)        
        with open(completename,'w') as fh:
            fh.write('// Start Time: Unknown'"\n"
                     '// Update Rate: {}.0Hz'"\n"
                     '// Filter Profile: human (46.1)'"\n"
                     '// Option Flags: AHS Disabled ICC Disabled '"\n"
                     '// Firmware Version: 4.0.2'"\n".format(freq))                     
    
            count = t_calib*freq
            if sensor == 'Xsens':
                fh.write('PacketCounter\tSampleTimeFine\tMat[1][1]\tMat[2][1]\tMat[3][1]\tMat[1][2]\tMat[2][2]\tMat[3][2]\tMat[1][3]\tMat[2][3]\tMat[3][3]'"\n")

                for x in range(length):
                    fh.write("%s" % '{}'.format(PacketCounter[count])+'\t{}'.format(SampleTimeFine[count])+'\t{}'.format(Mat11[count])+'\t{}'.format(Mat21[count])+'\t{}'.format(Mat31[count])+'\t{}'.format(Mat12[count])+'\t{}'.format(Mat22[count])+'\t{}'.format(Mat32[count])+'\t{}'.format(Mat13[count])+'\t{}'.format(Mat23[count])+'\t{}\n'.format(Mat33[count]))
                    count += 1
                    if count == length:
                        break 
            
            if sensor == 'Vicon':
                fh.write('PacketCounter\tSampleTimeFine\tMat[1][1]\tMat[2][1]\tMat[3][1]\tMat[1][2]\tMat[2][2]\tMat[3][2]\tMat[1][3]\tMat[2][3]\tMat[3][3]'"\n")

                for x in range(length):
                    fh.write("%s" % '{}'.format(PacketCounter[count])+'\t{}'.format(time_s[count])+'\t{}'.format(Mat11[count])+'\t{}'.format(Mat21[count])+'\t{}'.format(Mat31[count])+'\t{}'.format(Mat12[count])+'\t{}'.format(Mat22[count])+'\t{}'.format(Mat32[count])+'\t{}'.format(Mat13[count])+'\t{}'.format(Mat23[count])+'\t{}\n'.format(Mat33[count]))
                    count += 1
                    if count == length:
                        break 
                

      
        
        
        