import matplotlib
matplotlib.use('nbagg') 
import matplotlib.pyplot as plt 
plt.rcParams['figure.dpi'] = 300
plt.rcParams['mathtext.fontset'] = 'cm' # (10, 6)
# Other functions from matplotlib 
from matplotlib.collections import PatchCollection
import matplotlib.path as mpath
import matplotlib.patches as mpatches

import matplotlib.lines as mlines


axes = plt.subplot(111)
circ = mpatches.Circle((0.5, 0.5), 0.1, fc='w', ec='k')
arrow = mpatches.Arrow(0.5+0.1, 0.51, 0.1, 0.0, width=0.05, fc='w', ec='k')
circ1 = mpatches.Circle((0.8, 0.5), 0.1, fc='w', ec='k')
arrow1 = mpatches.Arrow(0.8, 0.4, 0.0, -0.12, width=0.05, fc='w', ec='k')
axes.add_patch(circ)
axes.add_patch(arrow)
axes.add_patch(circ1)
axes.add_patch(arrow1)
axes.text(0.48, 0.49, 'Gut', fontsize=12)
axes.text(0.765, 0.49, 'Central', fontsize=12)
axes.text(0.63, 0.55, '$k_a$', fontsize=12)
axes.text(0.83, 0.35, '$CL$', fontsize=12)
axes.text(0.4, 0.3, "$\\bf{Figure.}$ One-compartment model\nwith first-order absorption",
         family="Roboto Mono Thin", weight=140, va='top')
axes.text(0.4, 0.35, 
          r"$C(t) = \frac{D\cdot k_a}{V(k_a - k)}\{exp(-k\cdot t) - exp(-k_a \cdot t)\}$",
         fontsize=12)
#axes.set_ylim(0, 0.9)
axes.spines['top'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['left'].set_visible(False)
axes.set_xticks([])
axes.set_yticks([])
plt.plot()
plt.savefig('com.eps')
