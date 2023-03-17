#! /usr/bin/python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as Axes
import numpy as np
import seaborn as sns

df=pd.read_csv("inter.ssv", header=0, sep='\s+')
print (df)
x=df["pDFT"]
y=df["pDNP"]
yerr=df["psd"]
#z=df["INTER"]
Atm=df["Ele"]
xpar=[-10,15]
ypar=[-10,15]
linepar_df=pd.DataFrame({"xpar":xpar, "ypar":ypar})

g = sns.relplot(data=df, x='pDFT', y='pDNP', hue="Ele", zorder=2, height=6.75, aspect=1)
l = sns.lineplot(x = "xpar", y = "ypar", data=linepar_df, c='red', zorder=0)

plt.legend(ncol=1, bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("DFT (eV)", fontsize=24, fontweight='bold')
plt.ylabel("DNP (eV)", fontsize=24, fontweight='bold')
plt.title( 'B)', x=0.05, y=0.9, fontsize=24, fontweight='bold') 
plt.errorbar(x, y, yerr=yerr, fmt=' ', c='black', zorder=0, lw=1, capsize=3, capthick=1)

# Hide the right and top spines
ax = sns.despine(bottom = False, left = False, top = False, right = False, )
sns.axes_style("ticks")
g._legend.remove()

plt.legend([],[], frameon=False)
plt.xlim(-1,11)
plt.ylim(-1,11)
plt.rcParams['xtick.labelsize'] = 2
plt.rcParams['ytick.labelsize'] = 2
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.gcf().subplots_adjust(bottom=0.12, left=0.12, wspace=0, hspace=0)

plt.show()
g.savefig('fig3B.png')
