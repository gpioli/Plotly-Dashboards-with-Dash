import numpy as np
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

# Conditional filtering
print('')
print('Conditional filtering')
ser_of_bool = df['Age'] > 30
print(ser_of_bool)

# Passing them to the data frame allows us to filter:
print(df[ser_of_bool])
# Exact same thing and most common use:
print(df[df['Age'] > 30])
# Inside our data frame we are asking which columns contain registries with an age > 30 and printing those results

# Useful methods:

# Grabing unique values:
print('Grabing unique values: ')
print(df['Age'].unique())
# And we can use nunique to know the lenght of that list
print(df['Age'].nunique())

# Listing the columns
print(df.columns)  # notice as this is an attribute of the df and not a method, so it doesnt require '()'

# info() reports back information of our df
print(df.info())

# describe() will give us an statistical summary:
print(df.describe())

# index -> creates an automatic range index of the df
print(df.index)

# MIXING numpy and Pandas

mat = np.arange(0, 50).reshape(5, 10)
print(mat) # this is a numpy matrix

# We can convert it to a pandas df:
new_df = pd.DataFrame(data=mat)
print(new_df) # Notice Pandas automatically labels the column names and the index (rows)

# Let's give it another try, providing our own columns name and index:
new_mat_2 = np.arange(0, 10).reshape(5, 2)
new_df_2 = pd.DataFrame(data=new_mat_2, columns=['A', 'B'], index=['Peter', 'Maria', 'Nick', 'Tomas', 'Jessie'])
print(new_df_2)
