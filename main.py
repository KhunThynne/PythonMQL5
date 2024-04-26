from datetime import datetime
import sys
from matplotlib import pyplot as plt
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



# Test = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 1)
# print(Test)
MACD = MovingAverageConvergenceDivergence(input_data=EUR)

G = MACD.getTiGraph()
MACD = MACD._calculateTi()
# MACD = MACD.getTiGraph()
MACD= MACD.dropna()

print(MACD)

G.show()