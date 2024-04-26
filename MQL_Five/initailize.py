# import sys
import os
from MQL_Five.__config import mt5,json



path = os.path.join(os.getcwd(), 'MQL_Five', 'user.json')

account = {}
mt5 = mt5

with open(path) as f:
    account = json.load(f)


def initial_login():
    if not mt5.initialize(login=account["login"], server=account['server'],password=account['password']):
        print("\n Authorization fail \n\ninitialize() failed, error code =",mt5.last_error())
        mt5.shutdown()
        quit()
    else:
        print("\n Success Authorization \n")
        return mt5
        

