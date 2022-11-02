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
