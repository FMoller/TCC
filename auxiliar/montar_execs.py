import numpy as np
import pandas as pd
import leitor
pastas = pd.read_csv("pastas.csv")
prblm = pd.read_csv("problemas.csv")
print("START")
dt_struct={"alg":[]}

for problema in prblm["Problema"]:
    for i in range(len(pastas["Pasta"])):
        dt_struct["alg"].append(problema+" "+pastas["algoritmo"].iloc[i])
        try:
            if i!=0 and problema=="cc":
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
            else:    
                a = leitor.captura(pastas["Pasta"].iloc[i],problema)
            for j in range(25):
                try:
                    try:
                        dt_struct[j+1].append(str(a[j]))
                    except:
                        dt_struct[j+1].append('None')
                except:
                    dt_struct[j+1]=[]
                    try:
                        dt_struct[j+1].append(str(a[j]))
                    except:
                        dt_struct[j+1].append('None')
        except:
            for j in range(25):
                try:
                    dt_struct[j+1].append('None')
                except:
                    dt_struct[j+1]=[]
                    dt_struct[j+1].append('None')
                    

df = pd.DataFrame(data=dt_struct)
df.to_csv("tabela2.csv")
            
            
            
        
    
