#Climate-Analysis

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. The purpose behind the project is to be able to use the API to plan around weather. SQLAlchemy was used within Python to store, inspect, and manipulate the data, while Pandas, Numpy, and Matplotlib was used within Python to visualize the data in a Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data while Python with Flask powered the developement of the web interface.

## Questions

1. How much total precipitation did Hawaii recieve in the last 12 months?
2. What were the most active weather stations during those 12 months?
3. What were the observaions of the most active weather stations, described using sumamry statistics?

## Tasks

### Climate Analysis

1. Use SQLAlchemy to connect to SQLite database.
2. Automap the database, and reflect the tables into classes.
3. Query and plot precipitation and weather station data.
4. Calculate summary statistics for the precipitation and weather station data. 


### Climate API

1. Connect to the SQLite database.
2. Automap the database, and reflect the tables into classes.
3. Define paths for:
	*API home screen
	*Precipitation information
	*Weather station information
	*Temperature informature
	*Dynamic routes that take in a start or end date

