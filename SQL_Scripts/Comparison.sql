SELECT sum(wf.AVG_Temperature) - sum(wat.AVG_Temperature) AS 'Temperature_Difference'
	,wf.Source
	,wf.City
FROM weather.weather_forecast wf
LEFT JOIN weather.weather_avg_temperature wat ON wf.Forecast_Date = wat.Forecast_Date
	AND wf.City = wat.City
GROUP BY wf.Source
	,wf.City