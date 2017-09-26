import numpy as np
import pandas as pd


class BlackLitterman():

    def __init__(self, marketCaps, prices, riskAversion = 1, frequency = 'W'):
        self.marketCaps = marketCaps
        self.marketWeights = marketCaps / marketCaps.sum()
        self.riskAversion = riskAversion

        self.prices = prices.resample('W').last()


        self.returns = self.prices / self.prices.shift(1) - 1

        self.covarianceMatrix = self.returns.cov()
        self.correlationMatrix = self.returns.corr()

    def calculateImpliedReturn(self):


        self.impliedReturn = self.riskAversion * self.covarianceMatrix.dot(self.marketWeights)

        return self.impliedReturn

