# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:44:54 2020

@author: Joris Ravenhorst
"""


from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement



def IMUmappings(sensor,trial_dir_path,files, IMUs):
#------------------------------------------------------------------------------
#---sensor Xsens---------------------------------------------------------------
    if sensor == 'Xsens':
        DOT_numbers = [0]*len(files)
        count = 0
        for file in files:
            DOT_numbers[count] = file[10:12]
            count += 1
        
        #---OpenSimDocument
        root = Element('OpenSimDocument')
        root.set('Version','41000')
        tree = ElementTree(root)
        
        #---XsensDataReaderSettings
        settings = SubElement(root,'XsensDataReaderSettings')
        
        #---trial
        trial_prefix = SubElement(settings,'trial_prefix')
        trial = '{}'.format(files[0][13:28])
        trial_prefix.text = trial
        
        #---sensors
        ExperimentalSensors = SubElement(settings,'ExperimentalSensors')
    
        #---identify elements and add to .xml file
        count = 0
        for x in files:
    
            ExperimentalSensor = SubElement(ExperimentalSensors,'ExperimentalSensor')
            ExperimentalSensor.set('name','_Xsens_DOT_{}'.format(DOT_numbers[count]))
    
            name_in_model = SubElement(ExperimentalSensor,'name_in_model')
            name_in_model.text = IMUs[count] + '_imu'        
       
            count += 1
        
    
        #--- write file
        #--- this file needs to be in the same folder as main script
        tree.write('myIMUmappings.xml')      
        

    
#------------------------------------------------------------------------------
#---sensor Vicon---------------------------------------------------------------    
    if sensor == 'Vicon':
        csvfilename_short = [0]*len(files)
        count = 0
        for x in files: 
            TSindex = files[0].index('TS')
            csvfilename_short[count] = files[count].replace('-','')
            count += 1
        
        #---OpenSimDocument
        root = Element('OpenSimDocument')
        root.set('Version','41000')
        tree = ElementTree(root)
        
        #---XsensDataReaderSettings
        settings = SubElement(root,'XsensDataReaderSettings')
        
        #---trial
        trial_prefix = SubElement(settings,'trial_prefix')
        trial = '{}_{}'.format(csvfilename_short[0][TSindex+8:TSindex+16],csvfilename_short[0][TSindex+16:TSindex+22])
        trial_prefix.text = trial
        
        #---sensors
        ExperimentalSensors = SubElement(settings,'ExperimentalSensors')
        
        #---identify elements and add to .xml file
        count = 0
        for x in files:        
            ExperimentalSensor = SubElement(ExperimentalSensors,'ExperimentalSensor')
            ExperimentalSensor.set('name','_Vicon_TS_{}'.format(csvfilename_short[count][TSindex+2:TSindex+7]))
    
            name_in_model = SubElement(ExperimentalSensor,'name_in_model')
            name_in_model.text = IMUs[count] + '_imu'        
       
            count += 1
        
    
        #--- write file
        #--- this file needs to be in the parent directory of the directory with IMU data txt files
        tree.write('myIMUmappings.xml')      
        
 
    
    
    
