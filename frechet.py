import numpy as np
from scipy.special import gamma as G, gammaincc as Ginc
from distribution import Distribution

class Frechet(Distribution):
    def __init__(self, gamma):
        self.gamma = gamma
        self.xi = 1/gamma

    def get_label(self):
        return "Frechet({})".format(round(self.gamma, 2))

    def cdf(self, x):
        gamma = self.gamma
        return np.exp(-x**(-gamma))

    def pdf(self, x):
        gamma = self.gamma
        return gamma * x**(-1-gamma) * self.cdf(x)

    def var(self, alph):
        gamma = self.gamma
        return (-np.log(alph))**(-1/gamma)

    def cvar(self, alph):
        gamma = self.gamma
        a = (gamma-1)/gamma
        x = -np.log(alph)
        return 1/(1-alph) * (G(a) - Ginc(a,x)*G(a))
