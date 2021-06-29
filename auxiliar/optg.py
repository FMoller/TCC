import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

A = [['C17','cm42a'],
     ['cm82a','cm138a'],
     ['decod','f51m'],
     ['majority','z4ml']]

fig, ax = plt.subplots(4,2)
for i in range(4):
    for j in range(2):
        prb = pd.read_csv(A[i][j]+'.csv', header=None)
        ax[i,j].plot(np.array(prb.iloc[0]))
        ax[i,j].plot(np.array(prb.iloc[1]))
        ax[i,j].plot(np.array(prb.iloc[2]))
plt.show()
