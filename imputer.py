import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

print("Original DataFrame: \n")
print(df, "\n")

cat_cols = ['Sizes', 'Colors']
for col in cat_cols:
    mode_val = df[col].mode()[0]
    df[col].fillna(mode_val, inplace=True)


num_cols = ['Ratings']
for col in num_cols:
    median_val = df[col].median()
    df[col].fillna(median_val, inplace=True)

print("Imputed DataFrame: \n")
print(df, "\n")


