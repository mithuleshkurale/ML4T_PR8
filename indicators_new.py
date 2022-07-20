import matplotlib.pyplot as plt
import pandas as pd
from util import get_data


def author():
    return 'mkurale3'


def getBollingerBands(pricesDF, syms):
    rm_JPM = pricesDF[syms].rolling(30).mean()
    rstd_JPM = pricesDF[syms].rolling(30).std()
    upper_bound = rm_JPM + rstd_JPM * 2
    lower_bound = rm_JPM - rstd_JPM * 2
    #percent_B = (pricesDF[syms] - lower_bound / pricesDF[syms] - upper_bound) * 100
    
    return upper_bound, lower_bound

def getSimpleMovingAverage(pricesDF, syms):
    rm_JPM = pricesDF[syms].rolling(30).mean()
    price_sma = pricesDF[syms] / rm_JPM
    
    return price_sma

def getMomentum(pricesDF, syms):
    momentum = pricesDF[syms] / pricesDF[syms].shift(30) - 1
    
    return momentum
    
def getMACD(pricesDF, syms):
    twelve_day_EMA = pricesDF[syms].ewm(span=12).mean()
    twenty_six_day_EMA = pricesDF[syms].ewm(span=26).mean()
    MACD = twelve_day_EMA - twenty_six_day_EMA
    signal = MACD.ewm(span=9).mean()
    histogram = MACD - signal
    
    return MACD
    
def getPercentagePriceCalculator(pricesDF, syms):
    twelve_day_EMA = pricesDF[syms].ewm(span=12).mean()
    twenty_six_day_EMA = pricesDF[syms].ewm(span=26).mean()
    MACD = twelve_day_EMA - twenty_six_day_EMA
    PPO = (MACD / twenty_six_day_EMA) * 100
    signal = MACD.ewm(span=9).mean()
    
    return PPO

def getDailyReturns(pricesDF):
    return (pricesDF/ pricesDF.shift(1))-1

def run_indicators(pricesDF, syms):
    pricesDF_norm = pricesDF / pricesDF.iloc[0]

    upper_band, lower_band = getBollingerBands(pricesDF, syms)
    price_sma = getSimpleMovingAverage(pricesDF, syms)
    momentum = getMomentum(pricesDF, syms)
    macd = getMACD(pricesDF, syms)
    ppc = getPercentagePriceCalculator(pricesDF, syms)
    
    return upper_band, lower_band, price_sma, momentum, macd, ppc