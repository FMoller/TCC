"""
Base = analisedetipos.py
"""

__version__ = "2.0"
__author__ = "Frederico Moeller"
__copyright__ = "Copyright 2021, Frederico Moeller"
__license__ = "MIT"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


""" From analisedetipos.py """
NOMES2 = ['C17','cm42a','cm82a','cm138a','decod','f51m','majority','z4ml']
NM2LED=[3000000,3200000,2000000,4800000,3000000,4800000,2000000,4200000]
NM2MIN=[2966949,3072779,1888303,4101486,1699070,0,1975944,3772127]
NM290 = [NM2MIN[i]+int((NM2LED[i]-NM2MIN[i])*0.1) for i in range(len(NM2MIN))]
TPS = ['I1G','I2G','FG','OG']
LBS = ['IG','FG','OG']
TPS2 = ['OG','0','1','2','3','4+']
REFACT = ['IG1 Act.','IG2 Act.','FG Act.','OG Act.']

def intervals(parts, duration):
    """
    Divides the duration in n intervals and return two arrays one with the
    start index of each interval and other with the end index
    """
    
    part_duration = duration / parts
    return (np.array([int(np.round((i) * part_duration)) for i in range(parts)]),
            np.array([int(np.round((i+1) * part_duration)) for i in range(parts)]))

def md_intervals(intervals):
    """
    It receives the arrays with the indices of entry and exit of the intervals
    and returns an array with the indices to the midpoint of the intervals.
    """
    
    resultado=[]
    for i in range(len(intervals[0])):
        resultado.append((intervals[0][i]+intervals[1][i])/2)
    return resultado

def centroide(intervalos,maximo,eixoX,eixoY,minimo=0,rsct=True):
    eixoXm = np.zeros(intervalos)
    eixoYm = np.zeros(intervalos)
    valores = np.zeros(intervalos)
    vx=[]
    vy=[]
    marcadores =intervals(intervalos,maximo-minimo)
    for i in range(len(eixoX)):
        V1x = eixoX.iloc[i]>=marcadores[0]
        V2x = eixoX.iloc[i]<=marcadores[1]
        Vx = V1x==V2x
        eixoXm[Vx]+=eixoX.iloc[i]
        if type(eixoY)==type([]):
            eixoYm[Vx]+=eixoY[i]
        else:
            eixoYm[Vx]+=eixoY.iloc[i]
        valores[Vx]+=1
    for i in range(intervalos):
        if valores[i]>0:
            vx.append(eixoXm[i]/valores[i])
            vy.append(eixoYm[i]/valores[i])
        else:
            vx.append((marcadores[0][i]+marcadores[1][i])/2)
            vy.append(0)
    if rsct:    
        return (np.divide(eixoXm,valores),np.divide(eixoYm,valores),valores)
    else:
        return(vx,vy,valores)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



