import Plots
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=2,yvalues=6,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Ts, M=5, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=2,yvalues=6,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Ts, M=50, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=2,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-L, M=5, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=2,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-L, M=50, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=2,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Rhoc, M=5, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=2,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Rhoc, M=50, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=2,yvalues=7,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Tc, M=5, Z=0.02")

ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=2,yvalues=7,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Time-Tc, M=50, Z=0.02")
#----------------------
### Ts-L
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=6,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Ts-L, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=6,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Ts-L, Z=0.02")

### Ts-Rhoc
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=6,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Ts-Rhoc, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=6,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Ts-Rhoc, Z=0.02")

### Ts-Tc
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=6,yvalues=7,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Ts-Tc, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=6,yvalues=7,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Ts-Tc, Z=0.02")

### Tc-L
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=7,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Tc-L, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=7,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Tc-L, Z=0.02")

### Tc-Rhoc
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=7,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Tc-Rhoc, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=7,yvalues=8,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Tc-Rhoc, Z=0.02")

### Rhoc-L
ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=5, Z=0.02",detailed=False,xvalues=8,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=5M_\odot$, Z=0.02",color="blue",markerSize=0)
# Plots.endPlots("Rhoc-L, M=5, Z=0.02")

# ax = Plots.setupPlots(horizontal=1,vertical=1)
Plots.addPlot("M=50, Z=0.02",detailed=False,xvalues=8,yvalues=4,ax=ax,ylog=False,scatter=False,flipXaxis=False,label="$M=50M_\odot$, Z=0.02",color="red",markerSize=0)
Plots.endPlots("Rhoc-L, Z=0.02")