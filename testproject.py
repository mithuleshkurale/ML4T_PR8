import datetime as dt
import pandas as pd
from matplotlib import pyplot as plt
import ManualStrategy as man_strat
import marketsimcode as ms
import experiment1 as exp1
import experiment2 as exp2


def author():
    return 'mkurale3'


def printManualAndBenchmarkPerfMetrics(insample_portvals_manual, insample_portvals_benchmark, outsample_portvals_manual, outsample_portvals_benchmark):
    if isinstance(insample_portvals_manual, pd.DataFrame) and isinstance(outsample_portvals_manual, pd.DataFrame):
        insample_portvals_manual = insample_portvals_manual[insample_portvals_manual.columns[0]]  # just get the first column
        outsample_portvals_manual = outsample_portvals_manual[outsample_portvals_manual.columns[0]]  # just get the first column
    else:
        raise Exception("warning, code did not return a DataFrame")

    daily_ret_insample_manual = (insample_portvals_manual / insample_portvals_manual.shift(1)) - 1
    cum_ret_insample_manual = (insample_portvals_manual[-1] / insample_portvals_manual[0]) - 1
    avg_daily_ret_insample_manual = daily_ret_insample_manual.mean()
    std_daily_ret_insample_manual = daily_ret_insample_manual.std()

    cum_ret_insample_manual = "{:.6}".format(cum_ret_insample_manual)
    avg_daily_ret_insample_manual = "{:.6}".format(avg_daily_ret_insample_manual)
    std_daily_ret_insample_manual = "{:.6}".format(std_daily_ret_insample_manual)

    print("Manual Strategy data in sample")
    print("avg daily return insample: " + avg_daily_ret_insample_manual)
    print("std daily return insample: " + std_daily_ret_insample_manual)
    print("cumulative return outsample: " + cum_ret_insample_manual)


    daily_ret_outsample_manual = (outsample_portvals_manual / outsample_portvals_manual.shift(1)) - 1
    cum_ret_outsample_manual = (outsample_portvals_manual[-1] / outsample_portvals_manual[0]) - 1
    avg_daily_ret_outsample_manual = daily_ret_outsample_manual.mean()
    std_daily_ret_outsample_manual = daily_ret_outsample_manual.std()

    cum_ret_outsample_manual = "{:.6}".format(cum_ret_outsample_manual)
    avg_daily_ret_outsample_manual = "{:.6}".format(avg_daily_ret_outsample_manual)
    std_daily_ret_outsample_manual = "{:.6}".format(std_daily_ret_outsample_manual)

    print("Manual Strategy data out sample")
    print("avg daily return outsample: " + avg_daily_ret_outsample_manual)
    print("std daily return outsample: " + std_daily_ret_outsample_manual)
    print("cumulative return outsample: " + cum_ret_outsample_manual)

    # data = {'cumulative return insample': [cum_ret_insample_manual], 'avg daily return insample': [avg_daily_ret_insample_manual], 'std daily return insample': [std_daily_ret_insample_manual],
    #         'cumulative return outsample': [cum_ret_outsample_manual], 'avg daily return outsample': [avg_daily_ret_outsample_manual], 'std daily return outsample': [std_daily_ret_outsample_manual]}
    # metrics_df = pd.DataFrame(data)
    # metrics_df.to_html('p6_results.html')

    if isinstance(insample_portvals_benchmark, pd.DataFrame) and isinstance(outsample_portvals_benchmark, pd.DataFrame):
        insample_portvals_benchmark = insample_portvals_benchmark[insample_portvals_benchmark.columns[0]]  # just get the first column
        outsample_portvals_benchmark = outsample_portvals_benchmark[outsample_portvals_benchmark.columns[0]]  # just get the first column
    else:
        raise Exception("warning, code did not return a DataFrame")

    daily_ret_insample_benchmark = (insample_portvals_benchmark / insample_portvals_benchmark.shift(1)) - 1
    cum_ret_insample_benchmark = (insample_portvals_benchmark[-1] / insample_portvals_benchmark[0]) - 1
    avg_daily_ret_insample_benchmark = daily_ret_insample_benchmark.mean()
    std_daily_ret_insample_benchmark = daily_ret_insample_benchmark.std()

    cum_ret_insample_benchmark = "{:.6}".format(cum_ret_insample_benchmark)
    avg_daily_ret_insample_benchmark = "{:.6}".format(avg_daily_ret_insample_benchmark)
    std_daily_ret_insample_benchmark = "{:.6}".format(std_daily_ret_insample_benchmark)

    print("Benchmark data in sample")
    print("avg daily return insample: " + avg_daily_ret_insample_benchmark)
    print("std daily return in sample: " + std_daily_ret_insample_benchmark)
    print("cumulative return in sample: " + cum_ret_insample_benchmark)

    daily_ret_outsample_benchmark = (outsample_portvals_benchmark / outsample_portvals_benchmark.shift(1)) - 1
    cum_ret_outsample_benchmark = (outsample_portvals_benchmark[-1] / outsample_portvals_benchmark[0]) - 1
    avg_daily_ret_outsample_benchmark = daily_ret_outsample_benchmark.mean()
    std_daily_ret_outsample_benchmark = daily_ret_outsample_benchmark.std()

    cum_ret_outsample_benchmark = "{:.6}".format(cum_ret_outsample_benchmark)
    avg_daily_ret_outsample_benchmark = "{:.6}".format(avg_daily_ret_outsample_benchmark)
    std_daily_ret_outsample_benchmark = "{:.6}".format(std_daily_ret_outsample_benchmark)

    print("Benchmark data outsample")
    print("avg daily return outsample: " + avg_daily_ret_outsample_benchmark)
    print("std daily return out sample: " + std_daily_ret_outsample_benchmark)
    print("cumulative return outsample: " + cum_ret_outsample_benchmark)


def generate_insample_manual_benchmark_graph(manual_trades_df, port_vals_normalized, port_vals_benchmark_normalized):
    df_temp = pd.concat([port_vals_normalized, port_vals_benchmark_normalized],
                        keys=['Manual Strategy Normalized', 'Benchmark Normalized'], axis=1)
    ax = df_temp.plot(kind='line', y='Manual Strategy Normalized', color='red')
    df_temp.plot(kind='line', y='Benchmark Normalized', color='purple', ax=ax)
    for day, date in enumerate(manual_trades_df.index):
        #short
        if  manual_trades_df.loc[date]['Trades'] < 0:
            plt.axvline(x = date, color = 'black', label = 'axvline-full height')
        elif manual_trades_df.loc[date]['Trades'] > 0:#long
            plt.axvline(x=date, color='blue', label='axvline-full height')

    plt.title("In sample Manual Normalized vs Benchmark Normalized")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Values")
    plt.legend(['Manual', 'Benchmark', 'Long', 'Short'])
    plt.savefig('images/Figure1.png')
    #plt.show()
    plt.close()


def generate_outsample_manual_benchmark_graph(manual_trades_df, port_vals_normalized, port_vals_benchmark_normalized):
    df_temp = pd.concat([port_vals_normalized, port_vals_benchmark_normalized],
                        keys=['Manual Strategy Normalized', 'Benchmark Normalized'], axis=1)
    ax = df_temp.plot(kind='line', y='Manual Strategy Normalized', color='red')
    df_temp.plot(kind='line', y='Benchmark Normalized', color='purple', ax=ax)
    for day, date in enumerate(manual_trades_df.index):
        #short
        if manual_trades_df.loc[date]['Trades'] < 0:
            plt.axvline(x = date, color = 'black', label = 'axvline-full height')
        elif manual_trades_df.loc[date]['Trades'] > 0:#long
            plt.axvline(x=date, color='blue', label='axvline-full height')
    plt.title("Out Sample Manual Normalized vs Benchmark Normalized")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Values")
    plt.legend(['Manual', 'Benchmark'])
    plt.savefig('images/Figure2.png')
    #plt.show()
    plt.close()


def inSample_Manual_Benchmark():
    manual_learner = man_strat.ManualStrategy(verbose=False, impact=0.005, commission=9.95)
    manual_trades_df = manual_learner.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31),
                                            sv=100000)
    portvals = ms.compute_portvals(manual_trades_df, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                   endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95, impact=0.005)
    port_vals_normalized = portvals / portvals[0]

    benchMarkTrades_DF = manual_learner.benchMark(symbol=["JPM"], sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
    port_vals_benchmark = ms.compute_portvals(benchMarkTrades_DF, symbols=["JPM"], startDate=dt.datetime(2008, 1, 1),
                                              endDate=dt.datetime(2009, 12, 31), start_val=100000, commission=9.95,
                                              impact=0.005)

    port_vals_benchmark_normalized = port_vals_benchmark / port_vals_benchmark[0]


    generate_insample_manual_benchmark_graph(manual_trades_df, port_vals_normalized, port_vals_benchmark_normalized)

    return portvals, port_vals_benchmark


def outSample_Manual_Benchmark():
    manual_learner = man_strat.ManualStrategy(verbose=False, impact=0.005, commission=9.95)
    manual_trades_df = manual_learner.testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31),
                                            sv=100000)
    portvals = ms.compute_portvals(manual_trades_df, symbols=["JPM"], startDate=dt.datetime(2010, 1, 1),
                                   endDate=dt.datetime(2011, 12, 31), start_val=100000, commission=9.95, impact=0.005)
    port_vals_normalized = portvals / portvals[0]

    benchMarkTrades_DF = manual_learner.benchMark(symbol=["JPM"], sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31))
    port_vals_benchmark = ms.compute_portvals(benchMarkTrades_DF, symbols=["JPM"], startDate=dt.datetime(2010, 1, 1),
                                              endDate=dt.datetime(2011, 12, 31), start_val=100000, commission=9.95,
                                              impact=0.005)

    port_vals_benchmark_normalized = port_vals_benchmark / port_vals_benchmark[0]

    # generate chart
    generate_outsample_manual_benchmark_graph(manual_trades_df, port_vals_normalized, port_vals_benchmark_normalized)

    return portvals, port_vals_benchmark


if __name__ == "__main__":
    print("Entry point to project")
    insample_portvals_manual, insample_portvals_benchmark = inSample_Manual_Benchmark()
    outsample_portvals_manual, outsample_portvals_benchmark = outSample_Manual_Benchmark()
    printManualAndBenchmarkPerfMetrics(insample_portvals_manual.to_frame(), insample_portvals_benchmark.to_frame(), outsample_portvals_manual.to_frame(), outsample_portvals_benchmark.to_frame())
    exp1.run()
    exp2.run()
