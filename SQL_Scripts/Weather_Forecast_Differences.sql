SELECT wf.Forecast_Date
	,wf.AVG_Temperature AS 'Forecast_Temperature'
	,wat.AVG_Temperature AS 'Actual_Temperature'
	,wf.AVG_Temperature - wat.AVG_Temperature AS 'Temperature_Difference'
	,wf.Source
	,wf.City
	,wf.Ingest_Timestamp
FROM weather.weather_forecast wf
LEFT JOIN weather.weather_avg_temperature wat ON wf.Forecast_Date = wat.Forecast_Date
	AND wf.City = wat.City
ORDER BY wf.City
	,wf.Source
	,wf.Forecast_Date
	,wf.Ingest_Timestamp