# Surfs Up
## Overview
A company is trying to determine the viability and sustainability of an ice cream shop in Oahu, HI year round.  This analysis willl use one year of temperture data for Oahu and determine the statistics for the months of June and December.

## Setup for Analysis
Using the Python SQL toolkit and Object Relational Mapper we create an engine that connects to the hawaii.sqlite file.  This file contains the informaion about the weather in Hawaii.  There are two tables, measurement and station.  The measurement table is the one we are most interested in for this analysis.  The table consists of the following columns: __tobs, prcp, station, date and id__.  The tobs column provides us with the temperture reading and the prcp column is precipitation.  The station is the weather station where the reading was taken and the date is the day the reading was taken.  

For this analysis we create an empty list to capture the June temps for all the years of the data.  Then query the database on the date and tobs column, extracting just the information for the month of June (6).  Then the list is used to create a DataFrame and from that the dt.describe() function provides the information desired.  This is the code:
<br>
```
# Convert the June temperatures to a list.
june_temps = []
june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==6).all()

# Create a DataFrame from the list of temperatures for the month of June. 
df = pd.DataFrame(june_temps, columns=['date','temperture'])
df.set_index(df['date'], inplace=True)
df = df.sort_index()
df.describe()
```
<br>
We can then refactor the code above and change this as follows for December (12):
<br>
```
# Convert the June temperatures to a list.
dec_temps = []
dec_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).all()

# Create a DataFrame from the list of temperatures for the month of June. 
df = pd.DataFrame(dec_temps, columns=['date','temperture'])
df.set_index(df['date'], inplace=True)
df = df.sort_index()
df.describe()
```
<br>

## Results
The results for the June temperatures are: <br>

The results for the December temperatures are: <br>

