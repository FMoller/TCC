"""
Make the boxplot from data
"""

__version__ = "1.0"
__author__ = "Frederico Moeller"
__copyright__ = "Copyright 2021, Frederico Moeller"
__license__ = "MIT"

import functools
import numpy as np
import pandas as pd
import leitor
import matplotlib.pyplot as plt
from math import inf

def mse_cols(cola, colb):
    mse = 0
    for i in range(len(cola)):
        for j in range(3):
            mse += (cola[i,j] - colb[i,j])**2
    return mse/(len(cola)*3)

def find_maxd(surface):
    max_dist = 0
    md0 = 0
    md1 = -1
    for i in range(len(surface[0])-1):
        for j in range(i+1,len(surface[0])):
            dist = mse_cols(surface[:,i,:],surface[:,j,:])
            if dist > max_dist:
                #print('(',i,',',j,'):',dist) 
                max_dist = dist
                md0 = i
                md1 = j
    return (max_dist,md0,md1)
            


pastas = pd.read_csv("pastas_alpha.csv")
prblm = pd.read_csv("problemas_ok.csv")

surf = np.zeros((len(pastas['Pasta']), len(prblm['Problema'])))

sizes = dict()

for i in prblm['Problema']:
    sz = 2**int(prblm['in'].loc[prblm['Problema'] == i])
    sz *= int(prblm['out'].loc[prblm['Problema'] == i])
    while sz in sizes.keys():
        print(i,":",sz)
        sz += 1
    sizes[sz] = i

order = list(sizes.keys()).copy()
order.sort()
visited = []
for problema in prblm["Problema"]:
    sz = 2**int(prblm['in'].loc[prblm['Problema'] == problema])
    sz *= int(prblm['out'].loc[prblm['Problema'] == problema])
    while sz in visited:
        sz += 1
    visited.append(sz)
    for i in range(len(pastas["Pasta"])):
        
        if problema=="cc":
            try:
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
            except:
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
        else:
            a = leitor.captura(pastas["Pasta"].iloc[i],problema)
        while None in a:
            a.remove(None)
        if len(a) > 0:
            surf[i,order.index(sz)] = np.mean(a)
        else:
            surf[i,order.index(sz)] = -1

surf3 = np.zeros((len(pastas['Pasta']), len(prblm['Problema']), 3))
for col in range(len(prblm['Problema'])):
    values = list(surf[:,col]).copy()
    #print(values)
    while -1 in values:
        values.remove(-1)
    try:
        min_val = np.min(values)
        max_val = np.max(values)
    except:
        print(col)
    for line in range(len(pastas['Pasta'])):
        if surf[line,col] == -1:
            surf3[line,col,0] = 1
        elif min_val==max_val:
            surf3[line,col,0] = 1
            surf3[line,col,1] = 1
            surf3[line,col,2] = 1
        else:
            norm_val = 1 - ((surf[line,col]-min_val)/(max_val - min_val))
            surf3[line,col,0] = norm_val
            surf3[line,col,1] = norm_val
            surf3[line,col,2] = norm_val

my_ticks = [sizes[i]+'\n '+str(i) for i in order]

mse_col = dict()
#mse = 0
closer = 0
##for i in range(len(prblm['Problema'])):
##    for k in range(len(pastas['Pasta'])):
##        for j in range(3):
##            mse += (surf3[k,6,j] - surf3[k,i,j])**2
##    mse = mse/(3*(len(pastas['Pasta'])))


for i in range(len(prblm['Problema'])):
    dist = mse_cols(surf3[:,3,:], surf3[:,i,:])
    if dist in mse_col.keys():   
        print('doubled:',i,':',my_ticks[i])
    else:
        mse_col[dist] = [i,my_ticks[i]]
    

surf4 = np.zeros((len(pastas['Pasta']), len(prblm['Problema']), 3))
order2 = list(mse_col.keys()).copy()
order2.sort()
other_ticks = []
for i in range(len(order2)):
    idx = mse_col[order2[i]][0]
    surf4[:,i,:] = surf3[:,idx,:]
    other_ticks.append(mse_col[order2[i]][1])
    


fig, ax = plt.subplots()
ax.imshow(surf4)
ax.set_title('médias')
plt.yticks(range(len(pastas['Pasta'])), pastas['algoritmo'])
plt.xticks(range(len(prblm['Problema'])), other_ticks)
plt.show()
            
    
    
    
    




