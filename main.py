from datetime import datetime,timedelta
import json
import os
import sys
from matplotlib import pyplot as plt
from trading_technical_indicators.tti.indicators import MovingAverageConvergenceDivergence
import pandas as pd
from MQL_Five import initailize
from MQL_Five.send_ import Order
from time import sleep
from IPython.display import display, HTML
#Initailize
mt5 = initailize.initial_login()
symbol = "EURUSD"
#Dataset
buy_sell = dataset = pd.DataFrame()

date_time = datetime.now().strftime("%Y%m%d")
# G.show()
# request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": 0.1,
#         "type": mt5.ORDER_TYPE_BUY,
#         "price": price,
#         "sl": price - 100 * point,
#         "tp": price + 100 * point,
#         "deviation": deviation,
#         "magic": 234000,
#         "comment": "python script open",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_RETURN,
#     }

Trade_signal = Order(symbol,mt5,{"Thynne":"Hello word"})
# Trade_signal.request()


class ExportsDataset():
    def __init__(self,name,dataset) -> None:
        global MACD_return,result_Data,values
        self.name = name
        self.dataset = dataset
        self.initial()
        
    def initial(self)->None:
        indicators = ['macd']
        for indicator in indicators:
            os.makedirs(f"./dataset/indicators/{indicator}", exist_ok=True)
                  
    def createDirectory(self) -> None:
        export_ =  dataset.to_json(orient="index")
        path = "./dataset/buy_sell"
        if not os.path.exists(path):
            os.mkdir(path)
            print("Folder %s created!" % path)
        else:
            print("Folder %s already exists" % path)
        
    def exportfile(self) -> None:
        export_ =  dataset.to_json(orient="index")
        with open(f'dataset/Dataset_{date_time}.json', 'w') as f:
            f.write(export_)


def Dataset_(): 
    global dataset,MACD_return,result_Data,values
    values = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 1000)
    values = pd.DataFrame(values)
    values['date'] = pd.to_datetime(values['time'], unit='s')
    values.set_index('date', inplace=True)
    values['time'] = values.index.strftime('%H:%M:%S')
    # Test = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 1)
    # print(Test)
    MACD = MovingAverageConvergenceDivergence(input_data=values)

       # G = MACD.getTiGraph()
    MACD_return = MACD._calculateTi()
    
    # MACD = MACD.getTiGraph()
    
    # reult_Data= reult_Data.dropna()

    # print(MACD.index[-1])
    # new_data = values.iloc[-1]._append(reult_Data.iloc[-1])
    # result_Data= values.join(MACD_return)

    # แสดงผล combined_data
    # print(result_Data)
    
def Test():
    global MACD_return,result_Data,values
    print(values)

     
Dataset_()

def main():
    global dataset
    ### Ckeak symbol can subscribe
    if not mt5.symbol_select(symbol, True):
        print(f"Failed to subscribe to {symbol}, error code =", mt5.last_error())
        mt5.shutdown()
        quit()
    try:
        set_data = {"old":0,"new":0}
        while True:
            # Request the last tick data
            tick = mt5.symbol_info_tick(symbol)#Get tick event
            if tick:
                # timestamp_millis = tick.time_msc
                # timestamp_seconds = timestamp_millis / 1000
                # date_time_utc = datetime.fromtimestamp(timestamp_seconds)
                # date_time_thailand = date_time_utc + timedelta(hours=7)
                data = Dataset_()
                New = data['data']
                if(set_data['old'] != set_data['new'] ):
                    set_data['old']=  set_data['new']
                    print(f"Time {set_data['new']}")
                    dataset = dataset._append(New)
                    display(dataset)
                else:
                    tick_time = data['date']
                    set_data['new'] = tick_time
            sleep(1)   
    except KeyboardInterrupt as e:
        dataset.drop_duplicates(inplace=True)
        export_ =  dataset.to_json(orient="index")
        ExportsDataset('data',dataset)
        print("Script interrupted by user.")
    except AttributeError as e:
        print(f"Error:  {e}")
    # Shutdown MT5 connection

    mt5.shutdown()


# main()