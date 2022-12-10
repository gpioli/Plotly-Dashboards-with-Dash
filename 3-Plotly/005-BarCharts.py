import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Reading data
df = pd.read_csv('../Data/2018WinterOlympics.csv')
print(df)

##################################
# Setting data for the Bar Chart #
##################################
data = [go.Bar(x=df['NOC'],
               y=df['Total'])]
layout = go.Layout(title='Total Medals per Country Bar Chart')
figure = go.Figure(data=data, layout=layout)

# Graphing
pyo.plot(figure, filename='005-BarCharts-TotalMedals_per_Country_Bar_Chart.html')

#########################################
# Setting data for the Nested Bar Chart #
#########################################

# Let's not just display the total, but the amount of each medal type (Nested):
# In order to do this we need 3 bar plots, each under a trace:

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold,',
                marker={'color': '#FFD700'}) # we can google: color picker in order to select colors

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker={'color': '#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker={'color': '#CD7F32'})

data_for_nested_n_stacked = [trace1, trace2, trace3]

layout_for_nested = go.Layout(title='Total Medals per type and Country Bar Chart')
figure_for_nested = go.Figure(data=data_for_nested_n_stacked, layout=layout_for_nested)

# Graphing
pyo.plot(figure_for_nested, filename='005-BarCharts-TotalMedals_per_Country_Nested_Bar_Chart.html')

##########################################
# Setting data for the Stacked Bar Chart #
##########################################

# Let's not just display the total, but the amount of each medal type (Stacked):
# In order to do this we need 3 traces:


layout_for_stacked = go.Layout(title='Total Medals per type and Country Stacked Bar Chart', barmode='stack')
# Notice the change in the layout
figure_for_nested = go.Figure(data=data_for_nested_n_stacked, layout=layout_for_stacked)

# Graphing
pyo.plot(figure_for_nested, filename='005-BarCharts-Total_Medals_per_type_and_Country_Stacked_Bar_Chart.html')
