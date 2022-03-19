import numpy as np
import matplotlib.pyplot as plt


def Circle():
    """Draw a circle"""

    t = np.arange(0, 2*np.pi, 0.001)
    x = np.cos(t)
    y = np.sin(t)
    plt.figure(figsize=(10,10))

    plt.plot(x, y, color='k')
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.axis('off') 
    plt.savefig('circle.eps') 


if __name__ == '__main__':
    Circle()
