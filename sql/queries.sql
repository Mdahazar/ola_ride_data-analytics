
-- 1. Retrieve All Successful Bookings
SELECT *
FROM ola_rides
WHERE Booking_Status = 'Success';



-- 2. Average Ride Distance for Each Vehicle Type
SELECT 
Vehicle_Type,
AVG(Ride_Distance) AS Avg_Ride_Distance
FROM ola_rides
GROUP BY Vehicle_Type;



-- 3. Total Number of Rides Cancelled by Customers
SELECT 
COUNT(*) AS Customer_Cancelled_Rides
FROM ola_rides
WHERE Booking_Status = 'Canceled by Customer';



-- 4. Top 5 Customers With Highest Number of Rides
SELECT 
Customer_ID,
COUNT(*) AS Total_Rides
FROM ola_rides
GROUP BY Customer_ID
ORDER BY Total_Rides DESC
LIMIT 5;



-- 5. Number of Rides Cancelled by Drivers
SELECT 
COUNT(*) AS Driver_Cancelled_Rides
FROM ola_rides
WHERE Booking_Status = 'Canceled by Driver';



-- 6. Maximum and Minimum Driver Ratings for Prime Sedan
SELECT
MAX(Driver_Ratings) AS Max_Rating,
MIN(Driver_Ratings) AS Min_Rating
FROM ola_rides
WHERE Vehicle_Type = 'Prime Sedan';



-- 7. All Rides Where Payment Was Made Using UPI
SELECT *
FROM ola_rides
WHERE Payment_Method = 'UPI';



-- 8. Average Customer Rating Per Vehicle Type
SELECT 
Vehicle_Type,
AVG(Customer_Rating) AS Avg_Customer_Rating
FROM ola_rides
GROUP BY Vehicle_Type;



-- 9. Total Booking Value of Successful Rides
SELECT 
SUM(Booking_Value) AS Total_Revenue
FROM ola_rides
WHERE Booking_Status = 'Success';



-- 10. Incomplete Rides With Reason
SELECT 
Booking_ID,
Incomplete_Rides_Reason
FROM ola_rides
WHERE Incomplete_Rides = 'Yes';



-- Ride Volume Over Time
SELECT 
Date,
COUNT(*) AS Ride_Count
FROM ola_rides
GROUP BY Date
ORDER BY Date;



-- Revenue by Payment Method
SELECT 
Payment_Method,
SUM(Booking_Value) AS Revenue
FROM ola_rides
GROUP BY Payment_Method;



-- Cancellation Reasons by Customer
SELECT 
Canceled_Rides_by_Customer,
COUNT(*) AS Total
FROM ola_rides
GROUP BY Canceled_Rides_by_Customer;