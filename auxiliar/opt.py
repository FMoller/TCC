import pandas as pd
import numpy as np


def take_trans(problem,seed):
    arq = pd.read_csv(problem+"_"+str(seed))
    return arq.iloc[-1]['type']

def take_media(problem):
    val = []
    for i in range(1,26):
        val.append(take_trans(problem,i))
    return val

def by_quart(problem,seed):
    rate = np.zeros((5,25))
    arq = pd.read_csv(problem+"_"+str(seed))
    max_gen = arq.iloc[-2]['gen']
    for i in range(len(arq)-1):
        ind = arq.iloc[i]['gen']/max_gen
        ind = int(np.floor(ind/0.04))
        #print(ind)
        if ind >=25:
            ind = 24
        rate[arq.iloc[i]['type']][ind]+=1
    return rate

def quart_all(problem):
    rate = np.zeros((5,25))
    for i in range(1,26):
        print(i)
        rate+=by_quart(problem,i)
        rate[4,0]=i
        np.savetxt(problem+".csv",rate,fmt='%1.0d',delimiter=",")
    return rate
   
def take_mut(problem,seed):
    arq = pd.read_csv(problem+"_"+str(seed))
    return len(arq['gen']-1)/arq.iloc[-2]['gen']

def mean_mut(problem):
    mean = 0
    for i in range(1,26):
        mean += take_mut(problem,i)
    return mean/25

##
###a = take_media("C17")
prbs2 = ["cm42a","cm82a","cm138a","decod","majority","f51m","z4ml"]
##prbs = ["z4ml"]
##for i in prbs:
##    try:
##        a = quart_all(i)
##    except:
##        print("faild",i)

for i in prbs2:
    print(i+" : "+str(mean_mut(i)))
    
