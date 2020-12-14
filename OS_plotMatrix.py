# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:53:06 2020

@author: Joris Ravenhorst
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotMatrix(freq,t_calib,delay, Mat11,Mat21,Mat31,Mat12,Mat22,Mat32,Mat13,Mat23,Mat33):

    i_calib = freq*(t_calib)
   
  
    
    
    MatX = [0]*len(Mat11[i_calib:])
    for index in range(i_calib,len(Mat11)):
        MatX[index-i_calib] = [Mat11[index],Mat21[index],Mat31[index]]
    
    MatY = [0]*len(Mat11[i_calib:])
    for index in range(i_calib,len(Mat11)):
        MatY[index-i_calib] = [Mat12[index],Mat22[index],Mat32[index]]
    
    MatZ = [0]*len(Mat11[i_calib:])
    for index in range(i_calib,len(Mat11)):
        MatZ[index-i_calib] = [Mat13[index],Mat23[index],Mat33[index]]
        
    t_slider = np.arange(0,1,1/len(Mat11[i_calib:]))
        
    fig   = plt.figure()
    ax = fig.gca(projection='3d')
    
    
    MatXplot, = ax.plot([0,MatX[0][0]],[0,MatX[0][1]],[0,MatX[0][2]],'red')
    MatYplot, = ax.plot([0,MatY[0][0]],[0,MatY[0][1]],[0,MatY[0][2]],'green')
    MatZplot, = ax.plot([0,MatZ[0][0]],[0,MatZ[0][1]],[0,MatZ[0][2]],'blue')
    t_sliderplot, = ax.plot(t_slider[0],0,-1,'ro')
    ax.plot([0,1],[0,0],[-1,-1],'black')
    
    def animate(i):
        MatXplot.set_data_3d([0,MatX[i][0]], [0,MatX[i][1]], [0,MatX[i][2]])
        MatYplot.set_data_3d([0,MatY[i][0]], [0,MatY[i][1]], [0,MatY[i][2]])
        MatZplot.set_data_3d([0,MatZ[i][0]], [0,MatZ[i][1]], [0,MatZ[i][2]])
        t_sliderplot.set_data_3d(t_slider[i],0,-1)
    
        return MatXplot, MatYplot,MatZplot,t_sliderplot
    
    myAnimation = animation.FuncAnimation(fig, animate, frames=range(len(MatX)),interval=1,blit=True,repeat=False)
    plt.show
    
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    ax.set_xlim3d(-1,1)
    ax.set_ylim3d(-1,1)
    ax.set_zlim3d(-1,1)

    
    
 