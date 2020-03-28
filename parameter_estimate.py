import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


class NormSample(object):
    """That means the population is normally distributed"""
    
    def __init__(self, x: np.ndarray):
        self.x = x

    @property
    def shape(self):
        return self.x.shape

    @property
    def sample_size(self):
        return self.x.shape[1]

    @property
    def sample_mean(self):
        return self.x.mean(axis=0)

    @property
    def sample_std(self):
        return self.x.std(axis=1)

    @property
    def sample_var(self):
        return self.x.var(axis=1)

    def mu_estimate(self,alpha: float, sigma=None, color='black',label=None):
        """
        Bilateral confidence intervals
        1 - alph: confidence level
        """
        """Each column contains one sample"""
        x_bar = self.x.mean(axis=0)
        row, column = self.x.shape
        if sigma:
            std = np.sqrt(sigma)
        else:
            std = self.x.std(axis=0)
        for i in range(column):
            tmp = stats.norm.interval(1-alpha, loc=x_bar[i], scale=std)
            plt.plot([i]*2, np.linspace(tmp[0], tmp[1], 2), c='black')

        plt.legend()
        plt.show()
