#! /usr/bin/python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as Axes

import numpy as np
import seaborn as sns

# https://matplotlib.org/stable/api/markers_api.html
df=pd.read_csv("data_fig2.ssv", header=0, sep='\s+')
print (df)
x=df["nDFT"]
y=df["nvol"]
yerr=df["nsd"]
#z=df["PHASE"]
Atm=df["Ele"]
xpar=[0,70]
ypar=[0,70]
linepar_df=pd.DataFrame({"xpar":xpar, "ypar":ypar})
g = sns.relplot(data=df, x='nDFT', y='nvol', hue="Ele", zorder=2, height=6.75, aspect=1)
l = sns.lineplot(x = "xpar", y = "ypar", data=linepar_df, c='red', zorder=0)
plt.legend(ncol=1, loc="lower right")

plt.xlabel("DFT ($\AA^{3}$/atom)", fontsize=24, fontweight='bold')
plt.ylabel("DNP ($\AA^{3}$/atom)", fontsize=24, fontweight='bold')
plt.title( 'A)', x=0.05, y=0.9, fontsize=24, fontweight='bold') 
plt.errorbar(x, y, yerr=yerr, fmt=' ', c='black', zorder=1, lw=1, capsize=3, capthick=1)

# Hide the right and top spines
ax = sns.despine(bottom = False, left = False, top = False, right = False, )
sns.axes_style("ticks")
g._legend.remove()
plt.xlim(0,70)
plt.ylim(0,70)
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.gcf().subplots_adjust(bottom=0.12, left=0.12, wspace=0, hspace=0)
plt.show()
g.savefig('fig2A.png')
