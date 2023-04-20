import pandas as pd

# Step 2
df = pd.read_csv('data.csv', index_col=1)

# Step 3
print(df)
print(df.index)

# Step 4
print(df.head(3))
print(df.tail(5))

# Step 5
print(df.max())
print(df.min())

# Step 6
df_sorted = df.sort_values('Generosity', ascending=False)
print(df_sorted.head(10))

# Step 7
print(df.mean())
print(df.loc['Italy'])
print(df.loc['Italy'] > df.mean())

# Step 8
df.plot(y='GDP per capita')

# Step 9
df.plot(x='Score', y='GDP per capita', kind='scatter')

# Step 10
df.plot(x='Social support', y='Healthy life expectancy', kind='scatter')

# Step 11
df.plot(x='GDP per capita', y='Generosity', kind='scatter')
