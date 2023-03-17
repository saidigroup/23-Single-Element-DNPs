#! /usr/bin/python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as Axes
import numpy as np
import seaborn as sns

df=pd.read_csv("sfe.ssv", header=0, sep='\s+')
print (df)
x=df["DFT"]
y=df["DNP"]
yerr=df["sd"]
#z=df["PHASE"]
Atm=df["Element"]
xpar=[0,5000]
ypar=[0,5000]
linepar_df=pd.DataFrame({"xpar":xpar, "ypar":ypar})
g = sns.relplot(data=df, x='DFT', y='DNP', hue="Element", style="Surface", sizes=(100000), zorder=2, height=8.25, aspect=1)
l = sns.lineplot(x = "xpar", y = "ypar", data=linepar_df, c='red', zorder=0)
plt.legend(ncol=1, loc="lower right")
plt.xlabel("DFT (mJ/nm$^{3}$)", fontsize=24, fontweight='bold')
plt.ylabel("DNP (mJ/nm$^{3}$)", fontsize=24, fontweight='bold')
plt.errorbar(x, y, yerr=yerr, fmt=' ', c='black', zorder=1, lw=1, capsize=3, capthick=1)

# Hide the right and top spines
ax = sns.despine(bottom = False, left = False, top = False, right = False, )
sns.axes_style("ticks")
g._legend.remove()
plt.xlim(0,5000)
plt.ylim(0,5000)
plt.rcParams['xtick.labelsize'] = 50
plt.rcParams['ytick.labelsize'] = 50
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.gcf().subplots_adjust(bottom=0.12, left=0.13, wspace=1, hspace=1)

plt.show()
g.savefig('fig7.png')
