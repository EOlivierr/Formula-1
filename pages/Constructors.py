import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import plotly.figure_factory as ff
st.set_page_config(layout="wide")

circuits= pd.read_csv('circuits.csv')
constructor_results= pd.read_csv('constructor_results.csv')
constructor_standings= pd.read_csv('constructor_standings.csv')
constructors= pd.read_csv('constructors.csv')
driver_standings= pd.read_csv('driver_standings.csv')
drivers= pd.read_csv('drivers.csv')
lap_times= pd.read_csv('lap_times.csv')
pit_stops= pd.read_csv('pit_stops.csv')
qualifying= pd.read_csv('qualifying.csv')
races= pd.read_csv('races.csv')
results= pd.read_csv('results.csv')
seasons= pd.read_csv('seasons.csv')
sprint_results= pd.read_csv('sprint_results.csv')
status= pd.read_csv('status.csv')

racesdf = races.copy()
racesdf = racesdf.drop(columns = ['url',
       'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time',
       'quali_date', 'quali_time', 'sprint_date', 'sprint_time', 'time'])
racesdf = racesdf.rename(columns ={'name':'race_name'})

circuitsdf = circuits.copy()
circuitsdf = circuitsdf.drop(columns = ['alt', 'url'])
circuitsdf = circuitsdf.rename(columns={'name':'circuit_name', 'location':'city'})

results_copy_df = results.copy()

driversdf = drivers.copy()
driversdf =driversdf.drop(columns =['driverRef', 'number', 'code', 'url'])
driversdf['driver_name'] = driversdf['forename'] + ' ' + driversdf['surname']
driversdf = driversdf.drop(columns =['forename', 'surname'])

constructorsdf =constructors.copy()
constructorsdf =constructorsdf.drop(columns = ['url','constructorRef'])
constructorsdf =constructorsdf.rename(columns = {'name':'constructors_name'})

fastestlapdf = racesdf.merge(circuitsdf , on = 'circuitId')
fastestlapdf = fastestlapdf.merge(results_copy_df, on = 'raceId')

merged_df = results.merge(status , on = 'statusId')
merged_df = merged_df.merge(racesdf, on = 'raceId')
merged_df = merged_df.merge(driversdf, on = 'driverId')
merged_df = merged_df.merge(constructorsdf, on = 'constructorId')
merged_df = merged_df.merge(circuitsdf , on = 'circuitId')

merged_df = merged_df.rename(columns= {'nationality_x':'driver_nationality','nationality_y':'constructor_nationality'})

driver_analysis_df = merged_df.groupby(['year','driver_name']).agg({'points': ['sum'],'raceId':['count'], 'positionOrder':['mean','std'] }).reset_index()

driver_analysis_df.columns = ['_'.join(col).strip() for col in driver_analysis_df.columns.values]
driver_analysis_df = driver_analysis_df.rename( columns = {'year_':'year', 'driver_name_' : 'driver_name'})

champion_df= driver_analysis_df.groupby(['year', 'driver_name']).agg({'points_sum':sum}).reset_index()

champion_df = champion_df.sort_values(['year','points_sum'], ascending = False).groupby('year').head(1)

champion_df = champion_df.drop(3155)

most_races = merged_df.groupby('driver_name')[['raceId']].count().reset_index()
most_races = most_races.sort_values('raceId', ascending= False).head(10)
most_races = most_races.rename(columns ={'raceId': 'total_races'})

con_analysis_df = merged_df.groupby(['year','constructors_name']).agg({'points': ['sum'],'raceId':['count'],'positionOrder':['mean','std'] }).reset_index()
con_analysis_df.columns = ['_'.join(col).strip() for col in con_analysis_df.columns.values]

condf= con_analysis_df[['year_','constructors_name_', 'points_sum']].tail(10)
condf= condf.sort_values(by='points_sum', ascending=False)

#constructor punten per seizoen
st.write("Aantal punten per seizoen")
condf= con_analysis_df[['year_','constructors_name_', 'points_sum']].tail(10)
condf= condf.sort_values(by='points_sum', ascending=False)
fig = st.bar_chart(condf, y='points_sum', x='constructors_name_')

#meest succesvolle constructor
st.write("Meest succesvolle constructeur")
condf1= con_analysis_df[['year_','constructors_name_', 'points_sum']]
condf1 = condf1[condf1['points_sum']>= 70]
condf1= condf1.sort_values(by='points_sum', ascending=False)
fig = st.bar_chart(condf1, y='points_sum', x='constructors_name_')

#regplot voor een constructor

condf2 = condf1[condf1.constructors_name_ == 'Ferrari']
condf2 = condf2.drop(1085)
condf2.sort_values(by='year_', ascending=True)


fig = px.scatter(x=condf2["year_"], 
                 y=condf2["points_sum"],
                 trendline="ols", 
                 trendline_scope="overall", 
                 trendline_color_override="black",)

fig.update_layout(
       xaxis_title="Seizoen",
       yaxis_title="Aantal punten")
st.plotly_chart(fig)


