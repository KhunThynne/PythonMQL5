# prepare the buy request structure

import time

import pandas as pd
from MQL_Five.__config import mt5
from MQL_Five import initailize
# initailize.initial_login()
class Order():
    def __init__(self,symbol,mt5,request_object) -> None:
        self.symbol = symbol
        self.mt5 = mt5
        pass
    def request(self):
        account_info=self.mt5.account_info()
        if account_info!=None:
        # display trading account data 'as is'
            # print(account_info)
            # display trading account data in the form of a dictionary
            print("Show account_info()._asdict():")
            account_info_dict = mt5.account_info()._asdict()
            for prop in account_info_dict:
                print("  {}={}".format(prop, account_info_dict[prop]))
           
    
            # convert the dictionary into DataFrame and print
            df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
            print("account_info() as dataframe:")
           
        else:
            print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())
 
def send_request():
    symbol = "USDJPY"
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()
    
    # if the symbol is unavailable in MarketWatch, add it
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, exit",symbol)
            mt5.shutdown()
            quit()
    
    lot = 0.1
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - 100 * point,
        "tp": price + 100 * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    
    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, \nretcode={}".format(result.retcode))
        # request the result as a dictionary and display it element by element
        # result_dict=result._asdict()
        # for field in result_dict.keys():
        #     print("   {}={}".format(field,result_dict[field]))
        #     # if this is a trading request structure, display it element by element as well
        #     if field=="request":
        #         traderequest_dict=result_dict[field]._asdict()
        #         for tradereq_filed in traderequest_dict:
        #             print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
        print("shutdown() and quit")
        mt5.shutdown()
        quit()
    
    print("2. order_send done, ", result)
    # print("   opened position with POSITION_TICKET={}".format(result.order))
    # print("   sleep 2 seconds before closing position #{}".format(result.order))
    time.sleep(2)
    # # create a close request
    # position_id=result.order
    # price=mt5.symbol_info_tick(symbol).bid
    # deviation=20
    # request={
    #     "action": mt5.TRADE_ACTION_DEAL,
    #     "symbol": symbol,
    #     "volume": lot,
    #     "type": mt5.ORDER_TYPE_SELL,
    #     "position": position_id,
    #     "price": price,
    #     "deviation": deviation,
    #     "magic": 234000,
    #     "comment": "python script close",
    #     "type_time": mt5.ORDER_TIME_GTC,
    #     "type_filling": mt5.ORDER_FILLING_RETURN,
    # }
    # # send a trading request
    # result=mt5.order_send(request)
    # # check the execution result
    # print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
    # if result.retcode != mt5.TRADE_RETCODE_DONE:
    #     print("4. order_send failed, retcode={}".format(result.retcode))
    #     print("   result",result)
    # else:
    #     print("4. position #{} closed, {}".format(position_id,result))
    #     # request the result as a dictionary and display it element by element
    #     result_dict=result._asdict()
    #     for field in result_dict.keys():
    #         print("   {}={}".format(field,result_dict[field]))
    #         # if this is a trading request structure, display it element by element as well
    #         if field=="request":
    #             traderequest_dict=result_dict[field]._asdict()
    #             for tradereq_filed in traderequest_dict:
    #                 print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
    
    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()