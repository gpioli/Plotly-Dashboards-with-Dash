import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../SourceData/nst-est2017-alldata.csv')
print(df.head())

new_df = df[df['DIVISION'] == '1']
new_df.set_index('NAME', inplace=True)  # Inplace allows us to store the changes in place, in other words, without
# having to store the changes with an assignation (new_df = new_df.set_index('NAME')

# List comprehension
# Masking
list_of_pop_col = [col for col in new_df.columns if col.startswith('POP')]
new_df = new_df[list_of_pop_col]  # We filter based on the column values (starting with 'POP') (previous masking)

print(new_df.head())

# We use list comprehension in order to graph
data = [go.Scatter(x=new_df.columns,
                   y=new_df.loc[name],
                   mode='lines',
                   name=name) for name in new_df.index]
# for every name in the df, set x=columns, and set y to that 'name' # (rows) values

pyo.plot(data)


