# ETL Weather Forecast

Weather Forecast DAG
This is an Airflow DAG (Directed Acyclic Graph) that retrieves and stores weather forecast data for the city of Berlin from different weather APIs (Application Programming Interfaces).

![image](https://github.com/kevinbullock89/etl_weather_forecast/blob/master/Weather_DAG.PNG)

## Prerequisites:
- Linux Server
- Python 3.7 or higher
- Airflow 2.1.4 or higher
- MySQL database
- Docker to run Airflow.
- Rapid API Key (https://rapidapi.com/hub)
- Visual Studio Code with the Remote Explorer extension installed on your local machine.

## Installation

To install this project, it is recommended to use a Linux server in the cloud. Once you have a server set up, you can connect to it using VS Code with the Remote Explorer extension. This will allow you to edit and run the code directly on the server, which can be faster and more efficient than working on a local machine.

### Rapid API

If there is no login at Rapid API yet, this can be registered here: https://rapidapi.com/auth/sign-up?referral=/hub. 

Subscriptions to the following API are required:

- wettercom:               https://rapidapi.com/wettercom-wettercom-default/api/forecast9
- Weatherbit:              https://rapidapi.com/weatherbit/api/weather
- Visual Crossing Weather: https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather

here you can find the API Key: https://docs.rapidapi.com/docs/keys. This key must be stored in the python file rapidapi.key

### Connecting to the Server with Visual Studio Code

1. Open Visual Studio Code on your local machine.
2. Click on the "Remote Explorer" icon on the left-hand side of the window.
3. Click on the "+" button to add a new SSH connection.
4. Enter the connection details for your Linux server (hostname/IP address, username, and password or private key).
5. Once connected, you can browse and edit the files on your Linux server as if they were on your local machine.

### Install Airflow using Docker

- To install Docker on Linux use the official Docker instruction: https://docs.docker.com/engine/install/ubuntu/
- Install Airflow using Docker Compose by following the instructions https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

### Cloning the repository
To clone this repository, open your terminal and navigate to the directory where you want to store the project. Then, run the following command:

```sh
git clone https://github.com/kevinbullock89/etl_weather_forecast.git
```
### MySQL database

It is assumed that there is already a MySQL database. It must be ensured that Airflow has the ability to access the MySQL database. 

### Create a connection in Airflow to your MySQL database. 

You can do this through the Airflow UI by navigating to Admin > Connections and clicking the Create button. Enter the following details:

- Conn Id: Azure_MySQL_Weather
- Conn Type: MySQL
- Host: your MySQL server address
- Schema: your MySQL database name
- Login: your MySQL username
- Password: your MySQL password

### Define your RapidAPI key:

To load data from Rapid API you need to create an additional python file named rapidapi.py where the API key is stored. 

```sh
X_RapidAPI_Key = "your_RapidAPI_key"
```

To hide API key in a Python file, it is also possible to use of environment variables.

### Python packages

These Python packages must be installed:

- mysql-connector-python:

```sh
pip install mysql-connector-python
```

- apache-airflow:

```sh
pip install apache-airflow
```

- pandas:
```sh
pip install pandas
```

The PythonOperator is part of the core Airflow package.


## Python Scripts

### weather_dag.py

This file contains the Airflow DAG configuration that defines how the pipeline will be executed. It creates a DAG that runs three times a day and loads weather forecast data from three different APIs into a MySQL database. The DAG contains three tasks that load the data from the APIs into the database.

### weather_forecast.py

This file contains the functions that retrieve weather forecast data from three different APIs: Weatherbit, Wetter.com, and Visual Crossing. Each function extracts the relevant data from the API response and returns it in a standardized format.

### weather_functions.py

This file contains several utility functions that are used by the weather_forecast.py file to process and load data. These functions include a function that loads data into a MySQL database and a function that processes forecast data.


## Usage

To use this repository, simply browse the files and documentation included in the project.

## Contributing

1. Fork this repository to your own account.
2. Create a new branch with your changes: git checkout -b my-feature.
3. Commit your changes: git commit -am 'Add some feature'.
4. Push to the branch: git push origin my-feature.
5. Submit a pull request to this repository.

## License

This project is licensed under the MIT License.

