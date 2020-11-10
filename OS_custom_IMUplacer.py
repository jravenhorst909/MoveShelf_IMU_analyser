# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:48:07 2020

@author: Joris Ravenhorst
"""

import xml.etree.ElementTree as ET

def custom_IMUplacer(calibrated_model_path):
    pelvis_imu_transl = '-0.18 0.06 0'
    femur_r_imu_transl = '0.05 -0.28 0.03'
    femur_l_imu_transl = '0.05 -0.28 -0.03'
    tibia_r_imu_transl = '0.03 -0.25 0'
    tibia_l_imu_transl = '0.03 -0.25 0'
    
    tree = ET.parse(calibrated_model_path)
    
    pelvis_imu = tree.find(".//PhysicalOffsetFrame[@name='pelvis_imu']/translation")    
    pelvis_imu.text = pelvis_imu_transl
    pelvis_imu.set('custom','yes')

    femur_r_imu = tree.find(".//PhysicalOffsetFrame[@name='femur_r_imu']/translation")    
    femur_r_imu.text = femur_r_imu_transl
    femur_r_imu.set('custom','yes')

    femur_l_imu = tree.find(".//PhysicalOffsetFrame[@name='femur_l_imu']/translation")    
    femur_l_imu.text = femur_l_imu_transl
    femur_l_imu.set('custom','yes')

    tibia_r_imu = tree.find(".//PhysicalOffsetFrame[@name='tibia_r_imu']/translation")    
    tibia_r_imu.text = tibia_r_imu_transl
    tibia_r_imu.set('custom','yes')

    tibia_l_imu = tree.find(".//PhysicalOffsetFrame[@name='tibia_l_imu']/translation")    
    tibia_l_imu.text = tibia_l_imu_transl
    tibia_l_imu.set('custom','yes')

    # overwrite existing calibrated .osim mdoel file
    tree.write(calibrated_model_path)
