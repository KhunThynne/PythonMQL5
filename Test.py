from datetime import datetime
import sys

from matplotlib import pyplot as plt

# from MQL_Five import initailize,send_
# from Indicators.MACD import Display
from trading_technical_indicators.tti.indicators import MovingAverageConvergenceDivergence

import pandas as pd
from MQL_Five import initailize


#Initailize
mt5 = initailize.initial_login()


#Dataset
EUR = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 50)
EUR = pd.DataFrame(EUR)
EUR['date'] = pd.to_datetime(EUR['time'], unit='s')
EUR.set_index('date', inplace=True)
EUR['time'] = EUR.index.strftime('%H:%M:%S')

# file_path = 'sample_data.csv'
# df = pd.read_csv(file_path, parse_dates=True, index_col=0)

# แสดงข้อมูลใน DataFrame

Test = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 1)
print(Test)
MACD = MovingAverageConvergenceDivergence(input_data=EUR)


MACD_ = MACD._calculateTi()
MACD_ = MACD_.dropna()

def Grapt():
    plt.figure(figsize=(12, 6))
    plt.plot(MACD_.index, MACD_['macd'], label='MACD', color='blue')
    plt.plot(MACD_.index, MACD_['signal_line'], label='Signal Line', color='red')
    plt.legend(loc='upper left')
    plt.title('MACD and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

D  = MACD.getTiGraph()
D.show()