
import numpy
import matplotlib 
import random 
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
plt.xkcd() 

X = numpy.linspace(0, 12)
Y = 500 * 1.5 /25/(1.5 - 0.32) * (numpy.exp(-0.32*X) - numpy.exp(-1.5*X)) 

fig = plt.figure(figsize = (12,5), facecolor="white")
axes= plt.subplot(111) 
plt.plot(X,Y, color='r', linewidth=2, linestyle='-', zorder=+10)
axes.set_xlim(X.min(), X.max()) 
axes.set_ylim(1.01 * Y.min(), 1.01* Y.max()) 

axes.spines['top'].set_color('none') 
axes.spines['right'].set_color('none') 

axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

axes.spines['bottom'].set_position(("data", 0))
axes.spines['left'].set_position(("data", X.min())) 

axes.set_xticks([]) 
axes.set_yticks([]) 

axes.set_xlim(1.05 * X.min(), 1.10 * X.max())
axes.set_ylim( 1.15 * Y.min(), 1.05 * Y.max()) 
plt.ylabel(" Drug concentration ", fontsize=20 ,y=0.5)
plt.xlabel(" Time ", fontsize=20) 
plt.savefig('test.eps') 
