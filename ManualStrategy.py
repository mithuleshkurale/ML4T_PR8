import numpy as np
import pandas as pd
from indicators import *
import datetime as dt
import util as ut


class ManualStrategy(object):

    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """
        Constructor method
        """
        self.verbose = verbose
        self.impact = impact
        self.commission = commission

    def author(self):
        return "mkurale3"

    def testPolicy(self, symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000):
        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols

        prices = prices.fillna(method="ffill").fillna(method="bfill")
        pricesDF_norm = prices / prices.iloc[0]

        # indicator 1: price/sma
        sma = getSimpleMovingAverage(pricesDF_norm, syms)

        # indicator 2: Upper/Lower bollinger bands
        bbp = getBollingerBandsPercent(pricesDF_norm, syms)

        # indicator 3: Momentum
        momentum = getMomentum(pricesDF_norm, syms)

        # indicators_df = pd.concat((price_sma, bbp, momentum), axis=1)
        signals_df = pd.DataFrame()

        signals_df['SMA_SIGNAL'] = np.where(sma['20_SMA'] > sma['50_SMA'], 1, -1)

        signals_df['MOMENTUM_SIGNAL'] = np.where((momentum['MOMENTUM'] > 0) & (momentum['MOMENTUM'].shift(1) < 0), 1, 0)
        signals_df['MOMENTUM_SIGNAL'] = np.where((momentum['MOMENTUM'] < 0) & (momentum['MOMENTUM'].shift(1) > 0), -1,
                                                 signals_df['MOMENTUM_SIGNAL'])

        signals_df['PERCENT_BOL_BAND_SIGNAL'] = np.where(
            (bbp['PERCENT_BOL_BAND'] >= 0.75) & (bbp['PERCENT_BOL_BAND'].shift(1) < 0.75), 1, 0)
        signals_df['PERCENT_BOL_BAND_SIGNAL'] = np.where(
            (bbp['PERCENT_BOL_BAND'] < 0.2) & (bbp['PERCENT_BOL_BAND'].shift(1) >= 0.2), -1,
            signals_df['PERCENT_BOL_BAND_SIGNAL'])

        signals_df['Final_Decision'] = np.where(signals_df.sum(axis=1) > 1, 1, 0)
        signals_df['Final_Decision'] = np.where(signals_df.sum(axis=1) <= -1, -1, signals_df['Final_Decision'])

        init_pos = (sv, 0, [])  # cash, shares, [transactions]
        positions = [init_pos]
        net_shares = 0
        for day, date in enumerate(signals_df.index):
            additional_pos = []
            price = prices.iloc[day][0]
            signal = signals_df.loc[date]['Final_Decision']
            if signal == 1:
                for pos in positions:
                    list_new_pos = self.implmentAction(pos, price, [1000, 0, 2000], 'buy', self.impact, self.commission)
            elif signal == -1:
                for pos in positions:
                    list_new_pos = self.implmentAction(pos, price, [-2000, 0, -1000], 'sell', self.impact, self.commission)
            else:
                for pos in positions:
                    list_new_pos = self.implmentAction(pos, price, [0], 'do nothing', self.impact, self.commission)

            additional_pos.extend(list_new_pos)
            positions = self.determineBestPositions(additional_pos)

        avgPrice = prices[symbol].mean()

        # determine the best position that maximizes cash holdings of liquid and nonliquid
        max_position = positions[0]
        for i in range(1, len(positions)):
            curr_pos = positions[i]
            if (curr_pos[0] + curr_pos[1] * avgPrice) > (max_position[0] + max_position[1] * avgPrice):
                max_position = curr_pos

        ordersDF = pd.DataFrame(max_position[2], columns=['Trades'])
        ordersDF['Date'] = prices.index
        ordersDF = ordersDF.set_index('Date')

        return ordersDF

    def determineBestPositions(self, positions):
        best_pos = {}
        for pos in positions:
            cash_holding = pos[0]
            net_holdings = pos[1]
            # update the record if new cash val for existing net holdings is greater
            if net_holdings in best_pos and cash_holding > best_pos[net_holdings][0]:
                best_pos[net_holdings] = pos
            elif net_holdings not in best_pos:
                best_pos[net_holdings] = pos

        return list(best_pos.values())

    def implmentAction(self, pos, price, trades_allowed, action, impact, commission):
        additional_pos = []
        for trades in trades_allowed:
            new_shares = pos[1] + trades
            if new_shares not in [-1000, 0, 1000]:  # we can only have net positions of -1k, 0, 1K
                continue
            if action == 'buy' and trades!=0:
                new_cash_holding = pos[0] - (trades * (price + impact) - commission)
            elif action == 'sell' and trades!=0:
                new_cash_holding = pos[0] - (trades * (price - impact) - commission)
            else:
                new_cash_holding = pos[0]

            newOrder_transactions = pos[2] + [trades]
            new_pos = (new_cash_holding, new_shares, newOrder_transactions)
            additional_pos.append(new_pos)

        return additional_pos

    def benchMark(self, symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31)):
        pricesDF = ut.get_data(symbol, pd.date_range(sd, ed))
        pricesDF = pricesDF.fillna(method="ffill").fillna(method="bfill")
        pricesDF.drop(columns=["SPY"], inplace=True)

        ordersDF = pd.DataFrame(columns=['Date', 'Trades'])
        ordersDF['Date'] = pricesDF.index
        ordersDF.loc[0, 'Trades'] = 1000
        ordersDF = ordersDF.set_index('Date')
        ordersDF['Trades'] = ordersDF['Trades'].fillna(0)
        return ordersDF


if __name__ == "__main__":
    ms = ManualStrategy(verbose=False, impact=.005, commission=9.95)
    ms.testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000);

# if net_shares == -1000:
#     # buy 1000, 2000
#     if price_sma_val < 0.7 or bbp < 0.2 or momentum_val > 0:
#         trades_DF.loc[date] = [symbol, 2000]
#         net_shares = 1000
#
#     if price_sma_val < 0.6 or bbp < 0.2 or momentum_val > 0:
#         trades_DF.loc[date] = [symbol, 1000]
#         net_shares = 0
#
# elif net_shares == 0:
#     # buy 1000, sell 1000
#     if price_sma_val < 0.6 or bbp < 0.2 or momentum_val > 0:
#         trades_DF.loc[date] = [symbol, 1000]
#         net_shares = 1000
#
#     if price_sma_val > 1.0 or bbp > 0.75 or momentum_val < 0:
#         trades_DF.loc[date] = [symbol, -1000]
#         net_shares = -1000
#
# elif net_shares == 1000:
#     # sell -2000, -1000
#     if price_sma_val > 1.5 or bbp >= 0.75 or momentum_val > 0:
#         trades_DF.loc[date] = [symbol, -2000]
#         net_shares = -1000
#
#     if price_sma_val > 1.0 or bbp >= 0.75 or momentum_val > 0.1:
#         trades_DF.loc[date] = [symbol, -1000]
#         net_shares = 0
