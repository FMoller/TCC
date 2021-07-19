import numpy as np
import pandas as pd
import design_aval as da
from math import inf
pastas = pd.read_csv("pastas_des.csv")
prblm = pd.read_csv("problemas_des.csv")
print("START")
dt_struct={"alg":[]}
dt_dat=dict()
min_values=dict()
mean_values=dict()
min_dat=dict()
min_datT=dict()
diff_dat=dict()
diff_datT=dict()
mean_dat=dict()
sr_dat=dict()
sr_datT=dict()
#a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
#a = leitor.captura(pastas["Pasta"].iloc[i],problema)
for problema in prblm["Problema"]:
    if problema == 'cc':
        problema = 'ccp'
    for i in range(len(pastas["Pasta"])):
        if problema not in dt_dat.keys():
            dt_dat[problema]=dict()
            mean_values[problema]=[]
        if problema not in min_values.keys():
            min_values[problema]=inf
        try:
            
            a = da.take_des(pastas["Pasta"].iloc[i],problema)
            acp = a.copy()
            while None in acp:
                acp.remove(None)
        except:
            a=[None]*25
            acp = []
        try:
            if len(acp)>0:
                amean = np.mean(acp)
            else:
                amean = inf
            amin = np.min(acp)
        except:
            amin = inf
            amean = inf
        if amin < min_values[problema]:
            min_values[problema]=amin
        dt_dat[problema][pastas["algoritmo"].iloc[i]]=a
        mean_values[problema].append(amean)

#calculo do Best
for problema in prblm["Problema"]:
    if problema == 'cc':
        problema = 'ccp'
    for i in range(len(pastas["Pasta"])):
        if problema not in min_dat.keys():
            min_dat[problema]=dict()
        if pastas["algoritmo"].iloc[i] not in min_datT.keys():
            min_datT[pastas["algoritmo"].iloc[i]]=0
            mean_dat[pastas["algoritmo"].iloc[i]]=0
        if pastas["algoritmo"].iloc[i] not in diff_dat.keys():   
            diff_dat[pastas["algoritmo"].iloc[i]]=[]
            sr_dat[pastas["algoritmo"].iloc[i]]=[]
        diff = []
        try:
            a = da.take_des(pastas["Pasta"].iloc[i],problema)
            acp = a.copy()
            while None in acp:
                acp.remove(None)
        except:
            print(pastas["algoritmo"].iloc[i]+" "+problema+" não executado")
            a=[None]*25
            acp = []
        try:
            if len(acp)>0:
                amean = np.mean(acp)
            else:
                amean = inf
        except:
            amean = inf
        for j in a:
            if j!=None:
                if min_values[problema]!=inf:
                    diff_dat[pastas["algoritmo"].iloc[i]].append((j/min_values[problema])-1)
                    
        min_dat[problema][pastas["algoritmo"].iloc[i]]=a.count(min_values[problema])
        min_datT[pastas["algoritmo"].iloc[i]]+=a.count(min_values[problema])
        mean_dat[pastas["algoritmo"].iloc[i]]+=np.sum(np.array(mean_values[problema])<amean)
        sr_dat[pastas["algoritmo"].iloc[i]].append(len(acp))
for i in diff_dat.keys():
    try:
        diff_datT[i]=np.mean(diff_dat[i])
    except:
        print(i)
        
    sr_datT[i] = np.sum(sr_dat[i])/(len(sr_dat[i])*25)
            
        
dt_struct["alg"] = list(min_datT.keys())
dt_struct["Best"] = [min_datT[x] for x in min_datT.keys()]
dt_struct["Mdiff"] = [diff_datT[x] for x in min_datT.keys()]
dt_struct["Nscore"] = [mean_dat[x] for x in min_datT.keys()]
dt_struct["SR"] = [sr_datT[x] for x in min_datT.keys()]
df = pd.DataFrame(data=dt_struct)
df.to_csv("nmtrics_design80.csv")    
