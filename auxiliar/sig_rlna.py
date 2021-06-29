import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import leitor

ref="results/random-population/sam/"
alg="results/resultadosRLNA60/"

algs = ["C17","cm42a","cm82a","cm138a","decod","f51m","majority","z4ml"]
algs2 = ["9symml","alu2","alu4","cm85a","cm151a","cm162a","cu","x2"]
algs3 = ["cc","cmb","cordic","frg1","pm1","sct","t481","tcon","vda"]

def clear_none(lst):
    while None in lst:
        lst.remove(None)
    return lst

for i in algs:
    try:
        tr = leitor.captura(ref,i)
    except:
        print("No ref data for",i)
    try:
        if i == "cc":
            ta = leitor.captura(alg,"ccp")
        else:
            ta = leitor.captura(alg,i)
    except:
        print("No alg data for",i)
    tr = clear_none(tr)
    ta = clear_none(ta)
    try:
        tC17 = stats.kruskal(tr,ta)
        #tC17 = stats.ttest_ind(tr,ta,equal_var = False)
        print(i,tC17)
    except:
        print("Failed:",i)
    
##alg_bar = []
##alg_bar_l = []
##alg_bar_h = []
##ref_bar = []
##ref_bar_l = []
##ref_bar_h = []
##for i in algs:
##    print(i)
##    try:
##        tr = leitor.captura(ref,i)
##    except:
##        print("No ref data for",i)
##    try:
##        if i == "cc":
##            ta = leitor.captura(alg,"ccp")
##        else:
##            ta = leitor.captura(alg,i)
##    except:
##        print("No alg data for",i)
##        continue
##    tr = clear_none(tr)
##    ta = clear_none(ta)
##    if len(tr)==0 or len(ta)==0:
##        print("Got it")
##        continue
##    alg_bar.append(np.mean(ta))
##    ref_bar.append(np.mean(tr))
##    alg_bar_l.append(np.min(ta))
##    ref_bar_l.append(np.min(tr))
##    alg_bar_h.append(np.max(ta))
##    ref_bar_h.append(np.max(tr))
##
##fig, ax = plt.subplots()
##ax.plot(alg_bar,color="blue")
##ax.plot(alg_bar_l,color="blue",linestyle="--")
##ax.plot(alg_bar_h,color="blue",linestyle="--")
##ax.plot(ref_bar,color="orange")
##ax.plot(ref_bar_l,color="orange",linestyle="--")
##ax.plot(ref_bar_h,color="orange",linestyle="--")
##plt.show()
