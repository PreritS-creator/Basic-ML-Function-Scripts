import pandas as pd

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)
print("Original dataframe: \n")
print(df, "\n")

encoding = {}

cat_vals = df['Sizes'].dropna().unique()

for val, cat in enumerate(cat_vals):
    encoding[cat] = val

df['Sizes'] = df['Sizes'].map(encoding)
print("Encoded Dataframe: \n")
print(df, "\n")
