import numpy as np
import pandas as pd
import leitor
pastas = pd.read_csv("pastas.csv")
prblm = pd.read_csv("problemas.csv")
print("START")
dt_struct={"alg":[]}


for i in range(len(pastas["Pasta"])):
    dt_struct["alg"].append(pastas["algoritmo"].iloc[i])
    for problema in prblm["Problema"]:
        #print(pastas["Pasta"].iloc[i])
        #print(problema)
        try:
            if i!=0 and problema=="cc":
                a = leitor.captura(pastas["Pasta"].iloc[i],"ccp")
            else:    
                a = leitor.captura(pastas["Pasta"].iloc[i],problema)
            while None in a:
                a.remove(None)
            try:
                if len(a)>0:
                    dt_struct[problema+" min"].append(np.min(a))
                    dt_struct[problema+" mean"].append(np.mean(a))
                    dt_struct[problema+" median"].append(np.median(a))
                    dt_struct[problema+" max"].append(np.max(a))
                    dt_struct[problema+" std"].append(np.std(a))
                else:
                    dt_struct[problema+" min"].append(-1)
                    dt_struct[problema+" mean"].append(-1)
                    dt_struct[problema+" median"].append(-1)
                    dt_struct[problema+" max"].append(-1)
                    dt_struct[problema+" std"].append(-1)
                dt_struct[problema+" sr"].append(len(a)/25)
            except:
                dt_struct[problema+" min"]=[]
                dt_struct[problema+" mean"]=[]
                dt_struct[problema+" median"]=[]
                dt_struct[problema+" max"]=[]
                dt_struct[problema+" std"]=[]
                dt_struct[problema+" sr"]=[]
                if len(a)>0:
                    dt_struct[problema+" min"].append(np.min(a))
                    dt_struct[problema+" mean"].append(np.mean(a))
                    dt_struct[problema+" median"].append(np.median(a))
                    dt_struct[problema+" max"].append(np.max(a))
                    dt_struct[problema+" std"].append(np.std(a))
                else:
                    dt_struct[problema+" min"].append(-1)
                    dt_struct[problema+" mean"].append(-1)
                    dt_struct[problema+" median"].append(-1)
                    dt_struct[problema+" max"].append(-1)
                    dt_struct[problema+" std"].append(-1)
                dt_struct[problema+" sr"].append(len(a)/25)
                
        except:
            try:
                dt_struct[problema+" min"].append(-1)
                dt_struct[problema+" mean"].append(-1)
                dt_struct[problema+" median"].append(-1)
                dt_struct[problema+" max"].append(-1)
                dt_struct[problema+" std"].append(-1)
                dt_struct[problema+" sr"].append(-1)
            except:
                dt_struct[problema+" min"]=[]
                dt_struct[problema+" mean"]=[]
                dt_struct[problema+" median"]=[]
                dt_struct[problema+" max"]=[]
                dt_struct[problema+" std"]=[]
                dt_struct[problema+" sr"]=[]
                dt_struct[problema+" min"].append(-1)
                dt_struct[problema+" mean"].append(-1)
                dt_struct[problema+" median"].append(-1)
                dt_struct[problema+" max"].append(-1)
                dt_struct[problema+" std"].append(-1)
                dt_struct[problema+" sr"].append(-1)
df = pd.DataFrame(data=dt_struct)
df.to_csv("testedt.csv")
##    while None in a:
##        a.remove(None)
##    print(a)
