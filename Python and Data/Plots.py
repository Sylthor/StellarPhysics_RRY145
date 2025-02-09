# Dear best Stellar Physics crew,
# This script should be able to generate the plots for our project.
# Here are the instructions:
# - 1) Depending on


# IMPORTANT NOTES!!!
# - M=5, Z=0,0003 does NOT display values correctly. 1-X+Y=0,001 for some reason.
import numpy as np
import matplotlib.pyplot as plt
import os

# s = [1,2,3,4,5,6,7]
# a = 0
# b = 1
# print(s[:b][a:])

# Reads the data file, and stores each time index as a separate line in a list.
def getColumn(data,data_entry_index):
        # Extracts the column of the data file with list comprehension, and converts them to floats
        return [float(line.split()[data_entry_index]) for line in data if len(line.split()) > data_entry_index]
def addPlot(fileDirectory,detailed,xvalues,yvalues,timeIndex=0,singelTimeInstance=False,xlog=False,ylog=False,scatter=False,flipXaxis=False):
    '''
    - (String) fileDirectory: Path to the folder where all files are.
    - (Boolean) detailed: Use detailed data structure or not?
    - (int) xvalues: Extracts values corresponding to the integer according to website instructions.
    - (int) yvalues: Extracts values corresponding to the integer according to website instructions.
    - (int) timeIndex: Use specific time index IF DETAILED==True.
    - (Boolean) singelTimeInstance: Use only one instance IF DETAILED==False.
    - (Boolean) xlog:
    - (Boolean) ylog:
    - (Boolean) scatter: Use scatter plots.
    - (Boolean) flipXaxis:
    '''
    absolute_path = os.path.dirname(__file__)
    relative_path = fileDirectory
    full_path = os.path.join(absolute_path, relative_path)

    if detailed==False:
        dataInstances = [xvalues,yvalues]
        plotLabels = []
        f = open(full_path+"\\summary.txt", "r")
        data = f.read().split("\n")
        x = 0
        y = 0
        if(xvalues <30):
            x = getColumn(data,xvalues-1)
        if(xvalues==30):
            # Gets metallicity
            x = 1-np.array(getColumn(data,11-1))-np.array(getColumn(data,12-1))
        if(yvalues <30):
            y = getColumn(data,yvalues-1)
        if(yvalues==30):
            # Gets metallicity
            x = 1-np.array(getColumn(data,11-1))-np.array(getColumn(data,12-1))
        if singelTimeInstance==True:
            x = x[timeIndex]
            y = y[timeIndex]
        # if timeIndex != [-1,-1]:
        #     x = x[:]
        #     y = y[:]
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
                plotLabels.append(r"Dynamical Timescale $\tau_{dyn}$ [seconds]")
            if dataInstances[i]==17:
                plotLabels.append(r"Kelvin-Helmholtz Timescale $\tau_{KH}$ [years]")
            if dataInstances[i]==18:
                plotLabels.append(r"Nuclear Timescale $\tau_{nuc}$ [years]")
            if dataInstances[i]==19:
                plotLabels.append("Luminosity from PP Chain $L_{PP}$ [$L_\odot$]")
            if dataInstances[i]==20:
                plotLabels.append("Luminosity from CNO Cycle $L_{CNO}$ [$L_\odot$]")
            if dataInstances[i]==21:
                plotLabels.append(r"Luminosity from $3\alpha$ reactions $L_{3\alpha}$ [$L_\odot$]")
            if dataInstances[i]==22:
                plotLabels.append("Luminosity from Metal Burning $L_{Z}$ [$L_\odot$]")
            if dataInstances[i]==23:
                plotLabels.append("Luminosity from Neutrino Losses $L_{v}$ [$L_\odot$]")
            if dataInstances[i]==24:
                plotLabels.append("Mass of Helium Core $M_{He}$ [$M_\odot$]")
            if dataInstances[i]==25:
                plotLabels.append("Mass of Carbon Core $M_{C}$ [$M_\odot$]")
            if dataInstances[i]==26:
                plotLabels.append("Mass of Oxygen Core $M_{O}$ [$M_\odot$]")
            if dataInstances[i]==27:
                plotLabels.append("Radius of Helium Core $R_{He}$ [$R_\odot$]")
            if dataInstances[i]==28:
                plotLabels.append("Radius of Carbon Core $R_{C}$ [$R_\odot$]")
            if dataInstances[i]==29:
                plotLabels.append("Radius of Oxygen Core $R_{O}$ [$R_\odot$]")
            # ------------ Metallicity is not strictly in the files ------------
            if dataInstances[i]==30:
                plotLabels.append("Central Metallicity Mass Fraction $Z_c$ [1]")
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
## Test plot, make no conclusions from this
# addPlot("ezweb_29007",False,2,18,scatter=False)
# addPlot("M=5, Z=0,001",False,2,18,scatter=False)
# addPlot("M=5, Z=0,0003",False,2,18,scatter=False)
# addPlot("M=5, Z=0,0001",False,2,18,scatter=False)
# plt.show()

## M=constant=5, grid of metallicities
Z = ["0,0001","0,0003","0,001","0,004","0,01"]
for z in Z:
    addPlot("M=5, Z="+z,False,30,7,singelTimeInstance=True,timeIndex=2,scatter=True)
plt.show()
## Example: My folder is called "M=5, Z=0,03". I want to create HR-diagram
# addPlot("M=5, Z=0,02",False,6,4,scatter=False,flipXaxis=True)
# plt.show()

# ------------------------ #