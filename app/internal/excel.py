import pandas as pd
import base64
import io
import os

pandas_function_mapping = {
}

def register(func):
    name:str = func.__name__
    name = name.replace('to_', '')
    
    pandas_function_mapping[name] = func
    print(pandas_function_mapping)
    return func

@register
def to_json(df: pd.DataFrame):
    return df.to_dict(orient='records')

@register
def to_csv(df: pd.DataFrame):
    return df.to_csv()

@register
def to_html(df: pd.DataFrame):    
    return df.to_html()

def base64_to_excel(data:str):
    return pd.read_excel(data)

def read_excel_from_base64(base64_data):
    decoded_bites = base64.b64decode(base64_data)
    decoded_buffer = io.BytesIO(decoded_bites)
    return base64_to_excel(data=decoded_buffer)

def convert_file_to(type:str, data:str):
    try:    
        if not data:    
            current_dir = os.path.dirname(__file__)
            test_file_path = os.path.join(current_dir, 'text.txt')
            file = open(test_file_path, 'r') 
            data = file.read()  
        excel_data = read_excel_from_base64(base64_data=data) 
        return pandas_function_mapping[type](excel_data)
    except Exception as e:
        print("Error While Converting File >>> ", str(e))
        return e
