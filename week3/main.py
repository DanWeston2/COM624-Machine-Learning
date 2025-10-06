import pandas as pd

df = pd.read_csv("dataframe with indexes and header.csv")

caloriesMean = df["calories"].mean()
df["calories"].fillna(caloriesMean, inplace=True)

durationMean = df["duration"].mean()
df["duration"].fillna(durationMean, inplace=True)

heartbeatMean = df["heartbeat"].mean()
df["heartbeat"].fillna(heartbeatMean, inplace=True)

print(df)
