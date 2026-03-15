import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load cleaned data
df = pd.read_csv("../data/ola_cleaned.csv")

# 1 Ride count by vehicle type
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Vehicle_Type")
plt.title("Ride Volume by Vehicle Type")
plt.xticks(rotation=45)
plt.show()

# 2 Booking status distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Booking_Status")
plt.title("Booking Status Breakdown")
plt.show()

# 3 Revenue by payment method
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="Payment_Method", y="Booking_Value")
plt.title("Revenue by Payment Method")
plt.show()

# 4 Ride distance distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Ride_Distance"], bins=30)
plt.title("Ride Distance Distribution")
plt.show()

# 5 Driver vs customer ratings
plt.figure(figsize=(6,4))
sns.boxplot(data=df[["Driver_Ratings","Customer_Rating"]])
plt.title("Driver vs Customer Ratings")
plt.show()

# 6 Ride demand by hour
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Hour")
plt.title("Ride Demand by Hour")
plt.show()