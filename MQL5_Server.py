import json
from time import sleep
import importlib

while True:
    try:
        # Explicitly reload the module on each iteration
      
        # importlib.invalidate_caches()
        # import data
        # importlib.reload(data)
        
        # DD = data.DD
        f = open('MQL_Five/user.json')
    
        j = json.load(f)
        print(j['login'])
     
        # if hasattr(data, 'test'):
            
        #     print(f"TEST: {str(data.test)}")
        # else:
        #     print(DD)
    except AttributeError:
        print("Error:  not found in 'data' module")
    except Exception as e:
        print(f"Error: {str(e)}")
        continue  # Continue the loop despite errors
    finally:
        sleep(1)
