import pandas as pd
import numpy as np

df = pd.read_csv('cell2celltrain.csv')

df = df.drop(columns=["CustomerID"])
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df = df.drop_duplicates()

for col in ["MonthlyRevenue", "TotalRecurringCharge"]:
    df.loc[df[col] < 0, col] = np.nan

# print((df["AgeHH1"] == 0).sum(), (df["AgeHH2"] == 0).sum())

df["AgeHH1"] = df["AgeHH1"].replace(0, np.nan)
df["AgeHH2"] = df["AgeHH2"].replace(0, np.nan)

# print(df[["AgeHH1", "AgeHH2"]].isnull().mean() * 100)

# for col in df.select_dtypes(include=["object"]).columns:
#     print(col, df[col].unique()[:10])

df["HandsetPrice"] = df["HandsetPrice"].replace("Unknown", np.nan).astype(float)
df["CreditRating"] = df["CreditRating"].str[0].astype(int)

# print("ServiceArea unique: ", df["ServiceArea"].nunique())

df = df.drop(columns=["ServiceArea"])

df.to_csv("cleaned_data.csv", index=False)

print(df.shape)
print(df["Churn"].value_counts(normalize=True))
print(df.dtypes.value_counts())