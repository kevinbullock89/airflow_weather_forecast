import weather_functions
import requests
import rapidapi

# RapidAPI
X_RapidAPI_Key = rapidapi.Key # here is the Rapid API Key


class ForecastData:

    def process_weatherbit():

        # Weatherbit API informations
        X_RapidAPI_Host = "weatherbit-v1-mashape.p.rapidapi.com"
        data_key = 'data'
        datetime_col = 'datetime'
        app_max_temp_col = 'app_max_temp'
        app_min_temp_col = 'app_min_temp'
        fileformat = 'json'
        datasource = 'weatherbit'

        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"

        querystring = {"lat":weather_functions.longitude,"lon":weather_functions.latitude}

        headers = {
            "X-RapidAPI-Key": X_RapidAPI_Key,
            "X-RapidAPI-Host": X_RapidAPI_Host
        }

        response = requests.request("GET", url, headers=headers, params=querystring)


        return weather_functions.process_forecast_data(response,data_key,datetime_col,app_max_temp_col,app_min_temp_col, datasource, fileformat)

    def process_wettercom():
	
        # Weatherbit API informations
        X_RapidAPI_Host = "forecast9.p.rapidapi.com"
        data_key = 'forecast'
        datetime_col = 'date'
        app_max_temp_col = 'temperature.max'
        app_min_temp_col = 'temperature.min'
        datasource = 'wetter.com'
        fileformat = 'json'
        record_path = 'items'

        url = f"https://forecast9.p.rapidapi.com/rapidapi/forecast/{weather_functions.City}/summary/"

        headers = {
            "X-RapidAPI-Key": X_RapidAPI_Key,
            "X-RapidAPI-Host": X_RapidAPI_Host
        }

        response = requests.request("GET", url, headers=headers)

        return weather_functions.process_forecast_data(response,data_key,datetime_col,app_max_temp_col,app_min_temp_col, datasource, fileformat, record_path)
    
    def process_visualcrosswather():
    
        # RapidAPI
        X_RapidAPI_Host = "visual-crossing-weather.p.rapidapi.com"
        data_key = 'forecast'
        datetime_col = 'Date time'
        app_max_temp_col = 'Maximum Temperature'
        app_min_temp_col = 'Minimum Temperature'
        datasource = 'visual-crossing-weather'
        fileformat = 'csv'

        url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

        querystring = {"aggregateHours":"24","location":"Berlin, Germany","contentType":"csv","unitGroup":"metric","shortColumnNames":"false"}

        headers = {
            "X-RapidAPI-Key": X_RapidAPI_Key,
            "X-RapidAPI-Host": X_RapidAPI_Host
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return weather_functions.process_forecast_data(response,data_key,datetime_col,app_max_temp_col,app_min_temp_col, datasource, fileformat)