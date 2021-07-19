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
    ver = a.find('NUM TRANSISTORS',gen_st)
    f.close()
    if ver != -1:
        return int(a[gen_st:gen_sp])
    else:
        return None

def collect_des_trans(file):
##    print(file)
    f = open(file, "r")
    a = f.read()
    gen_st = a.find('GENERATION:',find_sat(a))+11
    ver = a.find('Num transistors:',gen_st)
    f.close()
    if ver != -1:
        ver = ver+16
        gen_sp = a.find('\n',ver)
        return int(a[ver:gen_sp])
    else:
        return None

def collect_des2(file):
##    print(file)
    f = open(file, "r")
    a = f.read()
    gen_st = a.find('GENERATION:',find_sat(a))+11
    gen_sp = a.find('\t',gen_st)
    f.close()
    ver = a.find('NUM TRANSISTORS',gen_st)
    f.close()
    if ver != -1:
        return int(a[gen_st:gen_sp])
    else:
        return None

def take_des(directory, problem):
    des_gen = []
    for i in range(1,26):
        try:
            try:
                file = directory+problem+'_'+str(i)
                des_gen.append(collect_des2(file))
            except:
                des_gen.append(collect_des(file))
        except:
            if problem == 'ccp':
                problem = 'cc'
            file = directory+problem+'_seed'+str(i)+'.txt'
            des_gen.append(collect_des(file))
    return des_gen

def take_des_trans(directory, problem):
    des_gen = []
    for i in range(1,26):
        try:
            file = directory+problem+'_'+str(i)
            des_gen.append(collect_des_trans(file))
        except:
            if problem == 'ccp':
                problem = 'cc'
            file = directory+problem+'_seed'+str(i)+'.txt'
            des_gen.append(collect_des_trans(file))
    return des_gen

prb = "decod"
a = take_des(dir_ref,prb)
b = take_des(myn_ref,prb)
all_data = [b,a]

exit_file = "fig2ff.eps"
A1 = [['C17','cm42a'],
     ['cm82a','cm138a']]
A2 = [['decod','f51m'],
     ['majority','z4ml']]
A3 = [['9symml','alu4'],
     ['cm85a','cm151a']]
A4 = [['cm162a','cu'],
     ['x2','x2']]
A5 = [['ccp','frg1'],
     ['sct','pm1']]
A6 = [['t481','tcon'],
     ['tcon','tcon']]

##A = A6
##fig, ax = plt.subplots(2,2)
##plt.rcParams["font.size"] = "20"
##for i in range(2):
##    for j in range(2):
##        ax[i,j].set_title(A[i][j])
##        all_data = [take_des(myn_ref,A[i][j]),
##                    take_des(dir_ref,A[i][j])]
##        for k in all_data:
##            while None in k:
##                k.remove(None)
##        #a=cumulative(a)
##        #b=cumulative(b)
##        #c=cumulative(c)
##        ax[i,j].boxplot(all_data, labels=['n-cgprl','cgp'])
##        
##        plt.setp(ax[i,j].get_xticklabels(), fontsize=15)
##        plt.setp(ax[i,j].get_yticklabels(), fontsize=15)
##        print(A[i][j])
##        print(np.min(all_data[0]))
##        print(np.mean(all_data[0]))
##        print(np.std(all_data[0]))
##        print('--------')
##        print(np.min(all_data[1]))
##        print(np.mean(all_data[1]))
##        print(np.std(all_data[1]))
##        print('########')
##        
##
##fig.subplots_adjust(left=0.1, bottom=0.07, right=0.950,
##                         top=0.945, wspace=0.12, hspace=0.18)
##fig.text(0.5, 0.02, 'Algorithm', ha='center')
##fig.text(0.02, 0.5, 'Generations to achieve a feasible individual', va='center', rotation='vertical')
##fig1 = plt.gcf()
##fig1.set_size_inches((13, 11), forward=False)
##fig.savefig(exit_file,dpi=100, format="eps")        
##plt.show()




##ax1.set_title("Gerações para chegar em uma solução factível "+prb)
##ax1.violinplot(all_data,showmeans=True,showmedians=True)
###ax1.plot([0.7,1.3],[201600,201600])
###ax1.scatter([1],[np.mean(a)])
##ax1.grid(True)

#ax1.violinplot(b,showmeans=True,showmedians=True)
#ax1.plot([0.7,1.3],[201600,201600])
#ax1.scatter([1],[np.mean(b)])
#ax1.grid(True)
#fig1.subplots_adjust(left=0.057, bottom=0.067, right=0.974, top=0.95, wspace=None, hspace=None)



    
    
    
