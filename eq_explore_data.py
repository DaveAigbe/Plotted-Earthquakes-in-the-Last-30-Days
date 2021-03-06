import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data

filename = 'eq_data/eq_data_30_day_m1.json'

with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['place'])
# Map the Earthquakes
data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_text,
         'marker': {
             'size': [5*mag for mag in mags],
             'color': mags,
             'colorscale': 'Viridis',
             'reversescale': True,
             'colorbar': {'title': 'Magnitude'},
         }
         }]
metadata_title = all_eq_data['metadata']['title']


my_layout = Layout(title=metadata_title)

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='global_earthquakes.html')
