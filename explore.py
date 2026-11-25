Boolean filter tests every row in a table with a yes/no or True/False rule. It will only keep the ones that are true.
df[“revenue”] makes a panda series, without a table structure. Where df[[“revenue”]] makes a 2-dimensional panda data frame with a table. 
When you write a pandas script, you can rerun the same calculations, cleanings and filtering without having to click through menus. 


import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print("--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- SHAPE ---")
print(df.shape)

print("\n--- COLUMNS ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

south = df[df['region'] == 'South']

print("\n--- SOUTH ROW COUNT ---")
print(len(south))

print("\n--- SOUTH FIRST 5 ROWS ---")
print(south.head())

print("\n--- TOP 5 BY REVENUE ---")
print(df.sort_values('revenue', ascending=False).head(5))

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print("\n--- BIG SOUTH ROW COUNT ---")
print(len(big_south))

print("\n--- BIG SOUTH FIRST 5 ROWS ---")
print(big_south.head())

df['per_unit'] = df['revenue'] / df['quantity']

print("\n--- FIRST 5 ROWS WITH PER_UNIT ---")
print(df.head())

print("\n--- MEAN PER-UNIT PRICE ---")
print(df['per_unit'].mean())

print("\n--- UNIQUE REGIONS ---")
print(df['region'].unique())

print("\n--- REGION VALUE COUNTS ---")
print(df['region'].value_counts())

subset = df[['region', 'product', 'revenue']]

print("\n--- SUBSET SHAPE ---")
print(subset.shape)

df.to_csv('data/explored.csv', index=False)
print("\nSaved data/explored.csv successfully!")