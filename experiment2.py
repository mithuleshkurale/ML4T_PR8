import math

import StrategyLearner as strat_learner
import datetime as dt
import marketsimcode as ms
import pandas as pd
from matplotlib import pyplot as plt

def author():
    return "mkurale3"


def graphThePortVals(normalized_portvals):
    line1 = normalized_portvals[0][1]
    line2 = normalized_portvals[1][1]
    line3 = normalized_portvals[2][1]
    line4 = normalized_portvals[3][1]

    df_temp = pd.concat([line1, line2, line3, line4],
                        keys=['Line 1', 'Line 2', 'Line 3', 'Line 4'],
                        axis=1)
    ax = df_temp.plot(kind='line', y='Line 1', color='red')
    df_temp.plot(kind='line', y='Line 2', color='purple', ax=ax)
    df_temp.plot(kind='line', y='Line 3', color='blue', ax=ax)
    df_temp.plot(kind='line', y='Line 4', color='black', ax=ax)
    plt.title("Experiment 2")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Values")
    plt.legend(['impact = 1.0', 'impact = 0.4', 'impact = .06', 'impact = .007'])
    plt.savefig('images/Figure5.png')
    # plt.show()
    plt.close()


def run():
    impacts = [1.0, .4, .06, .007]
    normalized_portvals = []
    for impact in impacts:
        learner = strat_learner.StrategyLearner(verbose=False, impact=impact, commission=0)
        learner.add_evidence(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
        trades_df = learner.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
                                       sv=100000)

        number_of_trades = trades_df[trades_df["Trades"]!=0].shape[0]
        print("Impact: " + str(impact) + " number of trades are: " + str(number_of_trades))

        portvals_learner = ms.compute_portvals(trades_df, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                               endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95,
                                               impact=impact)

        port_vals_learner_normalized = portvals_learner / portvals_learner[0]
        normalized_portvals.append([impact, port_vals_learner_normalized.to_frame()]);

    graphThePortVals(normalized_portvals)
    calc_stats(normalized_portvals)

def calc_stats(normalized_portvals):
    pval1 = normalized_portvals[0][1]
    pval1 = pval1[pval1.columns[0]]

    pval2 = normalized_portvals[1][1]
    pval2 = pval2[pval2.columns[0]]

    pval3 = normalized_portvals[2][1]
    pval3 = pval3[pval3.columns[0]]

    pval4 = normalized_portvals[3][1]
    pval4 = pval4[pval4.columns[0]]

    'impact = 1.0', 'impact = 0.4', 'impact = .06', 'impact = .007'
    #impact = 1.0
    dr_1 = (pval1 / pval1.shift(1)) - 1
    cum_ret1 = (pval1[-1] / pval1[0]) - 1
    std_1 = ((pval1 / pval1.shift(1)) - 1).std()
    sharp_ratio_1 = math.sqrt(252) * (dr_1.mean() / std_1)

    #impact = 0.4
    dr_2 = (pval2 / pval2.shift(1)) - 1
    cum_ret_2 = (pval2[-1] / pval2[0]) - 1
    std_2 = ((pval2 / pval2.shift(1)) - 1).std()
    sharp_ratio_2 = math.sqrt(252) * (dr_2.mean() / std_2)

    #impact = 0.6
    dr_3 = (pval3 / pval3.shift(1)) - 1
    cum_ret_3 = (pval3[-1] / pval3[0]) - 1
    std_3 = ((pval3 / pval3.shift(1)) - 1).std()
    sharp_ratio_3 = math.sqrt(252) * (dr_3.mean() / std_3)

    #impact = 0.007
    dr_4 = (pval4 / pval4.shift(1)) - 1
    cum_ret_4 = (pval4[-1] / pval4[0]) - 1
    std_4 = ((pval4 / pval4.shift(1)) - 1).std()
    sharp_ratio_4 = math.sqrt(252) * (dr_4.mean() / std_4)

    print("Impact = 1.0")
    print("avg_daily_return: " +str(dr_1.mean()))
    print("cumulative return: " + str(cum_ret1))
    print("standard deviation: " + str(std_1))
    print("sharp ratio: " + str(sharp_ratio_1))

    print("Impact = 0.4")
    print("avg_daily_return: " + str(dr_2.mean()))
    print("cumulative return: " + str(cum_ret_2))
    print("standard deviation: " + str(std_2))
    print("sharp ratio: " + str(sharp_ratio_2))

    print("Impact = .06")
    print("avg_daily_return: " + str(dr_3.mean()))
    print("cumulative return: " + str(cum_ret_3))
    print("standard deviation: " + str(std_3))
    print("sharp ratio: " + str(sharp_ratio_3))

    print("Impact = .007")
    print("avg_daily_return: " + str(dr_4.mean()))
    print("cumulative return: " + str(cum_ret_4))
    print("standard deviation: " + str(std_4))
    print("sharp ratio: " + str(sharp_ratio_4))




if __name__ == "__main__":
    run()
