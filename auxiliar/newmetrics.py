import numpy as np
import pandas as pd
import leitor
from math import inf
pastas = pd.read_csv("pastas.csv")
prblm = pd.read_csv("problemas.csv")
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
#a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
#a = leitor.captura(pastas["Pasta"].iloc[i],problema)
for problema in prblm["Problema"]:
    for i in range(len(pastas["Pasta"])):
        if problema not in dt_dat.keys():
            dt_dat[problema]=dict()
            mean_values[problema]=[]
        if problema not in min_values.keys():
            min_values[problema]=inf
        try:
            if i!=0 and problema=="cc":
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
            else:    
                a = leitor.captura(pastas["Pasta"].iloc[i],problema)
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
    for i in range(len(pastas["Pasta"])):
        if problema not in min_dat.keys():
            min_dat[problema]=dict()
        if pastas["algoritmo"].iloc[i] not in min_datT.keys():
            min_datT[pastas["algoritmo"].iloc[i]]=0
            mean_dat[pastas["algoritmo"].iloc[i]]=0
        if pastas["algoritmo"].iloc[i] not in diff_dat.keys():   
            diff_dat[pastas["algoritmo"].iloc[i]]=[]
        diff = []
        try:
            if i!=0 and problema=="cc":
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
            else:    
                a = leitor.captura(pastas["Pasta"].iloc[i],problema)
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
        
for i in diff_dat.keys():
    try:
        diff_datT[i]=np.mean(diff_dat[i])
    except:
        print(i)
            
            
        
    
