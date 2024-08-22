import pandas as pd

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
# print(df)
print(df[['temperatura', 'classification']])
