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