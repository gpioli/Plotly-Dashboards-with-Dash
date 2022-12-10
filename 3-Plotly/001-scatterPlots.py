# Working with scatter plots

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)  # from 1 to 101, give me 100 numbers
random_y = np.random.randint(1, 101, 100)

# nesting a plot inside of a list... be patient and we'll catch up
data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',  # markers
                   marker=dict(
                       size=12,
                       color='rgb(51, 204, 153)',
                       symbol='pentagon',
                       line={'width': 2}
                   ))]

# creating a layout variable: titles, axis titles, etc.
layout = go.Layout(title='Hello First Plot',
                   xaxis={'title': 'My X Axis'},
                   yaxis=dict(title='My Y Axis'),  # This does the same, but is another way of constructing a dictionary
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='001-scatter.html')
