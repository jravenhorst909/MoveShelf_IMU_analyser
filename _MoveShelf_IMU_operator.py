# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:51:24 2020

@author: Joris Ravenhorst
"""

from OpenSense_Main import Application
app = Application()


TrialName = '20201104_1'                                  # Should include date and trial number.
modelFileName = 'OpenSim_model.osim'            # The path to input model.
visulizeCalibration = True                      # Visualize calibrated model?
visualizeTracking = True                        # Visualize motion?
UploadFiles = True                              # Create a new clip and upload all files.

app.IMUanalyser(TrialName,modelFileName,visulizeCalibration,visualizeTracking,UploadFiles)



#%% Upload additional video 
VideoName = ''                                  # write video filename, including extension.

app.UploadVideo(VideoName)



