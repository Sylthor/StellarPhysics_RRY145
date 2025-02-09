# Dear best Stellar Physics crew,
# This script should be able to generate the plots for our project.
# Here are the instructions:
# - 1) Depending on


# IMPORTANT NOTES!!!
# - M=5, Z=0,0003 does NOT display values correctly. 1-X+Y=0,001 for some reason.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams.update({'font.size': 16})
plt.rcParams.update({
    "font.family": "serif",  # Use a serif font
    "pgf.rcfonts": False,
})

# Reads the data file, and stores each time index as a separate line in a list.
def getColumn(data,data_entry_index):
        # Extracts the column of the data file with list comprehension, and converts them to floats
        return [float(line.split()[data_entry_index]) for line in data if len(line.split()) > data_entry_index]
def addPlot(fileDirectory,detailed,xvalues,
            yvalues,ax,timeIndex=0,
            singelTimeInstance=False,xlog=False,ylog=False,
            scatter=False,flipXaxis=False,customX=[-1],
            legendText="",color="orange"):
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
            y = 1-np.array(getColumn(data,11-1))-np.array(getColumn(data,12-1))
        if singelTimeInstance==True:
            x = x[timeIndex]
            y = y[timeIndex]
        if customX != [-1]:
            x = customX
        
        dataInstances = [xvalues,yvalues]
        plotLabels = []
        for i in range(2):
            if dataInstances[i]==1:
                plotLabels.append("Step number [1]")
            if dataInstances[i]==2:
                plotLabels.append("$t$ [years]")
            if dataInstances[i]==3:
                plotLabels.append("$M$ [$M_\odot$]")
            if dataInstances[i]==4:
                plotLabels.append("$L$ [$Log_{10}(L/L_\odot$]")
            if dataInstances[i]==5:
                plotLabels.append("$R$ [$Log_{10}(R/R_\odot$]")
            if dataInstances[i]==6:
                plotLabels.append("$T_s$ [$Log_{10}(T_{s}/1K)$]")
            if dataInstances[i]==7:
                plotLabels.append("$T_c$ [$Log_{10}(T_{c}/1K)$]")
            if dataInstances[i]==8:
                plotLabels.append(r"$\rho_c$ [$Log_{10}(\rho_{c}/kgm^{-3})$]")
            if dataInstances[i]==9:
                plotLabels.append("$P_c$ [$Log_{10}(P_{c}/Nm^{-2})$]")
            if dataInstances[i]==10:
                plotLabels.append(r"$\psi_c$ [1]")
            if dataInstances[i]==11:
                plotLabels.append("$X_c$ [1]")
            if dataInstances[i]==12:
                plotLabels.append("$Y_c$ [1]")
            if dataInstances[i]==13:
                plotLabels.append("$X_{C,c}$ [1]")
            if dataInstances[i]==14:
                plotLabels.append("$X_{N,c}$ [1]")
            if dataInstances[i]==15:
                plotLabels.append("$X_{O,c}$ [1]")
            if dataInstances[i]==16:
                plotLabels.append(r"$\tau_{dyn}$ [seconds]")
            if dataInstances[i]==17:
                plotLabels.append(r"$\tau_{KH}$ [years]")
            if dataInstances[i]==18:
                plotLabels.append(r"$\tau_{nuc}$ [years]")
            if dataInstances[i]==19:
                plotLabels.append("$L_{PP}$ [$L_\odot$]")
            if dataInstances[i]==20:
                plotLabels.append("$L_{CNO}$ [$L_\odot$]")
            if dataInstances[i]==21:
                plotLabels.append(r"$L_{3\alpha}$ [$L_\odot$]")
            if dataInstances[i]==22:
                plotLabels.append("$L_{Z}$ [$L_\odot$]")
            if dataInstances[i]==23:
                plotLabels.append("$L_{v}$ [$L_\odot$]")
            if dataInstances[i]==24:
                plotLabels.append("$M_{He}$ [$M_\odot$]")
            if dataInstances[i]==25:
                plotLabels.append("$M_{C}$ [$M_\odot$]")
            if dataInstances[i]==26:
                plotLabels.append("$M_{O}$ [$M_\odot$]")
            if dataInstances[i]==27:
                plotLabels.append("$R_{He}$ [$R_\odot$]")
            if dataInstances[i]==28:
                plotLabels.append("$R_{C}$ [$R_\odot$]")
            if dataInstances[i]==29:
                plotLabels.append("$R_{O}$ [$R_\odot$]")
            # ------------ Metallicity is not strictly in the files ------------
            if dataInstances[i]==30:
                plotLabels.append("$Z_c$ [1]")
            # if dataInstances[i]==1:
            #     plotLabels.append("Step number [1]")
            # if dataInstances[i]==2:
            #     plotLabels.append("Age [years]")
            # if dataInstances[i]==3:
            #     plotLabels.append("Mass [$M_\odot$]")
            # if dataInstances[i]==4:
            #     plotLabels.append("Luminosity [$Log_{10}(L/L_\odot$]")
            # if dataInstances[i]==5:
            #     plotLabels.append("Radius [$Log_{10}(R/R_\odot$]")
            # if dataInstances[i]==6:
            #     plotLabels.append("Surface Temperature [$Log_{10}(T_{s}/1K)$]")
            # if dataInstances[i]==7:
            #     plotLabels.append("Central Temperature [$Log_{10}(T_{c}/1K)$]")
            # if dataInstances[i]==8:
            #     plotLabels.append(r"Central Density [$Log_{10}(\rho_{c}/kgm^{-3})$]")
            # if dataInstances[i]==9:
            #     plotLabels.append("Central Pressure [$Log_{10}(P_{c}/Nm^{-2})$]")
            # if dataInstances[i]==10:
            #     plotLabels.append(r"Central Electron Degeneracy Parameter $\psi_c$ [1]")
            # if dataInstances[i]==11:
            #     plotLabels.append("Central Hydrogen Mass Fraction $X_c$ [1]")
            # if dataInstances[i]==12:
            #     plotLabels.append("Central Helium Mass Fraction $Y_c$ [1]")
            # if dataInstances[i]==13:
            #     plotLabels.append("Central Carbon Mass Fraction $X_{C,c}$ [1]")
            # if dataInstances[i]==14:
            #     plotLabels.append("Central Nitrogen Mass Fraction $X_{N,c}$ [1]")
            # if dataInstances[i]==15:
            #     plotLabels.append("Central Oxygen Mass Fraction $X_{O,c}$ [1]")
            # if dataInstances[i]==16:
            #     plotLabels.append(r"Dynamical Timescale $\tau_{dyn}$ [seconds]")
            # if dataInstances[i]==17:
            #     plotLabels.append(r"Kelvin-Helmholtz Timescale $\tau_{KH}$ [years]")
            # if dataInstances[i]==18:
            #     plotLabels.append(r"Nuclear Timescale $\tau_{nuc}$ [years]")
            # if dataInstances[i]==19:
            #     plotLabels.append("Luminosity from PP Chain $L_{PP}$ [$L_\odot$]")
            # if dataInstances[i]==20:
            #     plotLabels.append("Luminosity from CNO Cycle $L_{CNO}$ [$L_\odot$]")
            # if dataInstances[i]==21:
            #     plotLabels.append(r"Luminosity from $3\alpha$ reactions $L_{3\alpha}$ [$L_\odot$]")
            # if dataInstances[i]==22:
            #     plotLabels.append("Luminosity from Metal Burning $L_{Z}$ [$L_\odot$]")
            # if dataInstances[i]==23:
            #     plotLabels.append("Luminosity from Neutrino Losses $L_{v}$ [$L_\odot$]")
            # if dataInstances[i]==24:
            #     plotLabels.append("Mass of Helium Core $M_{He}$ [$M_\odot$]")
            # if dataInstances[i]==25:
            #     plotLabels.append("Mass of Carbon Core $M_{C}$ [$M_\odot$]")
            # if dataInstances[i]==26:
            #     plotLabels.append("Mass of Oxygen Core $M_{O}$ [$M_\odot$]")
            # if dataInstances[i]==27:
            #     plotLabels.append("Radius of Helium Core $R_{He}$ [$R_\odot$]")
            # if dataInstances[i]==28:
            #     plotLabels.append("Radius of Carbon Core $R_{C}$ [$R_\odot$]")
            # if dataInstances[i]==29:
            #     plotLabels.append("Radius of Oxygen Core $R_{O}$ [$R_\odot$]")
            # # ------------ Metallicity is not strictly in the files ------------
            # if dataInstances[i]==30:
            #     plotLabels.append("Central Metallicity Mass Fraction $Z_c$ [1]")
        M = getColumn(data,3-1)[0]
        t = 0
        Z = 1-getColumn(data,11-1)[t]-getColumn(data,12-1)[t]
        print("M =",M)
        print("Z =",Z)
        ax.set_xlabel(plotLabels[0])
        ax.set_ylabel(plotLabels[1])
        # plt.ticklabel_format(style='sci',axis='y')
        if flipXaxis==True:
            ax.invert_xaxis()
        if xlog==True:
            ax.set_xscale("log")
        if ylog==True:
            ax.set_yscale("log")
        if scatter==True:
            ax.scatter(x,y,label=legendText)
        else:
            ax.plot(x,y,label=legendText)
    if detailed==True:
        f = open(full_path+"\\structure_"+str(f'{timeIndex:05}')+".txt", "r")
        data = f.read().split("\n")

        x = getColumn(data,xvalues-1)
        y = getColumn(data,yvalues-1)

        dataInstances = [xvalues,yvalues]
        plotLabels = []
        for i in range(2):
            if dataInstances[i]==1:
                plotLabels.append("$M_r$ [$M_\odot$]")
            if dataInstances[i]==2:
                plotLabels.append("$r$ [$R_\odot$]")
            if dataInstances[i]==3:
                plotLabels.append("$L_r$ [$L_\odot$]")
            if dataInstances[i]==4:
                plotLabels.append("$P$ [$N m^{-2}$]")
            if dataInstances[i]==5:
                plotLabels.append(r"$\rho$ [$kg m^{-3}$]")
            if dataInstances[i]==6:
                plotLabels.append("$T$ [$K$]")
            if dataInstances[i]==7:
                plotLabels.append("$U$ [$J kg^{-1}$]")
            if dataInstances[i]==8:
                plotLabels.append("$S$ [$J K^{-1} kg^{-1}$]")
            if dataInstances[i]==9:
                plotLabels.append("$C_P$ [$J K^{-1} kg^{-1}$]")
            if dataInstances[i]==10:
                plotLabels.append(r"$\Gamma_1$ [1]")
            if dataInstances[i]==11:
                plotLabels.append(r"$\nabla_{ad}$ [1]")
            if dataInstances[i]==12:
                plotLabels.append(r"$\mu$ [$kg$]")
            if dataInstances[i]==13:
                plotLabels.append("$n_e$ [$m^{-3}$]")
            if dataInstances[i]==14:
                plotLabels.append("$P_e$ [$N m^{-2}$]")
            if dataInstances[i]==15:
                plotLabels.append("$P_r$ [$N m^{-2}$]")
            if dataInstances[i]==16:
                plotLabels.append(r"$\nabla_{rad}$ [1]")
            if dataInstances[i]==17:
                plotLabels.append(r"$\nabla$ [1]")
            if dataInstances[i]==18:
                plotLabels.append("$v_c$ [$m s^{-1}$]")
            if dataInstances[i]==19:
                plotLabels.append(r"$\kappa$ [$m^2 s^{-1}$]")
            if dataInstances[i]==20:
                plotLabels.append(r"$\epsilon_{nuc}$ [$W kg^{-1}$]")
            if dataInstances[i]==21:
                plotLabels.append(r"$\epsilon_{PP}$ [$W kg^{-1}$]")
            if dataInstances[i]==22:
                plotLabels.append(r"$\epsilon_{CNO}$ [$W kg^{-1}$]")
            if dataInstances[i]==23:
                plotLabels.append(r"$\epsilon_{3\alpha}$ [$W kg^{-1}$]")
            if dataInstances[i]==24:
                plotLabels.append(r"$\epsilon_{v,nuc}$ [$W kg^{-1}$]")
            if dataInstances[i]==25:
                plotLabels.append(r"$\epsilon_{v}$ [$W kg^{-1}$]")
            if dataInstances[i]==26:
                plotLabels.append(r"$\epsilon_{grav}$ [$W kg^{-1}$]")
            if dataInstances[i]==27:
                plotLabels.append("$X$ [1]")
            if dataInstances[i]==28:
                plotLabels.append("$X_{H_n}$ [1]")
            if dataInstances[i]==29:
                plotLabels.append("$X^{+}$ [1]")
            if dataInstances[i]==30:
                plotLabels.append("$Y$ [1]")
            if dataInstances[i]==31:
                plotLabels.append("$Y^+$ [1]")
            if dataInstances[i]==32:
                plotLabels.append("$Y^{++}$ [1]")
            if dataInstances[i]==33:
                plotLabels.append("$X_C$ [1]")
            if dataInstances[i]==34:
                plotLabels.append("$X_N$ [1]")
            if dataInstances[i]==35:
                plotLabels.append("$X_O$ [1]")
            if dataInstances[i]==36:
                plotLabels.append(r"$\psi$ [1]")
        ax.set_xlabel(plotLabels[0])
        ax.set_ylabel(plotLabels[1])

        if flipXaxis==True:
            ax.invert_xaxis()
        if xlog==True:
            ax.set_xscale("log")
        if ylog==True:
            ax.set_yscale("log")
        if scatter==True:
            ax.scatter(x,y,label=legendText)
        else:
            ax.plot(x,y,label=legendText)
# ------------ Add graphs here ------------ #
## Test plot, make no conclusions from this
# fig, ax = plt.subplots(1,1,figsize=(5, 5),sharex=True)
# addPlot("M=5, Z=0.001",True,1,28,ax=ax,scatter=False)
# plt.savefig('Test, M=5.png',bbox_inches='tight',transparent=True)
# plt.show()

## M=constant=5, grid of metallicities
Z = [0.0001,0.0003,0.001,0.004,0.01,0.02,0.03]
fig, ax = plt.subplots(2,1,figsize=(8, 6),sharex=True)
plt.subplots_adjust(wspace=0,hspace=0)
for i in range(len(Z)):
    addPlot("M=5, Z="+str(Z[i]),
            detailed=False,
            xvalues=30,
            yvalues=7,
            ax=ax[0],
            singelTimeInstance=True,timeIndex=1,
            xlog=True,
            scatter=True,
            customX=Z[i])
    addPlot("M=5, Z="+str(Z[i]),
            detailed=False,
            xvalues=30,
            yvalues=8,
            ax=ax[1],
            singelTimeInstance=True,timeIndex=1,
            xlog=True,
            scatter=True,
            customX=Z[i])
ax[0].set_xlabel('')
plt.savefig('Metallicity vs T_c, rho_c, grid, M=5.png',bbox_inches='tight',transparent=True)
fig, ax = plt.subplots(2,1,figsize=(8, 6),sharex=True)
plt.subplots_adjust(wspace=0,hspace=0)
for i in range(len(Z)):
    addPlot("M=5, Z="+str(Z[i]),
            detailed=False,
            xvalues=30,
            yvalues=4,
            ax=ax[0],
            singelTimeInstance=True,timeIndex=1,
            xlog=True,
            scatter=True,
            customX=Z[i])
    addPlot("M=5, Z="+str(Z[i]),
            detailed=False,
            xvalues=30,
            yvalues=6,
            ax=ax[1],
            singelTimeInstance=True,timeIndex=1,
            xlog=True,
            scatter=True,
            customX=Z[i])
ax[0].set_xlabel('')
plt.legend()
plt.savefig('Metallicity vs L, T_s, grid, M=5.png',bbox_inches='tight',transparent=True)

## Example: My folder is called "M=5, Z=0,03". I want to create HR-diagram
# fig, ax = plt.subplots(1,1,figsize=(8, 6),sharex=True)
# plt.subplots_adjust(wspace=0,hspace=0)
# addPlot("M=5, Z=0.02",False,6,4,ax=ax,scatter=False,flipXaxis=True,legendText="AAA")
# plt.legend()
# plt.show()

# ------------------------ #