# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:28:40 2020

@author: Joris Ravenhorst
"""

import opensim as osim

def IMUdata_conversion(trial_dir_path,TrialName):
    # Build an Xsens Settings Object. 
    # Instantiate the Reader Settings Class
    xsensSettings = osim.XsensDataReaderSettings('myIMUMappings.xml')
    # Instantiate an XsensDataReader
    xsens = osim.XsensDataReader(xsensSettings)
    # Read in seprate tables of data from the specified IMU file(s)
    tables = xsens.read(trial_dir_path)
    # get the trial name from the settings
    trialID = xsensSettings.get_trial_prefix()
    # Get Orientation Data as quaternions
    quatTable = xsens.getOrientationsTable(tables)
    # Write to file
    osim.STOFileAdapterQuaternion.write(quatTable, trial_dir_path +'/'+ trialID + '_orientations.sto')
    # Get Acceleration Data
    accelTable = xsens.getLinearAccelerationsTable(tables)
    # Write to file
    osim.STOFileAdapterVec3.write(accelTable, trial_dir_path +'/'+ trialID + '_linearAccelerations.sto')
    # Get Magnetic (North) Heading Data
    magTable = xsens.getMagneticHeadingTable(tables)
    # Write to file
    osim.STOFileAdapterVec3.write(magTable, trial_dir_path +'/'+ trialID + '_magneticNorthHeadings.sto')
    # Get Angular Velocity Data
    angVelTable = xsens.getAngularVelocityTable(tables)
    # Write to file
    osim.STOFileAdapterVec3.write(angVelTable, trial_dir_path +'/'+ trialID + '_angularVelocities.sto')
    
    return trialID