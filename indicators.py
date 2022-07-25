import numpy as np
import pandas as pd


def author():
    return 'mkurale3'


def getBollingerBandsPercent(pricesDF, syms):
    rm = pricesDF[syms].rolling(20).mean()
    rstd = pricesDF[syms].rolling(20).std()
    upper_bound = rm + rstd * 2
    lower_bound = rm - rstd * 2
    percent_B = (pricesDF[syms] - lower_bound) / (upper_bound - lower_bound)
    percent_B = percent_B.fillna(0)
    percent_B.rename(columns={syms[0]: 'PERCENT_BOL_BAND'}, inplace=True)
    return percent_B


def getSimpleMovingAverage(pricesDF, syms):
    sma_indicator_DF = pricesDF.copy()
    sma_indicator_DF['20_SMA'] = pricesDF[syms].rolling(20).mean()
    sma_indicator_DF['50_SMA'] = pricesDF[syms].rolling(50).mean()
    sma_indicator_DF = sma_indicator_DF.fillna(0)
    return sma_indicator_DF


def getMomentum(pricesDF, syms):
    momentum = pricesDF[syms] / pricesDF[syms].shift(30) - 1
    momentum = momentum.fillna(0)
    momentum.rename(columns={syms[0]: 'MOMENTUM'}, inplace=True)
    return momentum
