#top 20 meest voorkomende circuits

most_circuits = fastestlapdf.groupby(['year','circuit_name']).count().reset_index()

m = most_circuits['circuit_name'].value_counts().reset_index().head(20)
m =  m.rename(columns ={'circuit_name': 'count', 'index': 'circuit_name'})

import plotly.express as px
fig = px.bar(m, x='count', y='circuit_name')

fig.update_layout(title='Top 20 meest voorkomende circuits in Formule 1',
                   xaxis_title='Circuits',
                   yaxis_title='Rondetijden',
                   template = "plotly_dark")

fig.show()


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

fig = go.Figure()

fig.add_trace(go.Scatter(x=lap.year, y=lap.fastest_lap,
                    mode='lines',
                    name='Silverstone'))
fig.add_trace(go.Scatter(x=lap1.year, y=lap1.fastest_lap,
                    mode='lines',
                    name='Monaco'))
fig.add_trace(go.Scatter(x=lap2.year, y=lap2.fastest_lap,
                    mode='lines',
                    name='Monza'))
fig.add_trace(go.Scatter(x=lap3.year, y=lap3.fastest_lap,
                    mode='lines',
                    name='Catalunya'))
fig.add_trace(go.Scatter(x=lap4.year, y=lap4.fastest_lap,
                    mode='lines',
                    name='Hungaroring'))
fig.add_trace(go.Scatter(x=lap5.year, y=lap5.fastest_lap,
                    mode='lines',
                    name='Spa-Francorchamps'))

fig.update_layout(title='Snelste rondetijden per Circuit per paar',
                   xaxis_title='Jaar',
                   yaxis_title='Rondetijden',
                   template = "plotly_dark")

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

fig = go.Figure()

fig.add_trace(go.Scatter(x=lap.year, y=lap.milliseconds,
                    mode='lines',
                    name='Silverstone'))
fig.add_trace(go.Scatter(x=lap1.year, y=lap1.milliseconds,
                    mode='lines',
                    name='Monaco'))
fig.add_trace(go.Scatter(x=lap2.year, y=lap2.milliseconds,
                    mode='lines',
                    name='Monza'))
fig.add_trace(go.Scatter(x=lap3.year, y=lap3.milliseconds,
                    mode='lines',
                    name='Catalunya'))
fig.add_trace(go.Scatter(x=lap4.year, y=lap4.milliseconds,
                    mode='lines',
                    name='Hungaroring'))
fig.add_trace(go.Scatter(x=lap5.year, y=lap5.milliseconds,
                    mode='lines',
                    name='Spa-Francorchamps'))

fig.update_layout(title='Snelste pitstoptijden per Circuit per jaar',
                   xaxis_title='Jaren',
                   yaxis_title='Pitstoptijden',
                   template = "plotly_dark")

#circuits op de kaart 
circuitsdf['text'] = circuitsdf['circuit_name'] + ', ' + 'Country: ' + circuitsdf['country'].astype(str)

fig = go.Figure(data=go.Scattergeo(
        lon = circuitsdf['lng'],
        lat = circuitsdf['lat'],
        text = circuitsdf['text'],
        mode = 'markers',
        marker_colorscale = "thermal"
        
        ))

fig.update_geos(projection_type="orthographic")

fig.update_layout(
        #title = 'Circuits of Formula 1 across the world<br>(Hover for info)',
        height=500,
        margin={"r":0,"t":0,"l":0,"b":0},
        template = "plotly_dark"
    )


fig.show()
