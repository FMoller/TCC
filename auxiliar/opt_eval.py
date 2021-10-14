import numpy as np
import pandas as pd
import leitor
from math import inf

#pasta="results/resultadosRLNA60/"
pasta="results/random-population/sam/"

def get_opt(f_name, rd = False, bs = False):
    f = open(f_name, 'r')
    a = f.read()
    st_nm = 0
    l_st_nm = 0
    ed_nm = 0
    o_eval = {}
    while True:
        st_nm = a.find('NUM TRANSISTORS:',st_nm)+17
        ed_nm = a.find('INDIVIDUAL:',st_nm)-1
        if l_st_nm > st_nm:
            break
        l_st_nm = st_nm
        tr = int(a[st_nm:ed_nm])
        gen_st = a.find('GENERATION:',st_nm)+12
        if bs:
            gen_ed = a.find('\n',st_nm)
        else:
            gen_ed = a.find('\t',st_nm)-1
        gn = int(a[gen_st:gen_ed])
        if rd:
            if gn%50000 == 0:
                o_eval[gn] = tr
        else:
            o_eval[gn] = tr
    return o_eval

def mean_opt(pasta,problm, rd = False, bs = False):
    m_dict = {}
    means = []
    for i in range(1,26):
        if bs:
            d = get_opt(pasta+problm+'_seed'+str(i)+'.txt',rd, bs)
        else:
            d = get_opt(pasta+problm+'_'+str(i),rd)
        for j in d.keys():
            if j in m_dict.keys():
                m_dict[j].append(d[j])
            else:
                m_dict[j] = [d[j]]
    for i in m_dict.keys():
        m_tr = np.mean(m_dict[i])
        means.append([i,m_tr])
    np.savetxt(pasta+"opt_conv/"+problm+".csv",means,fmt='%1.0d',delimiter=",")
    return np.array(means),m_dict




#b = get_opt(pasta+'C17_seed1.txt',False,True)
b = mean_opt(pasta,"C17", True, True)[0]
