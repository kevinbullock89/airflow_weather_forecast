import requests
import json
import pandas as pd
import io
from datetime import date, datetime
from airflow.providers.mysql.hooks.mysql import MySqlHook

# City
City = "Berlin"
longitude = "52.520008"
latitude = "13.404954"


def process_forecast_data(response, data_key, datetime_col, app_max_temp_col, app_min_temp_col, datasource, fileformat, record_path=None):

    if fileformat == 'json':
        data = response.json()
        df = pd.json_normalize(data[data_key], record_path=record_path)
    elif fileformat == 'csv':
        df = pd.read_csv(io.StringIO(response.text))

    # filter only necessary columns and save in a dataframe
    forecast_data = df.filter(items=[datetime_col, app_max_temp_col, app_min_temp_col])

    forecast_data['AVG_Temperature'] = forecast_data[app_max_temp_col] - forecast_data[app_min_temp_col]
    # add Datasource to the Dataframe
    forecast_data['Source'] = datasource
    # add Current Date to the Dataframe
    forecast_data['Ingest_Timestamp'] = datetime.now()
    # add City to the Dataframe
    forecast_data['City'] = City    
    # Rename date 
    forecast_data.rename(columns={datetime_col : 'Forecast_Date'}, inplace=True)
    # removal of unnecessary columns
    forecast_data.drop(columns=[app_max_temp_col, app_min_temp_col], inplace=True)
    #change date format to YYYY-MM-DD
    forecast_data['Forecast_Date'] = pd.to_datetime(forecast_data['Forecast_Date'], errors='coerce')

    return forecast_data

def load_data_to_mysql(ds, func, **kwargs):
    # Retrieve the data from the process_weather_data function
    df = func()

    # Create a connection to the MySQL database
    hook = MySqlHook(mysql_conn_id='Azure_MySQL_Weather')
    engine = hook.get_sqlalchemy_engine()

    # Use pandas to load the data into the MySQL database
    table_name = 'weather_forecast'
    df.to_sql(name=table_name, con=engine, if_exists='append', index = False)