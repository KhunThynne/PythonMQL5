# import sys
import os
from MQL_Five.__config import mt5,json
from time import sleep
path = os.path.join(os.getcwd(), 'MQL_Five', 'user.json')

mt5 = mt5
def initial_login():
    global account
    Login = False
    try:
        while not Login:
            
            with open(path) as f:
                account = json.load(f)
            if not mt5.initialize(login=account["login"], server=account['server'],password=account['password']):
                print("\n Authorization fail \n\ninitialize() failed, error code =",mt5.last_error())
                print(f"Something wrong can't login plece check user.json\n User : {account["login"]} \n Server : {account['server']} \n {account['password']} ")
                sleep(5)
                os.system('cls')
            else:
                print("\n Success Authorization \n")
                Login = True
                return mt5
    except KeyboardInterrupt as e:
        print(e)
        mt5.shutdown()
        quit()
                    

