import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dir_ref = "results/random-population/sam/"
arquivo = "9symml_seed1.txt"
myn_ref = "results/resultadosRLNA60/"



def find_sat(text):
    lp = 0
    rs = 0
    while(rs!=-1):
        rs = text.find('SAT COUNT:',lp)
        if rs>lp:
            lp = rs+1
##        print(rs)
    return lp

def collect_des(file):
##    print(file)
    f = open(file, "r")
    a = f.read()
    gen_st = a.find('GENERATION:',find_sat(a))+11
    gen_sp = a.find('\n',gen_st)
    f.close()
    return int(a[gen_st:gen_sp])

def collect_des2(file):
##    print(file)
    f = open(file, "r")
    a = f.read()
    gen_st = a.find('GENERATION:',find_sat(a))+11
    gen_sp = a.find('\t',gen_st)
    f.close()
    return int(a[gen_st:gen_sp])

def take_des(directory, problem):
    des_gen = []
    for i in range(1,26):
        try:
            file = directory+problem+'_'+str(i)
            des_gen.append(collect_des2(file))
        except:
            file = directory+problem+'_seed'+str(i)+'.txt'
            des_gen.append(collect_des(file))
    return des_gen

prb = "decod"
a = take_des(dir_ref,prb)
b = take_des(myn_ref,prb)

fig1, ax1 = plt.subplots()
ax1.set_title("Gerações para chegar em uma solução factível "+prb)
ax1.violinplot(a,showmeans=True,showmedians=True)
#ax1.plot([0.7,1.3],[201600,201600])
ax1.scatter([1],[np.mean(a)])
ax1.grid(True)

ax1.violinplot(b,showmeans=True,showmedians=True)
#ax1.plot([0.7,1.3],[201600,201600])
ax1.scatter([1],[np.mean(b)])
ax1.grid(True)
fig1.subplots_adjust(left=0.057, bottom=0.067, right=0.974, top=0.95, wspace=None, hspace=None)

plt.show()

    
    
    
