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
PAGE_NAME = "Driver"
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









#Driver plots
#Nationality plot oud
nat_df= driver_analysis_df[['year','driver_name', 'points_sum']]
nat_df1= nat_df.merge(driversdf, on='driver_name')

start_date5 = min(nat_df1['year'])
end_date5 = max(nat_df1['year'])
max_days5 = end_date5-start_date5

with st.sidebar:
       slider5 = st.slider('Selecteer het jaargetal om de Nationaliteiten te zien!', min_value=start_date5 ,max_value=end_date5)


nat_df1 = nat_df1[nat_df1['year']==slider5]

driver_country3 = nat_df1.groupby('nationality').driver_name.nunique().reset_index() 
driver_country3 = driver_country3.rename(columns = {'driver_name': 'driver_counts'})

labels2 = driver_country3['nationality']
values2 = driver_country3['driver_counts']

fig4 = go.Figure(data=[go.Pie(labels=labels2, values=values2, hole=.3, pull=[0, 0, 0, 0, 0, 0, 0.2], hoverinfo='label+value')])

#fig4.update_layout(title='Verdeling van nationaliteit per seizoen', template = "plotly_dark")

with col2:
       st.plotly_chart(fig4)

#Nationality plot nieuw       
fig12 = go.Figure(data=go.Bar(
        x = driver_country3['nationality'],
        y = driver_country3['driver_counts']
        ))

fig12.update_layout(title='Verdeling van nationaliteit per seizoen',
                    height=500,
                     width=700)
with col2:
       st.plotly_chart(fig12)       
       
       
       
       
       
       
       
       
       
condf= con_analysis_df[['year_','constructors_name_', 'points_sum']]
condf= condf.sort_values(by='points_sum', ascending=False)


drivers = driver_analysis_df[['year','driver_name', 'points_sum']]
#slider van de driver plot
start_date = min(drivers['year'])
end_date = max(drivers['year'])
max_days = end_date-start_date

with st.sidebar:
       slider = st.slider('Selecteer het jaargetal om de punten van de Coureurs te zien te zien!', min_value=start_date ,max_value=end_date)


drivers = drivers[drivers['year']==slider]
drivers = drivers.sort_values(by='points_sum')

#Punten van de driver plot
with col2:
       fig1 = st.bar_chart(drivers, y='points_sum', x=('driver_name'))

       
#Correlatie tussen p1 en pole
scat_df = merged_df[['raceId', 'year','driver_name', 'constructors_name', 'grid', 'position', 'circuit_name']]
scat_df = scat_df[scat_df.year == 2021]
#scat_df = scat_df[scat_df.constructors_name == 'Williams']
#scat_df = scat_df[scat_df.driver_name == 'Nicholas Latifi']
scat_df = scat_df[scat_df.position != r'\N']
scat_df = scat_df.sort_values(by= ['position', 'grid'], ascending = [True, True]).head(500)

alle_drivers= scat_df['driver_name'].unique()

                   
  
fig = go.Figure()

teller = 0
buttonlist = [dict(label = "Kies een coureur", method='update', args=[{"visible": [True*len(alle_drivers)]}])]

for i in alle_drivers:
    df2= scat_df[scat_df['driver_name'] == i]
    
    fig.add_trace(go.Scatter(x=df2["grid"], y=df2["position"], mode='markers', name=str(i)))
    
    lijst = [False]*len(alle_drivers)
    lijst[teller] = True
    teller = teller + 1
    
    one_button = dict(label = str(i), method='update', args=[{"visible": lijst}])
    buttonlist.append(one_button)
    
fig.update_layout(
updatemenus=[
        dict(
            buttons=buttonlist,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=1.1,
            xanchor="left",
            y=1.2,
            yanchor="top"
        ),        
    ]
)

fig.update_layout(xaxis_title='Qualificatie positie',
                   yaxis_title='Eindpositie',
                   template = "plotly_dark")

fig.update_yaxes(type='linear')

with col2:
       st.plotly_chart(fig)
       
with col2:     
       st.markdown("[![Foo](data:image/png;base64,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)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)Klik voor link naar dataset")

