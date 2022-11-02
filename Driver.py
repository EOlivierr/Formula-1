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

#Driver plots








#Nationality plot oud
#driver_country = driversdf.groupby('nationality').driver_name.nunique().reset_index() 
#driver_country = driver_country.rename(columns = {'driver_name': 'driver_counts'})
#driver_country1 = driver_country[driver_country.driver_counts >= 30].sort_values('driver_counts' ,ascending = False )
#driver_country1.loc[len(driver_country1.index)] = ['Others', (driver_country.driver_counts.sum() - driver_country1.driver_counts.sum())]

#labels = driver_country1['nationality']
#values = driver_country1['driver_counts']

#fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, pull=[0, 0, 0, 0, 0, 0, 0.2], hoverinfo='label+value')])

#fig3.update_layout(title='Verdeling van nationaliteit per seizoen', template = "plotly_dark")

#st.plotly_chart(fig3)

#Nationality plot nieuw
nat_df= driver_analysis_df[['year','driver_name', 'points_sum']]
nat_df1= nat_df.merge(driversdf, on='driver_name')

start_date5 = min(nat_df1['year'])
end_date5 = max(nat_df1['year'])
max_days5 = end_date5-start_date5
slider5 = st.slider('Selecteer de datum', min_value=start_date5 ,max_value=end_date5)
st.markdown(slider5)

nat_df1 = nat_df1[nat_df1['year']==slider5]

driver_country3 = nat_df1.groupby('nationality').driver_name.nunique().reset_index() 
driver_country3 = driver_country3.rename(columns = {'driver_name': 'driver_counts'})
#driver_country4 = driver_country3[driver_country3.driver_counts >= 30].sort_values('driver_counts' ,ascending = False )
#driver_country4.loc[len(driver_country3.index)] = ['Others', (driver_country3.driver_counts.sum() - driver_country4.driver_counts.sum())]
#st.dataframe(driver_country3)

labels2 = driver_country3['nationality']
values2 = driver_country3['driver_counts']

fig4 = go.Figure(data=[go.Pie(labels=labels2, values=values2, hole=.3, pull=[0, 0, 0, 0, 0, 0, 0.2], hoverinfo='label+value')])

fig4.update_layout(title='Verdeling van nationaliteit per seizoen', template = "plotly_dark")

st.plotly_chart(fig3)







condf= con_analysis_df[['year_','constructors_name_', 'points_sum']]
condf= condf.sort_values(by='points_sum', ascending=False)


drivers = driver_analysis_df[['year','driver_name', 'points_sum']]
#slider van de driver plot
start_date = min(drivers['year'])
end_date = max(drivers['year'])
max_days = end_date-start_date
slider = st.slider('Select date', min_value=start_date ,max_value=end_date)
st.markdown(slider)

drivers = drivers[drivers['year']==slider]
drivers = drivers.sort_values(by='points_sum')

#Punten van de driver plot
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

fig.update_layout(title='Correlatie tussen Qualificatie positie en eindpositie',
                   xaxis_title='Qualificatie positie',
                   yaxis_title='Eindpositie',
                   template = "plotly_dark")

fig.update_yaxes(type='linear')

st.plotly_chart(fig)
