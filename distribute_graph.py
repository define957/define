import numpy as np
from scipy import stats as stats
import matplotlib.pyplot as plt

def show

def f_distribution_graph(m, n, ub, label=None, color=None,legend_position='best'):
    """
    m: degree of freedom m
    n:degree of freedom n
    ub: x-axis limit
    legend_position: ''
    """
    x = np.linspace(0, ub, 1000)
    y = stats.f.pdf(x, m, n)
    plt.plot(x, y, label=label, c=color)
    plt.xlim(0,ub)
    plt.legend()
    plt.legend()


def