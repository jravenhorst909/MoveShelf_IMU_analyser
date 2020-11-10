# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:54:02 2020

@author: Joris Ravenhorst
"""

import opensim as osim

def inv_kinematics(trial_dir_path,trialID,modelFileName,t_range,sensor_to_opensim_rotation,visualizeTracking):
    # Set variables to use
    modelFileName_calibr = 'calibrated_' + modelFileName      # The path to calibrated input model
    orientationsFileName = trial_dir_path + '/' + trialID + '_orientations.sto'   # The path to orientation data for calibration 
    startTime = t_range[0]          # Start time (in seconds) of the tracking simulation. 
    endTime = t_range[1]              # End time (in seconds) of the tracking simulation.
    
    # Instantiate an InverseKinematicsTool
    imuIK = osim.IMUInverseKinematicsTool()
     
    # Set tool properties
    imuIK.set_model_file(modelFileName_calibr)
    imuIK.set_orientations_file(orientationsFileName)
    imuIK.set_sensor_to_opensim_rotations(sensor_to_opensim_rotation)
    imuIK.set_results_directory(trial_dir_path)
    
    # Set time range in seconds
    imuIK.set_time_range(0, startTime) 
    imuIK.set_time_range(1, endTime)   
    
    # Run IK
    imuIK.run(visualizeTracking)
    
    
    
    # test
    imuIK.get_time_range(1)
    imuIK.get_marker_file()