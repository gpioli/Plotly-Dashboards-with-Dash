import pandas as pd

df = pd.read_csv('salaries.csv')
print(df)

# Selecting columns:
print('')
print('Selecting columns')
print(df['Salary'])
# notice the index positions are numbered for us

# Grabbing multiple columns of data:
print('')
print('Grabbing multiple columns')
print(df[['Name', 'Salary']])  # We must pass it as a list of name columns to the data frame, that's why the double
# square brackets

# Similarly to Numpy, we can grab min, max, mean values from a column
print('')
print('Grabbing min, max and mean values from a column')
print('Min Salary: ', df['Salary'].min())
print('Max Salary: ', df['Salary'].max())
print('Mean Salary: ', df['Salary'].mean())

