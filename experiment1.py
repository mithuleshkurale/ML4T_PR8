import ManualStrategy as man_strat
import StrategyLearner as strat_learner
import marketsimcode as ms
import datetime as dt
from matplotlib import pyplot as plt
import pandas as pd


def author():
    return "mkurale"

def generate_insample_strategy_manual_benchmark_graph(port_vals_manual_normalized, port_vals_benchmark_normalized,
                                             port_vals_learner_normalized):
    df_temp = pd.concat([port_vals_manual_normalized, port_vals_benchmark_normalized, port_vals_learner_normalized],
                        keys=['Manual Strategy Normalized', 'Benchmark Normalized', 'Strategy Q Learner'],
                        axis=1)
    ax = df_temp.plot(kind='line', y='Manual Strategy Normalized', color='red')
    df_temp.plot(kind='line', y='Benchmark Normalized', color='purple', ax=ax)
    df_temp.plot(kind='line', y='Strategy Q Learner Normalized', color='blue', ax=ax)
    plt.title("In Sample Manual vs Benchmark vs Strategy Q Learner Normalized")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Values")
    plt.legend(['Manual', 'Benchmark', 'Strategy Q Learner'])
    plt.savefig('images/Figure4.png')
    # plt.show()
    plt.close()


def generate_outsample_strategy_manual_benchmark_graph(port_vals_manual_normalized, port_vals_benchmark_normalized,
                                              port_vals_learner_normalized):
    df_temp = pd.concat([port_vals_manual_normalized, port_vals_benchmark_normalized, port_vals_learner_normalized],
                        keys=['Manual Strategy Normalized', 'Benchmark Normalized', 'Strategy Q Learner'],
                        axis=1)
    ax = df_temp.plot(kind='line', y='Manual Strategy Normalized', color='red')
    df_temp.plot(kind='line', y='Benchmark Normalized', color='purple', ax=ax)
    df_temp.plot(kind='line', y='Strategy Q Learner Normalized', color='blue', ax=ax)
    plt.title("Out Sample Manual vs Benchmark vs Strategy Q Learner Normalized")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Values")
    plt.legend(['Manual', 'Benchmark', 'Strategy Q Learner'])
    plt.savefig('images/Figure3.png')
    # plt.show()
    plt.close()


def inSample_Strategy_Manual_Benchmark():
    # Manual
    manual_trades_df = man_strat.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
                                            sv=100000)
    portvals_manual = ms.compute_portvals(manual_trades_df, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                          endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95,
                                          impact=0.005)

    port_vals_manual_normalized = portvals_manual / portvals_manual.iloc[0, 0]

    # Benchmark
    benchMarkTrades_DF = man_strat.benchMark(symbol=["JPM"], sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
    port_vals_benchmark = ms.compute_portvals(benchMarkTrades_DF, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                              endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95,
                                              impact=0.005)

    port_vals_benchmark_normalized = port_vals_benchmark / port_vals_benchmark.iloc[0, 0]

    # Strategy
    learner = strat_learner.StrategyLearner(verbose=False, impact=9.95, commission=0.005)
    learner.add_evidence(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    trades_df = learner.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    portvals_learner = ms.compute_portvals(trades_df, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                           endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95,
                                           impact=0.005)
    port_vals_learner_normalized = portvals_learner / portvals_learner.iloc[0, 0]

    # generate chart
    generate_insample_strategy_manual_benchmark_graph(port_vals_manual_normalized, port_vals_benchmark_normalized,
                                             port_vals_learner_normalized)


def outSample_Strategy_Manual_Benchmark():
    # Manual
    manual_trades_df = man_strat.testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31),
                                            sv=100000)
    portvals_manual = ms.compute_portvals(manual_trades_df, symbols=["JPM"], startDate=dt.datetime(2010, 1, 1),
                                          endDate=dt.datetime(2011, 12, 31), start_val=100000, commission=9.95,
                                          impact=0.005)

    port_vals_manual_normalized = portvals_manual / portvals_manual.iloc[0, 0]

    # Benchmark
    benchMarkTrades_DF = man_strat.benchMark(symbol=["JPM"], sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31))
    port_vals_benchmark = ms.compute_portvals(benchMarkTrades_DF, symbols=["JPM"], startDate=dt.datetime(2010, 1, 1),
                                              endDate=dt.datetime(2011, 12, 31), start_val=100000, commission=9.95,
                                              impact=0.005)

    port_vals_benchmark_normalized = port_vals_benchmark / port_vals_benchmark.iloc[0, 0]

    # Strategy
    learner = strat_learner.StrategyLearner(verbose=False, impact=9.95, commission=0.005)
    learner.add_evidence(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000)
    trades_df = learner.testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000)
    portvals_learner = ms.compute_portvals(trades_df, symbols=["JPM"], startDate=dt.datetime(2010, 1, 1),
                                           endDate=dt.datetime(2011, 12, 31), start_val=100000, commission=9.95,
                                           impact=0.005)
    port_vals_learner_normalized = portvals_learner / portvals_learner.iloc[0, 0]

    # generate chart
    generate_outsample_strategy_manual_benchmark_graph(port_vals_manual_normalized, port_vals_benchmark_normalized,
                                              port_vals_learner_normalized)

def run():
    inSample_Strategy_Manual_Benchmark()
    outSample_Strategy_Manual_Benchmark()