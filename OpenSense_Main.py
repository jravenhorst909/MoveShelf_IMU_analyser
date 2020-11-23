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
from api import MoveshelfApi, Metadata
api = MoveshelfApi()

# from OS_trialsetup import trialsetup
from OS_IMUmappings import IMUmappings
from OS_csv_to_txt import csv_to_txt
from OS_IMUDataConversion import IMUdata_conversion
from OS_CalibrateModel import calibrate_model
from OS_InvKin import inv_kinematics
from OS_sync_tridents import sync_tridents
from OS_createAngles_json import createAngles_json
from OS_investigateJoints import investigateJoints
from OS_plotJointangles import plotJointangles
from OS_plotQuaternions import plotQuats

class Application:
    
    TrialName = '20201111_8'
    modelFileName = 'OpenSim_model.osim'          # The path to input model
    customIMUplacer = False                        # Use custom IMU placement on calibrated model? just for looks ^^
    visualizeCalibration = True                     # Visualize calibrated model?
    visualizeTracking = False                       # Visualize motion?
    
    UploadFiles = False                              # Create a new clip and upload all files.
    
    def IMUanalyser(self,TrialName,modelFileName,visualizeCalibration,visualizeTracking,UploadFiles):
        
        delay = 60          # after how many seconds is Vicon's heading stable?
        
        
        
        #------------------------------------------------------------------------------
        # %% Setup
        #   -if uploading: to which project?
        #   -Find .csv IMU data and setup.txt.
        #   -Creates 'myIMUMappings.xml'' : which IMU belongs to which body segment.
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
            print('thanks\n')
            
            
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
        t_calib = ldic['t_calib']-delay
        t_range = ldic['t_range']
        baseIMUName = ''
        baseIMUHeading = ''
        IMUs = ldic['IMUs']
    
        t_range = [t_range[0]-t_calib, t_range[1]-t_calib]
        sensor_to_opensim_rotation = osim.Vec3(-pi/2,0,0)	# The rotation of IMU data to the OpenSim world frame. !! Only change if subject/model is not facing x-direction in the calibration pose. 
        
        
        #---which joints are involved?
        joints = investigateJoints(IMUs)
        
        
        #---create myIMUmappings.xml
        IMUmappings(sensor,trial_dir_path,files,IMUs)
        
        
        #---convert output data .csv files to .txt in useable format 
        #   and perform interpolation and heading reset
        count = 0
        t0 = [0]*len(IMUs)
        txtfilenames = [0]*len(IMUs)
        
        for x in files:
            
            print('{}'.format(IMUs[count]))
            t0[count],txtfilenames[count] = csv_to_txt(sensor,trial_dir_path, files[count], device, t_calib, freq, delay, t_range)
            count += 1
            
        if sensor == 'Vicon':
            sync_tridents(t0,txtfilenames,freq)    
          
            
          
        #------------------------------------------------------------------------------
        # %% IMUDataConversion
        #   -Create .sto files of orientation, lin acceleration, magnetic north heading, angular velocity.
        #   -If no such data is provided, the file is left empty.
        trialID = IMUdata_conversion(trial_dir_path,TrialName)
        
        plotQuats(trial_dir_path, trialID)
        time.sleep(1)
        
        
        
        #------------------------------------------------------------------------------
        # %% CalibrateModel
        #   -Create a calibrated .osim model.
        #   -Optionally use custom IMU placement
        calibrate_model(trial_dir_path,trialID,modelFileName,sensor_to_opensim_rotation,baseIMUName,baseIMUHeading,visualizeCalibration)
           
        
        
        #------------------------------------------------------------------------------
        # %% InverseKinematics
        #   -Perform Opensim's inverse kinematics.
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
                    api.uploadAdditionalData(datafile_path, self.clipID, dataType, filename) # uploads additional data, returns data ID
            
            print('\t ...done!')
        
    
    
    def UploadVideo(self,video):
        if video != '':
            api.uploadAdditionalData(self._trial_dir_path+video, self.clipID, 'video', video)
        
