""""""
"""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
All Rights Reserved  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or edited.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT honor code violation.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""

import datetime as dt
import random

import pandas as pd
import util as ut
import QLearner as qLearner
from indicators_new import *
import marketsimcode as ms


class StrategyLearner(object):
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        If verbose = False your code should not generate ANY output.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type verbose: bool  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type impact: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type commission: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """

    # constructor  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        Constructor method  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        """
        self.verbose = verbose
        self.impact = impact
        self.commission = commission
        self.qLearner = qLearner.QLearner(num_states=10000,
                                          num_actions=3,
                                          alpha=0.2,
                                          gamma=0.9,
                                          rar=0.98,
                                          radr=0.999,
                                          dyna=0,
                                          verbose=False)
        #self.best_pos = {}
        self.prev_cum_ret_percent = 0
        self.df_trades_copy = pd.DataFrame()

    def author(self):
        return "mkurale3"

    # this method should create a QLearner, and train it for trading
    def add_evidence(
            self,
            symbol="IBM",
            sd=dt.datetime(2008, 1, 1),
            ed=dt.datetime(2009, 1, 1),
            sv=10000,
    ):
        """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        Trains your strategy learner over a given time frame.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param symbol: The stock symbol to train on  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type symbol: str  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type sd: datetime  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type ed: datetime  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type sv: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        """

        # add your code to do learning here  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 

        # example usage of the old backward compatible util function  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms,
                                 dates)  # automatically adds SPY
        prices = prices_all[
            syms]  # only portfolio symbols
        prices_SPY = prices_all[
            "SPY"]  # only SPY, for comparison later
        if self.verbose:
            print(prices)

        prices = prices.fillna(method="ffill").fillna(method="bfill")
        pricesDF_norm = prices / prices.iloc[0]
        price_sma = getSimpleMovingAverage(pricesDF_norm, syms)
        upper_bol_band, lower_bol_band = getBollingerBands(pricesDF_norm, syms)
        momentum = getMomentum(pricesDF_norm, syms)
        # daily_returns_df = getDailyReturns(pricesDF_norm)

        orders = pd.DataFrame(0, index=pricesDF_norm.index, columns=['Shares'])

        df_trades = pd.concat([orders], axis=1)
        df_trades.columns = ['Trades']

        self.df_trades_copy = df_trades.copy()
        indicators_df = pd.concat((price_sma, upper_bol_band, lower_bol_band, momentum), axis=1)
        discretized_states_df = self.discretize(indicators_df)

        # get the initial state by discretizing indicators
        hasNotConverged = True
        j = -1
        while hasNotConverged and j<200:
            init_pos = (sv, 0, [])  # cash, shares, [transactions]
            positions = [init_pos]
            j+=1;
            print(j)
            #self.best_pos = {}
            for day, date in enumerate(indicators_df.index):
                additional_pos = []
                price = prices.loc[date][symbol]
                for pos in positions:
                    if date == indicators_df.index[0]:
                        # On day 1 there is no reward only action of buy or sell shares
                        initial_state = discretized_states_df[date]
                        action = self.qLearner.querysetstate(initial_state) - 1
                    else:
                        # Every day after day 1 you have daily return rewards
                        prev_price = pricesDF_norm[symbol].iloc[day - 1]
                        curr_price = pricesDF_norm[symbol].loc[date]
                        reward = pos[1] * ((curr_price / prev_price) - 1) * (1 - self.impact)
                        state = discretized_states_df[date]
                        action = self.qLearner.query(state, reward)-1

                    if action == 1:
                        list_new_pos = self.implmentAction(pos, price, [1000, 2000, 0])
                        additional_pos.extend(list_new_pos)
                    elif action == -1:
                        list_new_pos = self.implmentAction(pos, price, [-2000, -1000, 0])
                        additional_pos.extend(list_new_pos)
                    else:
                        list_new_pos = self.implmentAction(pos, price, [0])
                        additional_pos.extend(list_new_pos)

                positions = self.determineBestPositions(additional_pos)
                if len(positions) == 0:
                    print("happy")

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
            hasNotConverged = not(self.determineConvergence(ordersDF, syms, sd, ed, sv, self.commission, self.impact))

        if (j==200):
            print("j reached 200")

            #return ordersDF

    def determineConvergence(self, ordersDF, syms, sd, ed, sv, comm, impact):
        # portvals = ms.compute_portvals(ordersDF, symbols=syms, startDate=sd,
        #                                endDate=ed, start_val=sv, commission=comm, impact=impact)
        # port_vals_normalized = portvals / portvals.iloc[0, 0]
        # if isinstance(port_vals_normalized, pd.DataFrame):
        #     port_vals_normalized = port_vals_normalized[port_vals_normalized.columns[0]]  # just get the first column
        # else:
        #     raise Exception("warning, code did not return a DataFrame")
        # cum_ret = (port_vals_normalized[-1] / port_vals_normalized[0]) - 1
        # cum_ret_percent = cum_ret * 100
        # if (abs(self.prev_cum_ret_percent - cum_ret_percent) < 1):
        #     print("converged")
        #     return True
        # else:
        #     self.prev_cum_ret_percent = cum_ret_percent
        if ordersDF.equals(self.df_trades_copy):
            return True
        else:
            self.df_trades_copy = ordersDF.copy()

        return False

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

    def implmentAction(self, pos, price, trades_allowed):
        additional_pos = []
        for trades in trades_allowed:
            new_shares = pos[1] + trades
            if new_shares not in [-1000, 0, 1000]:
                continue
            new_cash_holding = pos[0] - trades * price
            newOrder_transactions = pos[2] + [trades]
            new_pos = (new_cash_holding, new_shares, newOrder_transactions)
            additional_pos.append(new_pos)

        return additional_pos

    def discretize(self, data):

        upper_bol_bands = pd.cut(data['UPPER_BOL_BAND'], 10, labels=False)
        lower_bol_bands = pd.cut(data['LOWER_BOL_BAND'], 10, labels=False)
        price_sma = pd.cut(data['PRICE_SMA'], 10, labels=False)
        momentum = pd.cut(data['MOMENTUM'], 10, labels=False)

        return (upper_bol_bands * 1000) + (lower_bol_bands * 100) + (price_sma * 10) + momentum

    # this method should use the existing policy and test it against new data

    def testPolicy(
            self,
            symbol="IBM",
            sd=dt.datetime(2009, 1, 1),
            ed=dt.datetime(2010, 1, 1),
            sv=10000,
    ):
        """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        Tests your learner using data outside of the training data  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param symbol: The stock symbol that you trained on on  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type symbol: str  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type sd: datetime  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type ed: datetime  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :type sv: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        :rtype: pandas.DataFrame  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        """

        # here we build a fake set of trades  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        # your code should return the same sort of data  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 

        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms,
                                 dates)  # automatically adds SPY
        prices = prices_all[
            syms]  # only portfolio symbols
        prices_SPY = prices_all[
            "SPY"]  # only SPY, for comparison later
        if self.verbose:
            print(prices)

        prices = prices.fillna(method="ffill").fillna(method="bfill")
        pricesDF_norm = prices / prices.iloc[0]
        price_sma = getSimpleMovingAverage(pricesDF_norm, syms)
        upper_bol_band, lower_bol_band = getBollingerBands(pricesDF_norm, syms)
        momentum = getMomentum(pricesDF_norm, syms)
        # daily_returns_df = getDailyReturns(pricesDF_norm)

        indicators_df = pd.concat((price_sma, upper_bol_band, lower_bol_band, momentum), axis=1)
        discretized_states_df = self.discretize(indicators_df)
        init_pos = (sv, 0, [])  # cash, shares, [transactions]
        positions = [init_pos]
        # self.best_pos = {}
        for day, date in enumerate(indicators_df.index):
            additional_pos = []
            price = prices.loc[date][symbol]
            state = discretized_states_df[date]
            for pos in positions:
                if date == indicators_df.index[0]:
                    # On day 1 there is no reward only action of buy or sell shares
                    action = self.qLearner.querysetstate(state) - 1
                else:
                    # Every day after day 1 you have daily return rewards
                    prev_price = pricesDF_norm[symbol].iloc[day - 1]
                    curr_price = pricesDF_norm[symbol].loc[date]
                    reward = pos[1] * ((curr_price / prev_price) - 1) * (1 - self.impact)
                    action = self.qLearner.querysetstate(state) - 1

                if action == 1:
                    list_new_pos = self.implmentAction(pos, price, [1000, 2000, 0])
                    additional_pos.extend(list_new_pos)
                elif action == -1:
                    list_new_pos = self.implmentAction(pos, price, [-2000, -1000, 0])
                    additional_pos.extend(list_new_pos)
                else:
                    list_new_pos = self.implmentAction(pos, price, [0])
                    additional_pos.extend(list_new_pos)

            positions = self.determineBestPositions(additional_pos)
            if len(positions) == 0:
                print("happy")

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


if __name__ == "__main__":
    # learner = StrategyLearner(verbose=False, impact=9.95, commission=0.005)  # constructor
    # learner.add_evidence(symbol="AAPL", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
    #                      sv=100000)  # training phase
    print("One does not simply think up a strategy")

    # if (action == -1) and (total_holdings < 1000):
    #     buy_sell.loc[index]['Order'] = 'BUY'
    # if total_holdings == 0:
    #     orders.loc[index]['Shares'] = 1000
    #     total_holdings += 1000
    # else:
    #     orders.loc[index]['Shares'] = 2000
    #     total_holdings += 2000
    # elif (action == 1) and (total_holdings > -1000):\
    #     buy_sell.loc[index]['Order'] = 'SELL'
    # if total_holdings == 0:
    #     orders.loc[index]['Shares'] = -1000
    #     total_holdings = total_holdings - 1000
    # else:
    #     orders.loc[index]['Shares'] = -2000
    #     total_holdings = total_holdings - 2000
