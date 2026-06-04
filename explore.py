import pandas as pd

df = pd.read_csv("C:\\Users\\poula\\Downloads\\co2\\student_perfomence\\Pass-Fail Data.csv")
print(df.head())
print(df.info())
print(df.describe())