Hawaii-Climate-Analysis

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. The purpose behind the project is to be able to use the API to plan around weather. SQLAlchemy was used within Python to store, inspect, and manipulate the data, while Pandas, Numpy, and Matplotlib was used within Python to visualize the data in a Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data while Python with Flask powered the developement of the web interface.

Questions

Climate Analysis
Precipitation Analysis
How much total precipitation did Hawaii receive during the last twelve months on record?
What are the summary statistics for that precipitation data?
Weather Station Analysis
What are the most active weather stations based on observation count?
What are the maximum, minimum, and average temperatures for the most active weather station?
Temperature Analysis
For the most active weather station, what are the most frequent temperature observations for the last twelve months on record?
Are the monthly averages of the recorded June and December temperature observations statistically significant?
Historical Analysis
Given a set of start and end dates, what are the maximum, minimum, and average temperatures for the same date range one year prior?
Given a set of start and end dates, what is the total precipitation for each weather station for the same date range one year prior?
Given a set of start and end dates, what are the daily maximum, minimum, and average temperatures for the same date range for all years on record?