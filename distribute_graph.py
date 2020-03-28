import numpy as np
from scipy import stats as stats
import matplotlib.pyplot as plt


def f_distribution_graph(m, n, ub, label=None, color=None,legend_position='best') -> None:
    """
    m: degree of freedom m
    n:degree of freedom n
    ub: x-axis limit
    """
    x = np.linspace(0, ub, 1000)
    y = stats.f.pdf(x, m, n)
    plt.plot(x, y, label=label, c=color)
    plt.xlim(0,ub)
    plt.legend()


def t_distribution_graph(n: int, lb: float, ub: float, label=None, color=None) -> None:
    """
    n:degree of freedom n
    lb and ub : lower bound and upper bound
    label:the label of graph
    """
    x = np.linspace(lb, ub)
    y = stats.t.pdf(x, n)
    plt.plot(x, y, label=label, c=color)
    plt.xlim(lb,ub)
    plt.legend()


def chi2_distribution_graph(n: int, ub: float, label=None, color=None) -> None:
    """

    :param n:  degree of freedom
    :param ub: graph upper bound
    :param label: name of line
    :param color: color of line
    :return: None
    """
    x = np.linspace(0, ub)
    y = stats.chi2.pdf(x, n)
    plt.plot(x, y, label=label, c=color)
    plt.xlim(0, ub)
    plt.legend()



