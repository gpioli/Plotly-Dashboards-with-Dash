#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../Data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']
print(df.head())
print(df)

new_df = df.drop('LST_DATE', axis=1, inplace=False)  # axis = 0 eliminates rows(index), axis = 1 eliminates columns
new_df.set_index('DAY', inplace=True)
print(new_df)


# Use a for loop (or list comprehension to create traces for the data list)
# data = []
data = [go.Scatter(x=new_df['LST_TIME'],
                   y=new_df.loc[day, 'T_HR_AVG'],
                   mode='lines',
                   name=day) for day in days]

print(data)
print(type(data))
# Old way of creating the same:
# for day in days:
#     # What should go inside this Scatter call?
#     trace = go.Scatter(x=new_df['LST_TIME'],
#                        y=df.loc[day, 'T_HR_AVG'],
#                        mode='lines',
#                        name=day)
#     data.append(trace)

# Define the layout
layout = go.Layout(title='Hourly temperature over weekday')




# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo = pyo.plot(fig, filename='004-PlotlyExercise-hourly-temp')
