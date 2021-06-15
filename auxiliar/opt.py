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
    rate = np.zeros((4,25))
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
    rate = np.zeros((4,25))
    for i in range(1,26):
        print(i)
        rate+=by_quart(problem,i)
    return rate

        
        
    

#a = take_media("C17")
a = quart_all("C17")       

    
