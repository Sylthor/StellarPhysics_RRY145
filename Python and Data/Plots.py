# Dear best Stellar Physics crew,
# This script should be able to generate the plots for our project.
# Here are the instructions:
# - 1) Depending on

import numpy as np
import matplotlib.pyplot as plt
import os

# Reads the data file, and stores each time index as a separate line in a list.
def getColumn(data,data_entry_index):
        # Extracts the column of the data file with list comprehension, and converts them to floats
        return [float(line.split()[data_entry_index]) for line in data if len(line.split()) > data_entry_index]
def addPlot(fileDirectory,detailed,xvalues,yvalues,timeIndex=0,xlog=False,ylog=False,scatter=False,flipXaxis=False):
    '''
    - (String) fileDirectory: Path to the folder where all files are.
    - (Boolean) detailed: Use detailed data structure or not?
    - (int) xvalues: Extracts values corresponding to the integer according to website instructions.
    - (int) yvalues: Extracts values corresponding to the integer according to website instructions.
    - (int) timeIndex: Use specific time index IF DETAILED==True.
    - (Boolean) loglog: Use loglog scales for the axis.
    - (Boolean) scatter: Use scatter plots.
    '''
    absolute_path = os.path.dirname(__file__)
    relative_path = fileDirectory
    full_path = os.path.join(absolute_path, relative_path)

    if detailed==False:
        dataInstances = [xvalues,yvalues]
        plotLabels = []
        f = open(full_path+"\\summary.txt", "r")
        data = f.read().split("\n")
        x = getColumn(data,xvalues-1)
        y = getColumn(data,yvalues-1)
        for i in range(2):
            if dataInstances[i]==1:
                plotLabels.append("Step number [1]")
            if dataInstances[i]==2:
                plotLabels.append("Age [years]")
            if dataInstances[i]==3:
                plotLabels.append("Mass [$M_\odot$]")
            if dataInstances[i]==4:
                plotLabels.append("Luminosity [$Log_{10}(L/L_\odot$]")
            if dataInstances[i]==5:
                plotLabels.append("Radius [$Log_{10}(R/R_\odot$]")
            if dataInstances[i]==6:
                plotLabels.append("Surface Temperature [$Log_{10}(T_{s}/1K)$]")
            if dataInstances[i]==7:
                plotLabels.append("Central Temperature [$Log_{10}(T_{c}/1K)$]")
            if dataInstances[i]==8:
                plotLabels.append(r"Central Density [$Log_{10}(\rho_{c}/kgm^{-3})$]")
            if dataInstances[i]==9:
                plotLabels.append("Central Pressure [$Log_{10}(P_{c}/Nm^{-2})$]")
            if dataInstances[i]==10:
                plotLabels.append(r"Central Electron Degeneracy Parameter $\psi_c$ [1]")
            if dataInstances[i]==11:
                plotLabels.append("Central Hydrogen Mass Fraction $X_c$ [1]")
            if dataInstances[i]==12:
                plotLabels.append("Central Helium Mass Fraction $Y_c$ [1]")
            if dataInstances[i]==13:
                plotLabels.append("Central Carbon Mass Fraction $X_{C,c}$ [1]")
            if dataInstances[i]==14:
                plotLabels.append("Central Nitrogen Mass Fraction $X_{N,c}$ [1]")
            if dataInstances[i]==15:
                plotLabels.append("Central Oxygen Mass Fraction $X_{O,c}$ [1]")
            if dataInstances[i]==16:
                plotLabels.append("Dynamical Timescale $\tau_{dyn}$ [seconds]")
            if dataInstances[i]==17:
                plotLabels.append("Kelvin-Helmholtz Timescale $\tau_{KH}$ [years]")
            if dataInstances[i]==18:
                plotLabels.append("Nuclear Timescale $\tau_{nuc}$ [years]")
            if dataInstances[i]==19:
                plotLabels.append("Luminosity from PP Chain $L_{PP}$ [$L_\odot$]")
            if dataInstances[i]==20:
                plotLabels.append("Luminosity from CNO Cycle $L_{CNO}$ [$L_\odot$]")
            if dataInstances[i]==21:
                plotLabels.append(r"Luminosity from $3\alpha$ reactions $L_{3\alpha}$ [$L_\odot$]")
        M = getColumn(data,3-1)[0]
        Z = 1-getColumn(data,11-1)[0]-getColumn(data,12-1)[0]
        print("M =",M)
        print("Z =",Z)
        plt.xlabel(plotLabels[0])
        plt.ylabel(plotLabels[1])
        # plt.ticklabel_format(style='sci',axis='y')
        if flipXaxis==True:
            plt.gca().invert_xaxis()
        if xlog==True:
            plt.xscale("log")
        if ylog==True:
            plt.yscale("log")
        if scatter==True:
            plt.scatter(x,y)
        else:
            plt.plot(x,y)
    if detailed==True:
        f = open(full_path+"\\structure_"+str(f'{timeIndex:05}')+".txt", "r")
        data = f.read().split("\n")
        x = getColumn(data,xvalues-1)
        y = getColumn(data,yvalues-1)
        if flipXaxis==True:
            plt.gca().invert_xaxis()
        if xlog==True:
            plt.xscale("log")
        if ylog==True:
            plt.yscale("log")
        if scatter==True:
            plt.scatter(x,y)
        else:
            plt.plot(x,y)
# ------------ Add graphs here ------------ #
import os
# addPlot("M=5, Z=0,03",False,2,21,scatter=True,xlog=True,ylog=True,flipXaxis=False)

# Example: My folder is called "M=5, Z=0,03". I want to create HR-diagram
addPlot("M=5, Z=0,02",True,6,4,scatter=False,flipXaxis=True)
# ------------------------ #
plt.show()