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
        """return the size of ever sample"""
        return self.x.shape[1]

    @property
    def sample_mean(self):
        return self.x.mean(axis=1)

    @property
    def sample_std(self):
        """calculate the sample standard variance"""
        return np.sqrt(self.sample_var)

    @property
    def sample_var(self):
        row,clo = self.x.shape
        ex = self.x.mean(axis=1)
        ex = ex.reshape(row, 1)
        var = np.sum(np.power(self.x - ex, 2),axis=1)/(clo-1)
        return var

    def plot_mu_estimate(self,alpha: float, vartype='unbiased', sigma=None, color='black',label=None):
        """
        Bilateral confidence intervals
        1 - alph: confidence level
        """
        """Each column contains one sample"""
        x_bar = self.x.mean(axis=1)
        row, column = self.x.shape
        if sigma:
            std = np.sqrt(sigma)
        elif vartype =='biased':
            std = self.x.std(axis=1)
        elif vartype == 'unbiased':
            std = np.sqrt(self.sample_var)

        for i in range(row):
            tmp = stats.norm.interval(1-alpha, loc=x_bar[i], scale=std)
            plt.plot([i]*2, np.linspace(tmp[0], tmp[1], 2), c='black')
        plt.xlabel("sample")
        plt.legend()
        plt.show()
