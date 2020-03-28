import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def mu_estimate(x:np.ndarray,alph:float,sigma=None,color='black',label=None):
    """
    Bilateral confidence intervals
    1 - alph: confidence level
    """
    """Each column contains one sample"""
    x_bar = x.mean(axis=0)
    row,column = x.shape
    if sigma:
        std = np.sqrt(sigma)
    else:
        std = x.std(axis=0)
    for i in range(column):
        tmp = stats.norm.interval(1-alph, loc=x_bar[i], scale=std)
        plt.plot([i]*2,np.linspace(tmp[0],tmp[1],2),c='black')
    
    plt.legend()
    plt.show()