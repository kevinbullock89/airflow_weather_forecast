import weather_functions
import weather_forecast
from datetime import datetime, timedelta
from airflow import DAG 
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'kevin',
    'retries': 0,
    'retry_delay': timedelta(minutes=2)

}

dag = DAG(
    dag_id= 'weather_forecast',
    default_args=default_args,
    start_date=datetime(2023,3,8),
    schedule_interval='0 */8 * * *' # the DAG will run three times per day
)



CreateTable = MySqlOperator(
    task_id = 'create_postgres_table',
    mysql_conn_id = 'Azure_MySQL_Weather',
    sql = '''
        CREATE TABLE IF NOT EXISTS `weather_forecast` (
        `Forecast_Date` date NOT NULL,
        `AVG_Temperature` int(11) DEFAULT NULL,
        `Source` varchar(25) COLLATE utf8_bin NOT NULL,
        `Ingest_Timestamp` datetime NOT NULL,
        `City` varchar(25) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`Forecast_Date`,`Source`,`Ingest_Timestamp`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''
)

LoadDataWeatherbit = PythonOperator(
    task_id='load_data_to_mysql_weatherbit',
    python_callable=weather_functions.load_data_to_mysql,
    op_kwargs={
        'name': 'weather_forecast',
        'con': 'Azure_MySQL_Weather',
        'if_exists': 'append',
        'index': False,
        'func': weather_forecast.ForecastData.process_weatherbit
    },
    provide_context=True,
    dag=dag,
)

LoadDataWetter_com = PythonOperator(
    task_id='load_data_to_mysql_wetter_com',
    python_callable=weather_functions.load_data_to_mysql,
    op_kwargs={
        'name': 'weather_forecast',
        'con': 'Azure_MySQL_Weather',
        'if_exists': 'append',
        'index': False,
        'func': weather_forecast.ForecastData.process_wettercom
    },
    provide_context=True,
    dag=dag,
)

LoadVisualCrossing = PythonOperator(
    task_id='load_data_to_mysql_visualcrosswather',
    python_callable=weather_functions.load_data_to_mysql,
    op_kwargs={
        'name': 'weather_forecast',
        'con': 'Azure_MySQL_Weather',
        'if_exists': 'append',
        'index': False,
        'func': weather_forecast.ForecastData.process_visualcrosswather
    },
    provide_context=True,
    dag=dag,
)


# Run DAG
CreateTable >> LoadDataWeatherbit  >> LoadVisualCrossing >> LoadDataWetter_com
