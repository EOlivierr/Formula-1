import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
PAGE_NAME = "Circuits"
st.set_page_config(layout="wide")

col1, col2, col3, col4 = st.columns([1, 3, 1, 1])

image = Image.open('formula-1-logo-5-3.png')

with col4:
       st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

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

#circuits op de kaart 

loc_df = merged_df[['circuit_name', 'year', 'country','lat', 'lng']]
#slider voor map

start_date = min(loc_df['year'])
end_date = max(loc_df['year'])
max_days = end_date-start_date

with st.sidebar:
       slider = st.slider('Select de datum om de Circuits opde kaart te zien!', min_value=start_date ,max_value=end_date)
#value=(start_date,end_date)

#loc_df = loc_df[(loc_df.year >= slider[0]) & (loc_df.year <= slider[1])]
loc_df = loc_df[loc_df['year']== slider]

loc_df['text']= loc_df['circuit_name'] + ', ' + 'Country: ' + loc_df['country'].astype(str)

fig2 = go.Figure(data=go.Scattergeo(
        lon = loc_df['lng'],
        lat = loc_df['lat'],
        text = loc_df['text'],
        mode = 'markers',
        marker_colorscale = "thermal"
        ))

fig2.update_geos(projection_type="orthographic")

fig2.update_layout(
        title = 'Circuits of Formula 1 across the world (Hover for info)',
        height=500,
        width=500,
        margin={"r":0,"t":0,"l":0,"b":0}
    )
with col2:
       st.plotly_chart(fig2)

#top 20 meest voorkomende circuits
#st.write("Top 20 meest voorkomende circuits")
most_circuits = fastestlapdf.groupby(['year','circuit_name']).count().reset_index()

m = most_circuits['circuit_name'].value_counts().reset_index().head(20)
m =  m.rename(columns ={'circuit_name': 'count', 'index': 'circuit_name'})

import plotly.express as px
with col2:
       fig = st.bar_chart(m, x='circuit_name', y='count')

#fig.update_layout(title='Top 20 meest voorkomende circuits in Formule 1',
#                   xaxis_title='Circuits',
#                   yaxis_title='Rondetijden',
#                   template = "plotly_dark")

#fig.show()


#snelste rondetijd per circuit
fastestlapdf['f_lap_1'] = fastestlapdf['fastestLapTime'].apply(lambda x : (x.split('.')[-1]))
fastestlapdf['f_lap_2'] = fastestlapdf['fastestLapTime'].apply(lambda x : (x.split('.')[0]))
fastestlapdf['f_lap_3'] = fastestlapdf['f_lap_2'].apply(lambda x: (x.split(':')[-1]))
fastestlapdf['f_lap_4'] = fastestlapdf['f_lap_2'].apply(lambda x: (x.split(':')[0]))

fastestlapdf['f_lap_1'] = fastestlapdf['f_lap_1'].str.strip()
fastestlapdf['f_lap_3'] = fastestlapdf['f_lap_3'].str.strip()
fastestlapdf['f_lap_4'] = fastestlapdf['f_lap_4'].str.strip()

fastestlapdf['f_lap_1'] = pd.to_numeric(fastestlapdf['f_lap_1'] , errors = 'coerce')
fastestlapdf['f_lap_3'] = pd.to_numeric(fastestlapdf['f_lap_3'] , errors = 'coerce')
fastestlapdf['f_lap_4'] = pd.to_numeric(fastestlapdf['f_lap_4'] , errors = 'coerce')

fastestlapdf['fastest_lap'] = fastestlapdf['f_lap_1'] + fastestlapdf['f_lap_3']*1000 + fastestlapdf['f_lap_4']*60*1000

fastestlapdf = fastestlapdf.drop(columns = ['f_lap_4','f_lap_3', 'f_lap_2','f_lap_1'])

x = fastestlapdf.sort_values('year')

fastestlapdf = fastestlapdf[(fastestlapdf['year'].between(2004,2021, inclusive = 'both'))]

h = fastestlapdf.groupby(['year','circuit_name']).count().reset_index()

lap_time_monza = fastestlapdf[fastestlapdf['circuit_name'] == 'Autodromo Nazionale di Monza']
lap_time_monaco = fastestlapdf[fastestlapdf['circuit_name']== 'Circuit de Monaco']
lap_time_silverstone = fastestlapdf[fastestlapdf['circuit_name']== 'Silverstone Circuit']
lap_time_catalunya = fastestlapdf[fastestlapdf['circuit_name']=='Circuit de Barcelona-Catalunya']
lap_time_hungaroring = fastestlapdf[fastestlapdf['circuit_name']== 'Hungaroring']
lap_time_spa = fastestlapdf[fastestlapdf['circuit_name']== 'Circuit de Spa-Francorchamps']

lap = lap_time_silverstone.groupby('year')[['fastest_lap']].min().reset_index()
lap1 =  lap_time_monaco.groupby('year')[['fastest_lap']].min().reset_index()
lap2 =  lap_time_monza.groupby('year')[['fastest_lap']].min().reset_index()
lap3 = lap_time_catalunya.groupby('year')[['fastest_lap']].min().reset_index()
lap4 = lap_time_hungaroring.groupby('year')[['fastest_lap']].min().reset_index()
lap5 = lap_time_spa.groupby('year')[['fastest_lap']].min().reset_index()

fig3 = go.Figure()

fig3.add_trace(go.Scatter(x=lap.year, y=lap.fastest_lap,
                    mode='lines',
                    name='Silverstone'))
fig3.add_trace(go.Scatter(x=lap1.year, y=lap1.fastest_lap,
                    mode='lines',
                    name='Monaco'))
fig3.add_trace(go.Scatter(x=lap2.year, y=lap2.fastest_lap,
                    mode='lines',
                    name='Monza'))
fig3.add_trace(go.Scatter(x=lap3.year, y=lap3.fastest_lap,
                    mode='lines',
                    name='Catalunya'))
fig3.add_trace(go.Scatter(x=lap4.year, y=lap4.fastest_lap,
                    mode='lines',
                    name='Hungaroring'))
fig3.add_trace(go.Scatter(x=lap5.year, y=lap5.fastest_lap,
                    mode='lines',
                    name='Spa-Francorchamps'))

fig3.update_layout(title='Snelste rondetijden per Circuit per paar',
                   xaxis_title='Jaar',
                   yaxis_title='Rondetijden',
                   template = "plotly_dark")
with col2:
       st.plotly_chart(fig3)

#snelste pitlane
pitstopsdf = pit_stops.merge(races , on = 'raceId')
pitstopsdf = pitstopsdf.merge(circuits, on ="circuitId") 

lap_time_monza = pitstopsdf[pitstopsdf['name_y'] == 'Autodromo Nazionale di Monza']
lap_time_monaco = pitstopsdf[pitstopsdf['name_y']== 'Circuit de Monaco']
lap_time_silverstone = pitstopsdf[pitstopsdf['name_y']== 'Silverstone Circuit']
lap_time_catalunya = pitstopsdf[pitstopsdf['name_y']=='Circuit de Barcelona-Catalunya']
lap_time_hungaroring = pitstopsdf[pitstopsdf['name_y']== 'Hungaroring']
lap_time_spa = pitstopsdf[pitstopsdf['name_y']== 'Circuit de Spa-Francorchamps']

lap = lap_time_silverstone.groupby('year')[['milliseconds']].min().reset_index()
lap1 =  lap_time_monaco.groupby('year')[['milliseconds']].min().reset_index()
lap2 =  lap_time_monza.groupby('year')[['milliseconds']].min().reset_index()
lap3 = lap_time_catalunya.groupby('year')[['milliseconds']].min().reset_index()
lap4 = lap_time_hungaroring.groupby('year')[['milliseconds']].min().reset_index()
lap5 = lap_time_spa.groupby('year')[['milliseconds']].min().reset_index()

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=lap.year, y=lap.milliseconds,
                    mode='lines',
                    name='Silverstone'))
fig1.add_trace(go.Scatter(x=lap1.year, y=lap1.milliseconds,
                    mode='lines',
                    name='Monaco'))
fig1.add_trace(go.Scatter(x=lap2.year, y=lap2.milliseconds,
                    mode='lines',
                    name='Monza'))
fig1.add_trace(go.Scatter(x=lap3.year, y=lap3.milliseconds,
                    mode='lines',
                    name='Catalunya'))
fig1.add_trace(go.Scatter(x=lap4.year, y=lap4.milliseconds,
                    mode='lines',
                    name='Hungaroring'))
fig1.add_trace(go.Scatter(x=lap5.year, y=lap5.milliseconds,
                    mode='lines',
                    name='Spa-Francorchamps'))

fig1.update_layout(title='Snelste pitstoptijden per Circuit per jaar',
                   xaxis_title='Jaren',
                   yaxis_title='Pitstoptijden',
                   template = "plotly_dark")
with col2:
       st.plotly_chart(fig1)





