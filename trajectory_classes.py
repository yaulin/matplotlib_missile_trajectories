#!/usr/bin/python

# Yaroslav Aulin
# mail@yaulin.net
#
# version 07
# 2021-05-22
# load necessary libraries

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

import os

# apply seaborn styles

sns.set_context('talk')
sns.set_style('darkgrid')

class trajectory:
    
    data = pd.DataFrame()     #trajectory data
    fpath = ""                #file path
    fname = ""
    save = False              # save plots to files (don't save by default)
    dpi = 300                 # resolution of figures
    
    # default plot parameters
    
    color = 'mediumvioletred'
    lw = 3
    figsizeX = 6.4
    figsizeY = 4.8
    
    
    def __init__(self,f):
        self.fpath = f  # save file path
        bn = os.path.basename(f)
        self.fname = os.path.splitext(bn)[0]
        
        self.data = pd.read_csv(f)
        self.data.rename(columns = {'TTIME_S':'Time',
                                    'TRXI_M':'X Position', 
                                    'TRYI_M':'Y Position', 
                                    'TRZI_M':'Z Position',
                                    'TGRNKM_KM':'Ground Range', 
                                    'TALTKM_KM':'Altitude',
                                    'TDRNGE_M':'Downrange',
                                    'TCRNGE_M':'Crossrange',
                                    'TVRMAG_M/S':'Velocity',
                                    'TAIMAG_M/S2':'Acceleration',
                                    'TABXB_M/S2':'Acceleration X',
                                    'TABYB_M/S2':'Acceleration Y',
                                    'TABZB_M/S2':'Acceleration Z',
                                    'TPITCH_DEG':'Pitch Angle',
                                    'THEADG_DEG':'Heading Angle', 
                                    'TAMACH':'Mach'
                                                                   }, inplace = True)
        
        # convert X, Y, Z positions, crossrange and downrange to km
        
        self.data['X Position'] = self.data['X Position'] * 1e-3
        self.data['Y Position'] = self.data['Y Position'] * 1e-3
        self.data['Z Position'] = self.data['Z Position'] * 1e-3
        
        self.data['Downrange'] = self.data['Downrange'] * 1e-3
        self.data['Crossrange'] = self.data['Crossrange'] * 1e-3
        
        
        
    # change default parameters
    
    def set_color(self,color):
        self.color = color
        
    def set_lw(self, lw):
        self.lw = lw
        
    def sef_figsize(self,figsizeX,figsizeY):
        self.figsizeX = figsizeX
        self.figsizeY = figsizeY
        
    def enable_saving(self):
        self.save = True
        
    def disable_saving(self):
        self.save = False
    
        
    # plotting functions
    
    
    
    # Time plots
    
   
    # X vs Time
    
    def plot_xt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'X Position', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "X Position, km"
            )

        
        
        if self.save:
            plt.savefig(self.fname + '_xt.png',dpi = 300)
            
        plt.show()
        
        
        
    # Y vs Time
    
    def plot_yt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Y Position', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Y Position, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_yt.png',dpi = 300)
            
       
        plt.show()
        
    # Z vs Time
    
    def plot_zt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Z Position', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Z Position, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_zt.png',dpi = 300)
            
        
        plt.show()
        
    # Ground Range vs Time
    
    def plot_grt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Ground Range', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Ground Range, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_grt.png',dpi = 300)
            
        
        plt.show()
    
    # Altitude vs Time
    
    def plot_alt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Altitude', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Altitude, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_alt.png',dpi = 300)
            
        
        plt.show()
        
        
    # Downrange vs Time
    
    def plot_drt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Downrange', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Downrange, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_drt.png',dpi = 300)
            
        
        plt.show()
        
    # Crossrange vs Time
    
    def plot_crt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Crossrange', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Crossrange, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_crt.png',dpi = 300)
            
        
        plt.show()
        
        
    # Velocity vs Time
    
    def plot_vt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Velocity', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Earth relative velocity, m/s"
            )
        
        if self.save:
            plt.savefig(self.fname + '_vt.png',dpi = 300)
            
        
        plt.show()
        
        
    # Acceleration vs Time
    
    def plot_at(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Acceleration', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration, m/s$^2$"
            )
        
        if self.save:
            plt.savefig(self.fname + '_at.png',dpi = 300)
            
        
        plt.show()
        
    # Acceleration X vs Time
    
    def plot_axt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Acceleration X', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration X, m/s$^2$"
            )
        
        if self.save:
            plt.savefig(self.fname + '_axt.png',dpi = 300)
            
        
        plt.show()
        
    # Acceleration Y vs Time
    
    def plot_ayt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Acceleration Y', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration Y, m/s$^2$"
            )
        
        if self.save:
            plt.savefig(self.fname + '_ayt.png',dpi = 300)
            
        
        plt.show()
         
    # Acceleration Z vs Time
    
    def plot_azt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Acceleration Z', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration Z, m/s$^2$"
            )
        
        if self.save:
            plt.savefig(self.fname + '_azt.png',dpi = 300)
            
        
        plt.show()
        
        
    # Pitch Angle vs Time
    
    
    def plot_pat(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Pitch Angle', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Pitch Angle, deg"
            )
        
        if self.save:
            plt.savefig(self.fname + '_pat.png',dpi = 300)
            
        
        plt.show()
        
        
    # Pitch Angle vs Time
    
    
    def plot_hat(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Heading Angle', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Heading Angle, deg"
            )
        
        if self.save:
            plt.savefig(self.fname + '_hat.png',dpi = 300)
            
        
        plt.show()
        
        
    # Mach vs Time
    
    
    def plot_mt(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Time',
            'Mach', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Mach"
            )
        
        if self.save:
            plt.savefig(self.fname + '_mt.png',dpi = 300)
            
        
        plt.show()
        
        
        
    # Other plots


   # Altitude vs Mach
    
    
    def plot_am(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Mach',
            'Altitude', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Mach",
            ylabel = "Altitude, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_am.png',dpi = 300)
            
        
        plt.show()
        
   # Altitude vs Velocity
    
    
    def plot_av(self):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        plt.plot(
            'Velocity',
            'Altitude', 
            data=self.data, 
            marker= None , color= self.color, lw = self.lw
            )
        
        ax.set(
            xlabel = "Velocity, m/s",
            ylabel = "Altitude, km"
            )
        
        if self.save:
            plt.savefig(self.fname + '_av.png',dpi = 300)
            
        
        plt.show()
        
        
    # 3D plots
    
    # XYZ
    
    def plot_xyz(self):
        
        #fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        ax = plt.figure().add_subplot(projection='3d')
        
        ax.plot(
            self.data['X Position'],
            self.data['Y Position'],
            self.data['Z Position'],
            color = self.color,
            lw = self.lw
            )
        
        ax.set(
            xlabel = 'X, km',
            ylabel = 'Y, km',
            zlabel = 'Z, km'
            )
        
        if self.save:
            plt.savefig(self.fname + '_xyz.png',dpi = 300)
            

        
        plt.show()
        
        
    # Downrange, Crossrange, Altitude
        
    def plot_3D(self):
        
        #fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        ax = plt.figure().add_subplot(projection='3d')
        
        ax.plot(
            self.data['Downrange'],
            self.data['Crossrange'],
            self.data['Altitude'],
            color = self.color,
            lw = self.lw
            )
        
        ax.set(
            xlabel = 'Downrange, km',
            ylabel = 'Crossrange, km',
            zlabel = 'Altitude, km'
            )
        
        if self.save:
            plt.savefig(self.fname + '_3D.png',dpi = 300)
            

        
        plt.show()
        
# class containing all trajectories in a directory

class trajectory_dir:
    
    tdict = {}
    flist = []
    
    
    save = False              # save plots to files (don't save by default)
    dpi = 300                 # resolution of figures
    
    # default plot parameters
    
    color = 'mediumvioletred'
    lw = 3
    figsizeX = 6.4
    figsizeY = 4.8
    
    
    
    def __init__(self, dir1):
        flist = os.listdir(dir1)
        
        i = 0

        for f in flist:
            if (os.path.splitext(f)[-1] != '.CSV'):
                del flist[i]
            i+=1
            
            
        flist.sort()
        
        self.flist = flist
        
        
        for f in flist:
            fname = os.path.splitext(f)[0]
            self.tdict[fname] = trajectory(dir1 + f)
            
     
    
    # plot all independent plots for each trajectory
    
    def plot_all_separate(self, save = False):
        
        
        if save == True:
            for fname in self.tdict:
                self.tdict[fname].enable_saving()
                
        if save == False:
            for fname in self.tdict:
                self.tdict[fname].disable_saving()
            
        
        for fname in self.tdict:
            
            print("Trajectory: " + fname)
            
            self.tdict[fname].plot_xt()
            self.tdict[fname].plot_yt()
            self.tdict[fname].plot_zt()
            
            self.tdict[fname].plot_grt()
            self.tdict[fname].plot_alt()
       
            
            self.tdict[fname].plot_drt()
            self.tdict[fname].plot_crt()
            
            self.tdict[fname].plot_vt()

            self.tdict[fname].plot_at()
            self.tdict[fname].plot_axt()
            self.tdict[fname].plot_ayt()
            self.tdict[fname].plot_azt()

            self.tdict[fname].plot_pat()
            self.tdict[fname].plot_hat()

            self.tdict[fname].plot_mt()
            
            self.tdict[fname].plot_am()
            self.tdict[fname].plot_av()

            self.tdict[fname].plot_xyz()
            self.tdict[fname].plot_3D()
            
            
            
    
            
            
    def plot_combined_xt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'X Position', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "X Position, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
                       
        if save:
            plt.savefig('combined_xt.png',dpi = 300)
        
        plt.show()
        
        
                
    def plot_combined_yt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Y Position', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Y Position, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_yt.png',dpi = 300)
        
        plt.show()
        
                    
    def plot_combined_zt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Z Position', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Z Position, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_zt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_zt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Z Position', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Z Position, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_zt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_grt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Ground Range', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Ground Range, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_grt.png',dpi = 300)
        
        plt.show()
        
        
        
    def plot_combined_alt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Altitude', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Altitude, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_alt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_drt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Downrange', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Downrange, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_drt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_crt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Crossrange', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Crossrange, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_crt.png',dpi = 300)
        
        plt.show()
        
    def plot_combined_vt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Velocity', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Velocity, m/s"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_vt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_at(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Acceleration', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration, m/s$^2$"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_at.png',dpi = 300)
        
        plt.show()
        
        
        
    def plot_combined_axt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Acceleration X', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration X, m/s$^2$"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_axt.png',dpi = 300)
        
        plt.show()
        
    def plot_combined_ayt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Acceleration Y', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration Y, m/s$^2$"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_ayt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_azt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Acceleration Z', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Acceleration Z, m/s$^2$"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_azt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_pat(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Pitch Angle', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Pitch Angle, deg"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_pat.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_hat(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Heading Angle', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Heading Angle, deg"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_pat.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_mt(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Time',
                'Mach', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Time, s",
            ylabel = "Mach"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_mt.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_am(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Mach',
                'Altitude', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Mach",
            ylabel = "Altitude, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_am.png',dpi = 300)
        
        plt.show()
        
        
    
        
    def plot_combined_av(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Velocity',
                'Altitude', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Velocity, m/s",
            ylabel = "Altitude, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_av.png',dpi = 300)
        
        plt.show()
        
        
    def plot_combined_agr(self, save = False):
        
        fig, ax = plt.subplots(figsize = (self.figsizeX,self.figsizeY))
        
        for fname in self.tdict: 
                   
            plt.plot(
                'Ground Range',
                'Altitude', 
                data=self.tdict[fname].data, 
                lw = self.lw,
                label = fname
                )
        
        ax.set(
            xlabel = "Ground Range, km",
            ylabel = "Altitude, km"
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")
        
        if save:
            plt.savefig('combined_agr.png',dpi = 300)
        
        plt.show()
        
        
        
        
    # 3D plots
    
    def plot_combined_xyz(self, save = False):
            
        ax = plt.figure().add_subplot(projection='3d')
        
        
        for fname in self.tdict: 
        
            ax.plot(
                self.tdict[fname].data['X Position'],
                self.tdict[fname].data['Y Position'],
                self.tdict[fname].data['Z Position'],
                lw = self.lw
                )
            
        ax.set(
            xlabel = 'X, km',
            ylabel = 'Y, km',
            zlabel = 'Z, km'
            )
        
        if save:
            plt.savefig('combined_xyz.png',dpi = 300)
            

        
        plt.show()
        
    def plot_combined_3D(self, save = False):
            
        ax = plt.figure().add_subplot(projection='3d')
        
        
        for fname in self.tdict: 
        
            ax.plot(
                self.tdict[fname].data['Downrange'],
                self.tdict[fname].data['Crossrange'],
                self.tdict[fname].data['Altitude'],
                lw = self.lw
                )
            
        ax.set(
            xlabel = 'Downrange, km',
            ylabel = 'Crossrange, km',
            zlabel = 'Altitude, km'
            )
        
        if save:
            plt.savefig('combined_3D.png',dpi = 300)
            
        
        
        
        plt.show()
        
        
    def plot_combined_end_2D(self, save = False):
            
        ax = plt.figure().add_subplot()
        
        
        for fname in self.tdict: 
        
            ax.scatter(
                self.tdict[fname].data['Downrange'].iloc[-1],
                self.tdict[fname].data['Crossrange'].iloc[-1],
                marker = 'o',
                label = fname
                )
            
        ax.set(
            xlabel = 'Downrange, km',
            ylabel = 'Crossrange, km'
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")

        
        if save:
            plt.savefig('combined_end_2D.png',dpi = 300)
            
        
        
        
        plt.show()
        
        
    def plot_combined_end_xyz(self, save = False):
            
        ax = plt.figure().add_subplot(projection='3d')
        
        
        for fname in self.tdict: 
        
            ax.scatter(
                self.tdict[fname].data['X Position'].iloc[-1],
                self.tdict[fname].data['Y Position'].iloc[-1],
                self.tdict[fname].data['Z Position'].iloc[-1],

                marker = 'o',
                label = fname
                )
            
        ax.set(
            xlabel = 'X Position, km',
            ylabel = 'Y Position, km',
            zlabel = 'Z Position, km'
            )
        
        ax.legend(bbox_to_anchor=(1,1), loc="upper left")

        
        if save:
            plt.savefig('combined_end_3D.png',dpi = 300)
            
        
        
        
        plt.show()        

    
        
           
        
           
        
    
        
        
        

