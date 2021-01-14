import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kruskal import *

    
ignorar=["alu4","cu","x2","sct"]
arquivo = pd.read_csv("testedt.csv")
alvos=[("Medias","mean",4,np.mean),
        ("Melhores","min",3,np.min),
        ("Medianas","median",6,np.median)]
alvo = 2
dados = dict()
ind = -alvos[alvo][2]
ignorados = [i+" "+alvos[alvo][1] for i in ignorar]
# Organiza os dados de acordo com a referência
for i in arquivo:
    if np.max(arquivo[i].iloc[1:])!=-1:
        if i[ind:] == alvos[alvo][1]:
            if i not in ignorados:
                try:
                    ref = alvos[alvo][3](globals()[i.split()[0]+"E"])
                except:
                    ref= alvos[alvo][3](NsymmlE)
                for j in range(len(arquivo[i])):
                    try:
                        dados[arquivo['alg'].iloc[j]].append(arquivo[i].iloc[j]/ref)
                    except:
                        dados[arquivo['alg'].iloc[j]]=[]
                        dados[arquivo['alg'].iloc[j]].append(arquivo[i].iloc[j]/ref)
                
                 
grafico = dict()
gamma = 0.5*np.array(list(range(201)))*0.01
tprblm = len(dados['SAM-R'])
for i in dados:
    for j in gamma:
        try:
            #print(str(j)+" e "+str((np.sum(np.array(dados[i])<=j))/tprblm))
            grafico[i].append((np.sum(np.array(dados[i])<=j))/tprblm)
        except:
            grafico[i]=[]
            grafico[i].append((np.sum(np.array(dados[i])<=j))/tprblm)

fig, ax=plt.subplots()

pstyle = {'SAM-R':'-','RLN':'--','RLNA05':'-.','RLNA075':':','RLNA10':'-','RLNA15':'--','RLNA20':'-.','RLNA30':':'}

for i in grafico:
    print("AUC "+i+" : "+str(np.sum(grafico[i])))
    ax.plot(gamma,grafico[i],pstyle[i],label=i)

ax.grid(True)
ax.set_xlabel('Gamma')
ax.set_ylabel('P(Gamma)')
plt.legend()
plt.show()
    
