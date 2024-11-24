import pandas as pd
import base64
import io

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
    return pd.read_excel(data, keep_default_na=False)

def read_excel_from_base64(base64_data):
    decoded_bites = base64.b64decode(base64_data)
    decoded_buffer = io.BytesIO(decoded_bites)
    return base64_to_excel(data=decoded_buffer)

def convert_file_to(type:str, data:str):
    try:    
        if not data:    
            raise Exception('No Data')
        excel_data = read_excel_from_base64(base64_data=data) 
        return pandas_function_mapping[type](excel_data)
    except Exception as e:
        print("Error While Converting File >>> ", str(e))
        return e
    
def convert_file_to_json(data:str):
    try:
        if not data:
            raise Exception('No Data')
        excel = read_excel_from_base64(base64_data=data)
        print(excel)
        return excel.to_dict(orient="records")
    except Exception as e:
        print("Error in convert to json", str(e))
        return e
    
def convert_file_to_csv(data:str):
    try:
        if not data:
            raise Exception('No Data')
        excel = read_excel_from_base64(base64_data=data)
        return to_csv(excel)
    except Exception as e:
        print("Error in convert to json", str(e))
        return e
def convert_file_to_html(data:str):
    try:
        if not data:
            raise Exception('No Data')
        excel = read_excel_from_base64(base64_data=data)
        return to_html(excel)
    except Exception as e:
        print("Error in convert to json", str(e))
        return e
