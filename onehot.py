import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)
print("Original dataframe: \n")
print(df, "\n")

cat_vals = df['Colors'].dropna().unique()

for val in cat_vals:
    df[f'Color_{val}'] = np.where(df['Colors'] == val, 1, 0)

df=df.drop(columns=['Colors'])

print("Encoded Dataframe: \n")
print(df, "\n")