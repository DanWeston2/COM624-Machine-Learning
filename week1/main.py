import pandas as pd

df = pd.read_csv("titanic.csv")

df.info()

# tells you what columns have missing values
print(df.isnull().sum())

df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

df.to_csv("cleanedTitanic.csv", index=False)
