# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:43:52 2020

@author: Joris Ravenhorst
"""

import opensim as osim

def calibrate_model(trial_dir_path,trialID,modelFileName,sensor_to_opensim_rotation,baseIMUName,baseIMUHeading,visulizeCalibration):

    orientationsFileName = trial_dir_path +'/'+ trialID + '_orientations.sto'   # The path to orientation data for calibration 
   
    # Instantiate an IMUPlacer object
    imuPlacer = osim.IMUPlacer()
    
    # Set properties for the IMUPlacer
    imuPlacer.set_model_file(modelFileName)
    imuPlacer.set_orientation_file_for_calibration(orientationsFileName)
    imuPlacer.set_sensor_to_opensim_rotations(sensor_to_opensim_rotation)
    imuPlacer.set_base_imu_label(baseIMUName)
    imuPlacer.set_base_heading_axis(baseIMUHeading)
    
    # Run the IMUPlacer
    imuPlacer.run(visulizeCalibration)
    
    # Get the model with the calibrated IMU
    model = imuPlacer.getCalibratedModel()
    
    # Print the calibrated model to file.

    #   -> this one is to run invkinematics on automatically. This file will be overwritten for each trial using the same 'modelFilename'
    model.printToXML('calibrated_' + modelFileName)
    #   -> this one is for storage
    model.printToXML(trial_dir_path + '/calibrated_' + modelFileName)    
    
    
