import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from scipy import stats


df = pd.read_csv("user_behavior_dataset.csv")
df.dropna(inplace=True)
df = df[df['Screen_On_Time'] > 0]

mean_screen = df['Screen_On_Time'].mean()
median_screen = df['Screen_On_Time'].median()
mode_screen = df['Screen_On_Time'].mode()[0]
std_screen = df['Screen_On_Time'].std()
range_screen = df['Screen_On_Time'].max() - df['Screen_On_Time'].min()
print(f"mean: {mean_screen:.2f}, median: {median_screen}, mode: {mode_screen}")
print(f"standard deviation: {std_screen:.2f}, range: {range_screen}")

plt.figure(figsize=(8,5))
sns.histplot(df['Screen_On_Time'], bins=20, kde=True)
plt.title("distribution of screen on time")
plt.xlabel("hours of day")
plt.ylabel("frequency")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["App_Usage_Time"])
plt.title("boxplot of app usage time")
plt.xlabel("minutes per day")
plt.show()

os_group = df.groupby("Operating_System")["Screen_On_Time"].mean()
os_group.plot(kind="bar", color=["skyblue", "salmon"])
plt.title("average screen time on by operating system")
plt.ylabel("hours per day")
plt.show()

print(df.describe())