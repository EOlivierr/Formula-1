import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.graph_objects as px
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

#Driver plots

#Nationality plot
driver_country = driversdf.groupby('nationality').driver_name.nunique().reset_index() 
driver_country = driver_country.rename(columns = {'driver_name': 'driver_counts'})
driver_country1 = driver_country[driver_country.driver_counts >= 30].sort_values('driver_counts' ,ascending = False )
driver_country1.loc[len(driver_country1.index)] = ['Others', (driver_country.driver_counts.sum() - driver_country1.driver_counts.sum())]

labels = driver_country1['nationality']
values = driver_country1['driver_counts']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, pull=[0, 0, 0, 0, 0, 0, 0.2], hoverinfo='label+value')])
fig.update_layout(title='Verdeling van nationaliteit per seizoen', template = "plotly_dark")
st.plotly_chart(fig)

#Punten van de driver plot
drivers = driver_analysis_df[['year','driver_name', 'points_sum']]
#drivers = drivers.sort_values(by='points_sum', ascending=False)
drivers1 = drivers[drivers['year']==2021]

fig1 = st.bar_chart(drivers1, y='points_sum', x=('driver_name'))

#fig1.update_layout(title='Aantal punten vd Coureurs per Seizoen',
                   #xaxis_title='Team',
                   #yaxis_title='Punten',
                   #template = "plotly_dark")
#st.plotly_chart(fig1)

#Correlatie tussen p1 en pole
scat_df = merged_df[['raceId', 'year','driver_name', 'constructors_name', 'grid', 'position', 'circuit_name']]
scat_df = scat_df[scat_df.year == 2021]
#scat_df = scat_df[scat_df.constructors_name == 'Williams']
#scat_df = scat_df[scat_df.driver_name == 'Nicholas Latifi']
scat_df = scat_df[scat_df.position != r'\N']
scat_df = scat_df.sort_values(by= ['position', 'grid'], ascending = [True, True]).head(500)

#with st.echo(code_location='below'):
    #import plotly.express as px

fig = px.scatter(scat_df, x="grid", y="position")
    
fig.update_layout(title='Correlatie tussen Qualificatie positie en eindpositie',
                   xaxis_title='Qualificatie positie',
                   yaxis_title='Eindpositie',
                   template = "plotly_dark")
    

st.write(fig)


