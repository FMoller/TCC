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


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def case_count(f_name, budget, n_intervals=25, norm=False):
    """
    Receive a csv filen name with the results of a problem, the the budget of 
    the problem and the number of intervals into which the analysis is
    to be divided.

    Returns one array with the midpoints of each interval and an matrix with
    four lines and n_intervals columns with the number of the occurrences that
    every kind of mutation generated a better individual for each interval.

    The lines of the matrix are:
    0 -> I1G mutation on the first input adress
    1 -> I2G mutation on the second input adress
    2 -> FG mutation on the node gate
    3 -> OG mutation on the individual output

    The norm flag unit-normalizes the values in the output
    """
    file = pd.read_csv(f_name, sep='\t')
    kind_dict = {'I1G':0, 'I2G':1, 'FG':2, 'OG':3}
    if '_design' in f_name:
        stt_gen = budget
        stp_gen = np.min(file['Eval.'])
    else:
        stt_gen = np.max(file['Eval.'])
        stp_gen = 0
    (lim_inf,lim_sup) = intervals(n_intervals, stt_gen-stp_gen)
    
    cases = np.zeros((4,n_intervals))
    for i in range(len(file)):
        gen = stt_gen - file.iloc[i]['Eval.']
        m_kind = file.iloc[i]['Mutation']
        for j in range(n_intervals): #Not the best way, but it's ok for now
            if gen < lim_sup[j]:
                cases[kind_dict[m_kind], j] += 1
                break
    if norm:
        for i in range(n_intervals):
            total = cases[0][i] + cases[1][i] + cases[2][i] + cases[3][i]
            if total != 0:
                for j in range(4):
                    cases[j][i] = cases[j][i]/total
            
                
    return md_intervals((lim_inf,lim_sup)),cases


def f_count(f_list, n_intervals=25, norm=False):
    results = []
    for (f_name,budget) in f_list:
        case = case_count(f_name, budget, n_intervals, norm)
        results.append(case)
    
    return results

    

NOMES2 = ['C17','cm42a','cm82a','cm138a','decod','f51m','majority','z4ml']
NM2LED=[3000000,3200000,2000000,4800000,3000000,4800000,2000000,4200000]               
f_list1 = [
    ('C17_design.csv',3000000),
    ('cm42a_design.csv',3200000),
    ('cm82a_design.csv',2000000),
    ('cm138a_design.csv',4800000),
    ]        
teste2 = f_count(f_list1) 
teste = case_count('z4ml_opt.csv', NM2LED[3], n_intervals=25, norm=False)
  
##fig,ax = plt.subplots()
##ax.plot(teste[0],teste[1][0])
##ax.plot(teste[0],teste[1][1])
##ax.plot(teste[0],teste[1][2])
##ax.plot(teste[0],teste[1][3])
##plt.show()
##

width = 0.25
results = teste2
##fig, ax = plt.subplots()
##ax.bar(np.array(results[0][0]),results[0][1][0])
##plt.show()
fig, ax = plt.subplots(2,2)
for i in range(4):
    j = int(i>=2)
    k = int(i%2!=0)
    print((j,k))
    x = np.arange(len(results[i][0]))
    ax[j][k].bar(x - 3*width/2,
                results[i][1][0], width, label = 'I1G')
    ax[j][k].bar(x - width/2,
                results[i][1][1], width, label = 'I2G')
    ax[j][k].bar(x + width/2,
                results[i][1][2], width, label = 'FG')
    ax[j][k].bar(x + 3*width/2,
                results[i][1][3], width, label = 'OG')
    #ax[j][k].set_xticks(results[i][0])
    #fig.tight_layout()
plt.show()
    
    
