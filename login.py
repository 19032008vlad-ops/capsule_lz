import os
from datetime import datetime
from functools import wraps
import pandas as pd


def loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_file = 'logs.csv'
        file_check = os.path.isfile(log_file)
        
        
        if file_check and os.path.getsize(log_file) > 0:
            current_id = len(pd.read_csv(log_file, sep=';'))
        else:
            current_id = 0

        now = datetime.now()
        info = {
            'Username': os.getlogin(),
            'Function_name': func.__name__,
            'Date': now.strftime('%d.%m.%Y'),  
            'Time': now.strftime('%H:%M:%S')
        }

        try:
         df = pd.DataFrame([info], index=[current_id])
         df.to_csv(
            log_file, 
            mode="a", 
            index_label='id', 
            header=not file_check or os.path.getsize(log_file) == 0, 
            sep=';', 
            encoding='UTF-8'
          )

        except Exception as e:
            print(f"Error login: {e}")

        return func(*args, **kwargs)
    
    return wrapper