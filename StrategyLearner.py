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

import util as ut
import QLearner as qLearner
from indicators import *


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
        self.orderDF_copy = pd.DataFrame()

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

        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
        if self.verbose:
            print(prices)

        prices = prices.fillna(method="ffill").fillna(method="bfill")
        pricesDF_norm = prices / prices.iloc[0]

        # indicator 1: price/sma
        price_sma = getSimpleMovingAverage(pricesDF_norm, syms)
        price_sma = price_sma.drop(symbol, axis=1)

        # indicator 2: Upper/Lower bollinger bands
        bbp = getBollingerBandsPercent(pricesDF_norm, syms)

        # indicator 3: Momentum
        momentum = getMomentum(pricesDF_norm, syms)

        # concat the indicators to one data frame
        indicators_df = pd.concat((price_sma, bbp, momentum), axis=1)

        # pass the indicators df to discretize. Will return a df with discretized values
        discretized_states_df = self.discretize(indicators_df)

        # create a copy of orderDF. This will be used to determine if convergence has occurred
        self.orderDF_copy = pd.DataFrame(0, index=pricesDF_norm.index, columns=['Trades'])

        hasNotConverged = True
        j = -1
        while hasNotConverged and j < 300:
            init_pos = (sv, 0, [])  # cash, shares, [transactions]
            positions = [init_pos]
            j += 1;

            for day, date in enumerate(indicators_df.index):
                additional_pos = []
                price = prices.loc[date][symbol]
                for pos in positions:
                    if date == indicators_df.index[0]:
                        # On day 1 there is no daily return reward only action of buy or sell shares
                        initial_state = discretized_states_df[date]
                        action = self.qLearner.querysetstate(initial_state) - 1
                    else:
                        # Every day after day 1 you have daily return rewards
                        prev_price = pricesDF_norm[symbol].iloc[day - 1]
                        curr_price = pricesDF_norm[symbol].loc[date]
                        reward = pos[1] * ((curr_price / prev_price) - 1)
                        state = discretized_states_df[date]
                        action = self.qLearner.query(state, reward) - 1

                    """
                    action = -1: Sell 1k, 2K
                    action = 0: Do nothing
                    action = 1: Buy 1K, 2K
                    
                    Will implement the action based on the query result
                    """
                    if action == 1:
                        list_new_pos = self.implmentAction(pos, price, [1000, 2000, 0], 'buy', self.impact, self.commission)
                        additional_pos.extend(list_new_pos)
                    elif action == -1:
                        list_new_pos = self.implmentAction(pos, price, [-2000, -1000, 0], 'buy', self.impact, self.commission)
                        additional_pos.extend(list_new_pos)
                    else:
                        list_new_pos = self.implmentAction(pos, price, [0], 'do nothing', self.impact, self.commission)
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
            hasNotConverged = not (self.determineConvergence(ordersDF))

        if (j == 400):
            print("j reached 400")

    def determineConvergence(self, ordersDF):
        if ordersDF.equals(self.orderDF_copy):
            print("converged")
            return True
        else:
            self.orderDF_copy = ordersDF.copy()

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

    def implmentAction(self, pos, price, trades_allowed, action, impact, commission):
        additional_pos = []
        for trades in trades_allowed:
            new_shares = pos[1] + trades
            if new_shares not in [-1000, 0, 1000]: #we can only have net positions of -1k, 0, 1K
                continue
            if action == 'buy' and trades!=0:
                new_cash_holding = pos[0] - (trades * (price+impact) - commission)
            elif action=='sell' and trades!=0:
                new_cash_holding = pos[0] - (trades * (price-impact) - commission)
            else:
                new_cash_holding = pos[0]

            newOrder_transactions = pos[2] + [trades]
            new_pos = (new_cash_holding, new_shares, newOrder_transactions)
            additional_pos.append(new_pos)

        return additional_pos

    def discretize(self, data):

        percent_bol_bands = pd.cut(data['PERCENT_BOL_BAND'], 10, labels=False)
        price_20_sma = pd.cut(data['20_SMA'], 10, labels=False)
        price_50_sma = pd.cut(data['50_SMA'], 10, labels=False)
        momentum = pd.cut(data['MOMENTUM'], 10, labels=False)

        return (percent_bol_bands * 1000) + (price_20_sma * 100) + (price_50_sma * 10) + (momentum * 1)

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
        bbp = getBollingerBandsPercent(pricesDF_norm, syms)
        momentum = getMomentum(pricesDF_norm, syms)
        # daily_returns_df = getDailyReturns(pricesDF_norm)

        indicators_df = pd.concat((price_sma, bbp, momentum), axis=1)
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
                    action = self.qLearner.querysetstate(state) - 1

                if action == 1:
                    list_new_pos = self.implmentAction(pos, price, [1000, 2000, 0], 'buy', self.impact, self.commission)
                    additional_pos.extend(list_new_pos)
                elif action == -1:
                    list_new_pos = self.implmentAction(pos, price, [-2000, -1000, 0], 'sell', self.impact,
                                                       self.commission)
                    additional_pos.extend(list_new_pos)
                else:
                    list_new_pos = self.implmentAction(pos, price, [0], 'do nothing', self.impact, self.commission)
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
    learner = StrategyLearner(verbose=False, impact=.005, commission=9.95)  # constructor
    learner.add_evidence(symbol="AAPL", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
                         sv=100000)  # training phase
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
