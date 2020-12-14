# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:39:26 2020

@author: Joris Ravenhorst
"""

import json
import os

def createAngles_json(trial_dir_path,joints):
    # This function creates a .json file containing the joint angles of the analysed joint. 
    # The joint angles are retrieved from "orientations.mot".
    # Investigate joints determines which joints were monitored. 
    

    
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
        
        if joints[x_joint] == 'pelvis':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[1]: float(row[1]),
                    headers[2]: float(row[2]),
                    headers[3]: float(row[3]),
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
        if joints[x_joint] == 'knee_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[10]: float(row[10]),
                    headers[11]: float(row[11]),
                    })
        if joints[x_joint] == 'ankle_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[12]: float(row[12]),
                    })
        if joints[x_joint] == 'subtalar_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[13]: float(row[13]),
                    })
        if joints[x_joint] == 'mtp_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[14]: float(row[14]),
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
        if joints[x_joint] == 'knee_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[18]: float(row[18]),
                    headers[19]: float(row[19]),
                    })                
        if joints[x_joint] == 'ankle_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[20]: float(row[20]),
                    })
        if joints[x_joint] == 'subtalar_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[21]: float(row[21]),
                    })
        if joints[x_joint] == 'mtp_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[22]: float(row[22]),
                    })
        
        if joints[x_joint] == 'back':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[23]: float(row[23]),
                    headers[24]: float(row[24]),
                    headers[25]: float(row[25]),
                    })        

        if joints[x_joint] == 'shoulder_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[26]: float(row[26]),
                    headers[27]: float(row[27]),
                    headers[28]: float(row[28]),
                    })
        if joints[x_joint] == 'elbow_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[29]: float(row[29]),
                    })
        if joints[x_joint] == 'radioulnar_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[30]: float(row[30]),
                    })
        if joints[x_joint] == 'wrist_r':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[31]: float(row[31]),
                    headers[32]: float(row[32]),
                    })

        if joints[x_joint] == 'shoulder_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[33]: float(row[33]),
                    headers[34]: float(row[34]),
                    headers[35]: float(row[35]),
                    })
        if joints[x_joint] == 'elbow_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[36]: float(row[36]),
                    })
        if joints[x_joint] == 'radioulnar_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[37]: float(row[37]),
                    })
        if joints[x_joint] == 'wrist_l':
            for x in range(7,len(rows)):
                row = rows[x].split()
                data['data'][x_joint]['values'].append({
                    headers[0]: float(row[0]),  # time
                    headers[38]: float(row[38]),
                    headers[39]: float(row[39]),
                    })

                
    with open(trial_dir_path+'angles.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


