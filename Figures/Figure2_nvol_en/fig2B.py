#! /usr/bin/python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as Axes
import numpy as np
import seaborn as sns

df=pd.read_csv("data_fig2.ssv", header=0, sep='\s+')
print (df)
x=df["eDFT"]
y=df["Ecoh"]
yerr=df["esd"]
#z=df["PHASE"]
Atm=df["Ele"]
xpar=[-14,1]
ypar=[-14,1]
linepar_df=pd.DataFrame({"xpar":xpar, "ypar":ypar})
g = sns.relplot(data=df, x='eDFT', y='Ecoh', hue="Ele", zorder=2, height=6.75, aspect=1)
l = sns.lineplot(x = "xpar", y = "ypar", data=linepar_df, c='red', zorder=0)

plt.legend([],[], frameon=False)
plt.xlabel("DFT (eV/atom)", fontsize=24, fontweight='bold')
plt.ylabel("DNP (eV/atom)", fontsize=24, fontweight='bold')
plt.title( 'B)', x=0.05, y=0.9, fontsize=24, fontweight='bold') 
plt.errorbar(x, y, yerr=yerr, fmt=' ', c='black', zorder=1, lw=1, capsize=3, capthick=1)
ax = sns.despine(bottom = False, left = False, top = False, right = False, )
sns.axes_style("ticks")
g._legend.remove()
plt.xlim(-14,1)
plt.ylim(-14,1)
plt.rcParams['ytick.labelsize'] = 2
plt.rcParams['ytick.labelsize'] = 2
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.gcf().subplots_adjust(bottom=0.12, left=0.15, wspace=0, hspace=0)

plt.show()
g.savefig('fig2B.png')
