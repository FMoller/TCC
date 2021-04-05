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

def md_placings(f_name, budget):
##    file = pd.read_csv(f_name, sep='\t')
##    if '_design' in f_name:
##        stt_gen = budget
##        stp_gen = np.min(file['Eval.'])
##    else:
##        #stt_gen = np.max(file['Eval.'])
##        stt_gen = np.max(find_earlydes(f_name.split(sep='_')[0]+'_design.csv'))
##        stp_gen = 0
##    (lim_inf,lim_sup) = intervals(n_intervals, stt_gen-stp_gen)
##    # f.loc[f['Seed']==1]['Eval.']
    pass

def find_endings(f_name):
    """
    Find the generation where the best seed in the des phase found a factible
    solution
    """
    f = pd.read_csv(f_name, sep='\t')
    best = []
    for i in range(1,26):
        best.append(np.min(f.loc[f['Seed']==i]['Eval.']))
    return best
    

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def case_count(f_name, budget, n_intervals=25, norm=False, sing=True):
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
        #stt_gen = np.max(file['Eval.'])
        stt_gen = np.max(find_endings(f_name.split(sep='_')[0]+'_design.csv'))
        stp_gen = 0
    (lim_inf,lim_sup) = intervals(n_intervals, stt_gen-stp_gen)
    
    l_mdplc = 0
    b = find_endings(f_name) 
    while np.nan in b:
        b.remove(np.nan)
    md_plc = stt_gen - np.mean(b)
    
    for j in range(n_intervals):
        if md_plc < lim_sup[j]:
            l_mdplc = j
            break
    cases = np.zeros((4,n_intervals))
    for i in range(len(file)):
        gen = stt_gen - file.iloc[i]['Eval.']
        m_kind = file.iloc[i]['Mutation']
        for j in range(n_intervals): #Not the best way, but it's ok for now
            if gen < lim_sup[j]:
                cases[kind_dict[m_kind], j] += 1
                if sing:
                    break
    if norm:
        for i in range(n_intervals):
            total = cases[0][i] + cases[1][i] + cases[2][i] + cases[3][i]
            if total != 0:
                for j in range(4):
                    cases[j][i] = cases[j][i]/total
            
                
    return md_intervals((lim_inf,lim_sup)),cases,l_mdplc



def f_count(f_list, exit_file, n_intervals=25, norm=False, sp_type = 1 , w_og = False, m_ed = False):
    """
    Receive a list of files with the budget and print 4 graphics

    sp_type:
    0 -> Just bar graph, non cummulative
    1 -> Bar graph, nom cummulative and cummulative plot
    2 -> Just cummulative plot
    """
    results = []
    c_results = []
    for (f_name,budget) in f_list:
        case = case_count(f_name, budget, n_intervals, norm, True)
        c_case = case_count(f_name, budget, n_intervals, norm, False)
        results.append(case)
        c_results.append(c_case)
    
    #return results
    if w_og:
        width = 0.20
        dist = [-3*width/2, -width/2, width/2, 3*width/2]
    else:
        width = 0.30
        dist = [-width, 0, width, 0]
    fig, ax = plt.subplots(2,2)
    for i in range(4):
        j = int(i>=2)
        k = int(i%2!=0)
        print((j,k))
        x = np.arange(len(results[i][0]))
        if sp_type == 0 or sp_type == 1:
            ax[j][k].bar(x + dist[0],
                        results[i][1][0], width, label = 'I1G', color = 'tab:blue')   
            ax[j][k].bar(x + dist[1],
                        results[i][1][1], width, label = 'I2G', color = 'tab:orange')       
            ax[j][k].bar(x + dist[2],
                        results[i][1][2], width, label = 'FG', color = 'tab:green')  
            ax[j][k].set_title(f_list[i][0][:-4])
            if w_og:
                ax[j][k].bar(x + dist[3],
                        results[i][1][3], width, label = 'FG', color = 'tab:red')
        if sp_type == 1 or sp_type == 2:
            ax[j][k].set_title(f_list[i][0][:-4])
            ax[j][k].plot(c_results[i][1][0], color = 'tab:blue')
            ax[j][k].plot(c_results[i][1][1], color = 'tab:orange')
            ax[j][k].plot(c_results[i][1][2], color = 'tab:green')
            if w_og:
                ax[j][k].plot(c_results[i][1][3], color = 'tab:red')
        if m_ed:
            ax[j][k].scatter(results[i][2],200 )
    fig.subplots_adjust(left=0.07, bottom=0.07, right=0.950,
                         top=0.945, wspace=0.07, hspace=0.1)
    fig.text(0.5, 0.02, '4-percentile', ha='center')
    fig.text(0.02, 0.5, 'Occurrence of improvements', va='center', rotation='vertical')
    fig1 = plt.gcf()
    fig1.set_size_inches((13, 11), forward=False)
    fig.savefig(exit_file,dpi=100, format="png")

    

NOMES2 = ['C17','cm42a','cm82a','cm138a','decod','f51m','majority','z4ml']
NM2LED=[3000000,3200000,2000000,4800000,3000000,4800000,2000000,4200000]               
f_list1 = [
    ('C17_design.csv',3000000),
    ('cm42a_design.csv',3200000),
    ('cm82a_design.csv',2000000),
    ('cm138a_design.csv',4800000),
    ]
f_list2 = [
    ('C17_opt.csv',3000000),
    ('cm42a_opt.csv',3200000),
    ('cm82a_opt.csv',2000000),
    ('cm138a_opt.csv',4800000),
    ]
f_list3 = [
    ('decod_design.csv',3000000),
    ('f51m_design.csv',4800000),
    ('majority_design.csv',2000000),
    ('z4ml_design.csv',4200000),
    ]
f_list4 = [
    ('decod_opt.csv',3000000),
    ('f51m_opt.csv',4800000),
    ('majority_opt.csv',2000000),
    ('z4ml_opt.csv',4200000),
    ] 
teste2 = f_count(f_list4, 'peq8opt.png', sp_type = 1, w_og = True, m_ed = True) 
teste = case_count('z4ml_opt.csv', NM2LED[3], n_intervals=25, norm=False)
  
##fig,ax = plt.subplots()
##ax.plot(teste[0],teste[1][0])
##ax.plot(teste[0],teste[1][1])
##ax.plot(teste[0],teste[1][2])
##ax.plot(teste[0],teste[1][3])
##plt.show()
##


    
    
