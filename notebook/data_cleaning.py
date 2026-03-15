import pandas as pd

# load dataset
df = pd.read_excel("../data/OLA_DataSet.xlsx")

# remove unnecessary column
df = df.drop(columns=["Vehicle Images"])

# fill missing payment methods
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")

# fill ratings
df["Driver_Ratings"] = df["Driver_Ratings"].fillna(0)
df["Customer_Rating"] = df["Customer_Rating"].fillna(0)

# convert time column
df["Time"] = pd.to_datetime(df["Time"], errors="coerce")

# create new column (Hour)
df["Hour"] = df["Date"].dt.hour

# save cleaned dataset
df.to_csv("../data/ola_cleaned.csv", index=False)

print("Cleaning Completed ✅")
print(df.head())