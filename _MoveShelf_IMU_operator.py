# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:51:24 2020

@author: Joris Ravenhorst
"""

from OpenSense_Main import Application
app = Application()


TrialName = '20201127_13'                                  # Should include date and trial number.
modelFileName = 'OpenSim_model.osim'             # The path to input model.
visualizeCalibration = False                      # Visualize calibrated model?
visualizeTracking = False                        # Visualize motion?
UploadFiles = False                              # Create a new clip and upload all files.

app.IMUanalyser(TrialName,modelFileName,visualizeCalibration,visualizeTracking,UploadFiles)



#%% Upload additional video 
VideoName = ''                                  # write video filename, including extension.

app.UploadVideo(VideoName)


