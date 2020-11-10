# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:39:26 2020

@author: Joris Ravenhorst
"""

import json
import os

def createAngles_json(trial_dir_path,joints):
    for file in os.listdir(trial_dir_path):
        if file.endswith('.mot'):
            motfile = file


    fh = open(trial_dir_path+motfile,'r')
    rows = fh.readlines()
    headers = rows[6].split()


    data = {}
    data['data'] = []    
    
    for x_joint in range(len(joints)):
        data['data'].append({
            'label': joints[x_joint],
            'description': '',
            'values': [],
            'unit': 'deg'
            })
        
        if joints[x_joint] == 'hip_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[7]: float(row[7]),
                    headers[8]: float(row[8]),
                    headers[9]: float(row[9]),
                    })
        if joints[x_joint] == 'hip_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[15]: float(row[15]),
                    headers[16]: float(row[16]),
                    headers[17]: float(row[17]),
                    })
        if joints[x_joint] == 'knee_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[10]: float(row[10]),
                    headers[11]: float(row[11]),
                    })
        if joints[x_joint] == 'knee_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[18]: float(row[18]),
                    headers[19]: float(row[19]),
                    })                
                
    with open(trial_dir_path+'angles.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


