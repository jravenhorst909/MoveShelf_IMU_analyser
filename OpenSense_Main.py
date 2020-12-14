# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:42:01 2020

@author: Joris Ravenhorst
"""

# Import the opensim libraries
import os
import glob
import time
import opensim as osim # necessary to read setup file
from numpy import pi # necessary to read setup file
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from api import MoveshelfApi, Metadata
api = MoveshelfApi()

# from OS_trialsetup import trialsetup
from OS_IMUmappings import IMUmappings
from OS_findFirst_t import findFirst_t
from OS_csv_to_txt import csv_to_txt
from OS_IMUDataConversion import IMUdata_conversion
from OS_CalibrateModel import calibrate_model
from OS_InvKin import inv_kinematics
from OS_createAngles_json import createAngles_json
from OS_investigateJoints import investigateJoints
from OS_plotJointangles import plotJointangles
from OS_plotQuaternions import plotQuats

class Application:
    
    
    def IMUanalyser(self,TrialName,modelFileName,visualizeCalibration,visualizeTracking,UploadFiles):
        
        sensor_to_opensim_rotation = osim.Vec3(-pi/2,0,0)	# The rotation of IMU data to the OpenSim world frame. !! Only change if subject/model is not facing x-direction in the calibration pose. 

        
        
        #------------------------------------------------------------------------------
        # %% Setup
        #   -if uploading: to which project?
        #   -Find .csv IMU data and setup.txt.
        #   -Creates 'myIMUMappings.xml' : which IMU belongs to which body segment.
        #   -Resets the heading of all IMUs to 0 yaw in initial timestep. Assuming all IMUs are aligned.
        #   -Applies heading reset to whole dataset so all IMU orientations are relative to a shared initial position.
        #   -Cuts pre-calibration data from dataset.
        #   -Creates .txt files from .csv files in useable format.
        
        # upload to which project?
        if UploadFiles == True:
            userProjects = api.getUserProjects()
        
            print('upload to which project?:')
            
            count = 0
            for x in userProjects:
                print('[{}] {}'.format(count,userProjects[count]))
                count += 1
                   
            project_no = int(input('enter project number:\n'))
            
            print('\ndid you record a video with Vicon Blue Trident?:\n[0] Yes\n[1] No')
            uploadvideo = int(input('enter number:\n'))
            
            print('\nthanks\n')
            
            
        #---find data and setup
        for x in os.listdir(os.path.dirname(os.path.realpath('__file__'))+'\\IMUData'):    # runs through all directories in IMUData
            if TrialName in x:
                self._trial_dir_path = os.path.dirname(os.path.realpath('__file__'))+'\\IMUData\\'+x+'\\' # search for directory with 'trial' in its name
                trial_dir_path = self._trial_dir_path
        
        
        #---get .csv files
                files = glob.glob(trial_dir_path+'*.csv')
                count = 0
                for x in files:
                    files[count] = files[count].replace(trial_dir_path,'')
                    count+=1
        
        
        #---Xsens or Vicon?
        if 'DOT' in files[0]:
            sensor = 'Xsens'
            delay = 0
        if 'TS' in files[0]:
            sensor = 'Vicon'
            
            
        #---retrieve trial settings from setup file
        ldic = locals()
        exec(open(trial_dir_path + 'setup.txt','r').read(),globals(),ldic)
        
        device = ldic['device']
        freq = ldic['freq']
        t_calib = ldic['t_calib']  
        t_range = ldic['t_range']
        delay = ldic['delay']
        baseIMUName = ''
        baseIMUHeading = ''
        IMUs = ldic['IMUs']
    
        t_range = [t_range[0]-t_calib, t_range[1]-t_calib]
        
        
        #---which joints are involved?
        joints = investigateJoints(IMUs)
        
        
        #---create myIMUmappings.xml
        IMUmappings(sensor,trial_dir_path,files,IMUs)
        
        
        #---convert output data .csv files to .txt in useable format 
        #   and perform interpolation and heading reset
        t0 = [0]*len(IMUs)
        
        count = 0
        for csvfilename in files:
            t0[count] = findFirst_t(sensor, trial_dir_path, csvfilename, device)
            count += 1
        
        count = 0
        for x in files:
            print('{}'.format(IMUs[count]))
            csv_to_txt(sensor, trial_dir_path, files[count], device, t_calib, freq, delay, t_range, t0)
            count += 1
          
            
          
        #------------------------------------------------------------------------------
        # %% IMUDataConversion
        #   -Create .sto files of orientation, lin acceleration, magnetic north heading, angular velocity.
        #   -If no such data is provided, the file is left empty.
        trialID = IMUdata_conversion(trial_dir_path,TrialName)
        
        # plotQuats(trial_dir_path, trialID)

        
        
        
        #------------------------------------------------------------------------------
        # %% CalibrateModel
        #   -Create a calibrated .osim model.
        calibrate_model(trial_dir_path,trialID,modelFileName,sensor_to_opensim_rotation,baseIMUName,baseIMUHeading,visualizeCalibration)
           
        
        
        #------------------------------------------------------------------------------
        # %% InverseKinematics
        #   -Perform Opensim's inverse kinematics. Creates .mot file describing all joint angles.
        inv_kinematics(trial_dir_path,trialID,modelFileName,t_range,sensor_to_opensim_rotation,visualizeTracking)
        
        
        
        #------------------------------------------------------------------------------
        # %% PlotJointAngles in console
        #   function: plotJointangles(trial_dir_path, trialID, angles2plot)
        #   lumbar:
        #       'lumbar_extension', 'lumbar_bending', 'lumbar_rotation' 
        #   pelvic:
        #       'pelvis_tilt', 'pelvis_list', 'pelvis_rotation', 'pelvis_tx', 'pelvis_ty', 'pelvis_tz'
        #   lower extremities:
        #       'hip_flexion_r', 'hip_adduction_r', 'hip_rotation_r', 'knee_angle_r', 'knee_angle_r_beta', 'ankle_angle_r', 'subtalar_angle_r', 'mtp_angle_r' 
        #       'hip_flexion_l', 'hip_adduction_l', 'hip_rotation_l', 'knee_angle_l', 'knee_angle_l_beta', 'ankle_angle_l', 'subtalar_angle_l', 'mtp_angle_l' 
        #   upper extremities:
        #       'arm_flex_r', 'arm_add_r', 'arm_rot_r', 'elbow_flex_r', 'pro_sup_r', 'wrist_flex_r', 'wrist_dev_r' 
        #       'arm_flex_l', 'arm_add_l', 'arm_rot_l', 'elbow_flex_l', 'pro_sup_l', 'wrist_flex_l', 'wrist_dev_l'
        
        # # figure example:
        # angles2plot = ['knee_angle_r','knee_angle_l']
        # plotJointangles(trial_dir_path, trialID, angles2plot)
        
        
        
        #------------------------------------------------------------------------------
        # %% Upload Files
        if UploadFiles == True: 
            
            print('\nuploading files...')
            
            # create .json files
            createAngles_json(trial_dir_path,joints)    
            
            # create clip
            for x in os.listdir(os.path.dirname(os.path.realpath('__file__'))+'\\IMUData'):    # runs through all directories in IMUData
                if TrialName in x:
                    clipname = x
            self.clipID = api.uploadEmptyClip(clipname, userProjects[project_no])
            
            # upload joint angle data
            api.uploadAdditionalData(trial_dir_path+'angles.json', self.clipID, 'data', 'angles.json') # uploads additional data, returns data ID
                
            # upload all files
            for filename in os.listdir(trial_dir_path):
                datafile_path = trial_dir_path+filename
                dataType = filename[ -( filename[::-1].index('.') +1 ): ]
                
                
                if dataType != '.json':
                    if dataType == '.mp4':
                        if filename != "video_cut.mp4":
                            # optionally cut Trident video
                            if uploadvideo == 0:
                                ffmpeg_extract_subclip(datafile_path, 10, 12, targetname=trial_dir_path+"video_cut.mp4")    
                                # ffmpeg_extract_subclip(datafile_path, t_range[0], t_range[1], targetname=trial_dir_path+"video_cut.mp4")    
                                api.uploadAdditionalData(trial_dir_path+"video_cut.mp4", self.clipID, 'video', "video_cut.mp4")
                            if uploadvideo == 1:
                                api.uploadAdditionalData(trial_dir_path+filename, self.clipID, 'video', filename)
                                           
                    if dataType != '.mp4': 
                        api.uploadAdditionalData(datafile_path, self.clipID, dataType, filename) # uploads additional data, returns data ID
                
            print('\t ...done!')
        
    
    
    def UploadVideo(self,video):
        if video != '':
            api.uploadAdditionalData(self._trial_dir_path+video, self.clipID, 'video', video)
        
