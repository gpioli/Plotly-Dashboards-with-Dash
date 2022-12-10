import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

# Creating random data
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)  # returns a sample of the normal distribution

# Creating the line chart...
trace0 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='markers',
                    name='markers')

trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='mylines')

trace2 = go.Scatter(x=x_values,
                    y=y_values-5,
                    mode='lines+markers',
                    name='myfavorite')

data = [trace0, trace1, trace2]
layout = go.Layout(title='Line Charts')  # layout is optional!
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='002-lineCharts')
