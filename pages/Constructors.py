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
PAGE_NAME = "Constructors"
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



#constructor punten per seizoen
condf= con_analysis_df[['year_','constructors_name_', 'points_sum']]
condf = condf[condf['points_sum']!= 0]
condf= condf.sort_values(by='points_sum', ascending=False)

#slider van de punten per seizoen
start_date7 = min(condf['year_'])
end_date7 = max(condf['year_'])
max_days7 = end_date7-start_date7

with st.sidebar:
       slider7 = st.slider('Selecteer de datum om de punten van de teams te zien!', min_value=start_date7 ,max_value=end_date7)
       
condf = condf[condf['year_']==slider7]

with col2:
       fig1 = st.bar_chart(condf, y='points_sum', x='constructors_name_')





       
       
       
#meest succesvolle constructor
condf1= con_analysis_df[['year_','constructors_name_', 'points_sum']]
condf1 = condf1[condf1['points_sum']>= 30]
condf1= condf1.sort_values(by='points_sum', ascending=False)
#condf1.sort_values(by='year_', ascending=True)

#slider van succesvolle constructor
start_date9 = min(condf1['year_'])
end_date9 = max(condf1['year_'])
max_days9 = end_date9-start_date9

with st.sidebar:
       slider9 = st.slider('Selecteer de datum om de punten van de teams te zien!',value=(start_date9,end_date9), min_value=start_date9 ,max_value=end_date9)

condf1 = condf1[(condf1.year_ >= slider9[0]) & (condf1.year_ <= slider9[1])]

fig9 = px.bar(condf1, y='points_sum', x='constructors_name_')

with col2:
       st.plotly_chart(fig9)
       

       
 
       
       
       
       
       
       
       
       
#regplot voor een constructor
condf2= con_analysis_df[['year_','constructors_name_', 'points_sum']]
#condf2 = condf2[condf2['year_']!= 2022]
alle_teams= con_analysis_df['constructors_name_'].unique()

with st.sidebar:
       optie = st.selectbox(
              'Selecteer een team',
         (alle_teams))

#condf2 = con_analysis_df[con_analysis_df.constructors_name_ == 'Ferrari']
condf2 = condf2[(condf2.constructors_name_ == optie)
#condf2 = condf2.drop(1085)
#condf2 = condf2[condf2['year_']!= 2022]
#condf2.sort_values(by='year_', ascending=True)


#fig = px.scatter(x=condf2["year_"], 
                 #y=condf2["points_sum"],
                 #trendline="ols", 
                 #trendline_scope="overall", 
                 #trendline_color_override="black",)

#fig.update_layout(xaxis_title="Seizoen",
       #yaxis_title="Aantal punten")

#with col2:
       #st.plotly_chart(fig)
st.write(optie)     
st.dataframe(condf2)
       
       
       
       
       
       
       

#dropdown menu punten per seizoen per team


fig = go.Figure()

teller = 0
buttonlist = [dict(label = "Kies een constructeur", method='update', args=[{"visible": [True*len(alle_teams)]}])]

for i in alle_teams:
    df2= condf1[condf1['constructors_name_'] == i]
    
    fig.add_trace(go.Scatter(x=df2["year_"], y=df2["points_sum"], mode='markers', 
                             #trendline="ols", trendline_scope="overall", 
                             #trendline_color_override="black", 
                             name=str(i)))
    
    lijst = [False]*len(alle_teams)
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

fig.update_layout(xaxis_title='Seizoen',
                   yaxis_title='Aantal punten',
                  
                 )

fig.update_yaxes(type='linear')

with col2:
       st.plotly_chart(fig)


