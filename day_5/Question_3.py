'''Goal: Using "Boolean Masks" to fix messy data—this is how "Data Hours" actually look.
The "Outlier" Filter:
    1. Data: prices = np.array([10, 15, 300, 20, 25, 400, 18, 22])
    2. Task: Create a mask to find all prices under 100. Use that mask to create a new "Cleaned" array that removes the 300 and 400.
    
The "NaN" Replacement:
    1. Data: sensor_readings = np.array([1.2, np.nan, 1.5, 1.8, np.nan, 2.0])
    2. Task: Use np.isnan() to find the missing values and replace them with the mean (average) of the non-missing values.
The "Normalization" (Math Booster):
    1. Data: A random $5 \times 5$ matrix.
    2. Task: Subtract the mean of the entire matrix from every element, and then divide by the standard deviation. (This is called "Standardizing" data for Machine Learning).'''
    
    
import numpy as np
prices = np.array([10, 15, 300, 20, 25, 400, 18, 22])
cleaned_prices = prices[prices<100]
print(cleaned_prices)

sensor_readings = np.array([1.2, np.nan, 1.5, 1.8, np.nan, 2.0])
missing_values = np.nanmean(sensor_readings)
sensor_readings[np.isnan(sensor_readings)] = missing_values
print(sensor_readings)

arr = np.random.rand(5,5)
standardizing = arr-np.mean(arr)/np.std(arr)
print(standardizing)