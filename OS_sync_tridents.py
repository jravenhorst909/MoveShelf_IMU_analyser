# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:50:22 2020

@author: Joris Ravenhorst
"""

def sync_tridents(t0,txtfilenames,freq):
    t0_latest = max(t0)
        
    count = 0
    for x in t0:
        fh = open(txtfilenames[count],'r')
        rows = fh.readlines()
        
        PacketCounter = [0]*(len(rows)-6)
        SampletimeFine = [0]*(len(rows)-6)
        Mat11 = [0]*(len(rows)-6)
        Mat21 = [0]*(len(rows)-6)
        Mat31 = [0]*(len(rows)-6)
        Mat12 = [0]*(len(rows)-6)
        Mat22 = [0]*(len(rows)-6)
        Mat32 = [0]*(len(rows)-6)
        Mat13 = [0]*(len(rows)-6)
        Mat23 = [0]*(len(rows)-6)
        Mat33 = [0]*(len(rows)-6)
        
        for x in range(len(rows)-6):
            PacketCounter[x] = int(rows[x+6].split('\t')[0])
            SampletimeFine[x] = float(rows[x+6].split('\t')[1])
            Mat11[x] = float(rows[x+6].split('\t')[2])
            Mat21[x] = float(rows[x+6].split('\t')[3])
            Mat31[x] = float(rows[x+6].split('\t')[4])
            Mat12[x] = float(rows[x+6].split('\t')[5])
            Mat22[x] = float(rows[x+6].split('\t')[6])
            Mat32[x] = float(rows[x+6].split('\t')[7])
            Mat13[x] = float(rows[x+6].split('\t')[8])
            Mat23[x] = float(rows[x+6].split('\t')[9])
            Mat33[x] = float(rows[x+6].split('\t')[10])
        
        t0_ind = SampletimeFine.index(min(SampletimeFine, key=lambda x:abs(x-t0_latest)))
        fh.close()
    
        if t0_ind != 0:
            del PacketCounter[-t0_ind:]
            del SampletimeFine[:t0_ind]
            del Mat11[:t0_ind]
            del Mat21[:t0_ind]
            del Mat31[:t0_ind]
            del Mat12[:t0_ind]
            del Mat22[:t0_ind]
            del Mat32[:t0_ind]
            del Mat13[:t0_ind]
            del Mat23[:t0_ind]
            del Mat33[:t0_ind]
        

        with open(txtfilenames[count],'w') as fh:
            fh.write('// Start Time: Unknown'"\n"
                     '// Update Rate: {}.0Hz'"\n"
                     '// Filter Profile: human (46.1)'"\n"
                     '// Option Flags: AHS Disabled ICC Disabled '"\n"
                     '// Firmware Version: 4.0.2'"\n".format(freq))                     
    
            fh.write('PacketCounter\tSampleTimeFine\tMat[1][1]\tMat[2][1]\tMat[3][1]\tMat[1][2]\tMat[2][2]\tMat[3][2]\tMat[1][3]\tMat[2][3]\tMat[3][3]'"\n")
            
            count2 = 0
            for x in PacketCounter:
                fh.write("%s" % '{}'.format(PacketCounter[count2])+'\t{}'.format(SampletimeFine[count2])+'\t{}'.format(Mat11[count2])+'\t{}'.format(Mat21[count2])+'\t{}'.format(Mat31[count2])+'\t{}'.format(Mat12[count2])+'\t{}'.format(Mat22[count2])+'\t{}'.format(Mat32[count2])+'\t{}'.format(Mat13[count2])+'\t{}'.format(Mat23[count2])+'\t{}\n'.format(Mat33[count2]))
                count2 += 1

    count+=1
        
        
        
        
        
        