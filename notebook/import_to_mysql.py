import pandas as pd
import mysql.connector
import numpy as np

# Load dataset
df = pd.read_csv("../data/ola_cleaned.csv")

# Replace NaN with None for MySQL
df = df.replace({np.nan: None})

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ola_project"
)

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ola_rides (
Date DATETIME,
Time VARCHAR(20),
Booking_ID VARCHAR(50),
Booking_Status VARCHAR(50),
Customer_ID VARCHAR(50),
Vehicle_Type VARCHAR(50),
Pickup_Location VARCHAR(100),
Drop_Location VARCHAR(100),
V_TAT FLOAT,
C_TAT FLOAT,
Canceled_Rides_by_Customer VARCHAR(100),
Canceled_Rides_by_Driver VARCHAR(100),
Incomplete_Rides VARCHAR(20),
Incomplete_Rides_Reason VARCHAR(200),
Booking_Value INT,
Payment_Method VARCHAR(50),
Ride_Distance INT,
Driver_Ratings FLOAT,
Customer_Rating FLOAT,
Hour INT
)
""")

insert_query = """
INSERT INTO ola_rides VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

data = [tuple(row) for row in df.values]

# Insert in batches
batch_size = 1000

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    cursor.executemany(insert_query, batch)
    connection.commit()
    print(f"Inserted {i + len(batch)} rows")

print("✅ Data imported successfully!")

cursor.close()
connection.close()