import pandas as pd
import numpy as np

# Sample dataset with 15 records
data = {
    'OrderID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', np.nan, 'Jack', 'Karen', 'Liam', 'Mia', np.nan],
    'TableNumber': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Waiter': ['John', 'Mike', 'Sara', 'John', 'Mike', 'Sara', 'John', 'Mike', np.nan, 'John', 'Mike', 'Sara', 'John', np.nan, 'Sara'],
    'MenuItem': ['Pizza', 'Burger', 'Pasta', 'Salad', 'Pizza', 'Burger', 'Pasta', 'Salad', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Pizza', 'Burger', 'Salad'],
    'Quantity': [2, 1, 3, 1, 2, 1, 1, 2, 3, 1, 2, 1, 2, 1, 3],
    'Price': [20, 15, 30, 10, 20, 15, 30, 10, 20, 15, 10, 30, 20, 15, 10],
    'OrderTime': ['12:00', '12:05', '12:10', '12:15', '12:20', '12:25', np.nan, '12:35', '12:40', '12:45', '12:50', '12:55', '13:00', '13:05', '13:10']
}

# Convert to DataFrame
df = pd.DataFrame(data)

print(df)
#HANDLING MISSING DATA
# Check for missing data
print("\nMissing Data Summary:\n", df.isnull().sum())

# Fill missing CustomerName with 'Unknown'
df['CustomerName'].fillna('Unknown', inplace=True)

# Fill missing Waiter with 'TBD'
df['Waiter'].fillna('TBD', inplace=True)

# Fill missing OrderTime with the forward fill method
df['OrderTime'].fillna(method='ffill', inplace=True)

# Drop rows with any remaining missing values
df.dropna(inplace=True)

print("\nData After Handling Missing Values:\n", df)

# HIERARCHICAL INDEXING
# Set a hierarchical index using TableNumber and OrderID
df.set_index(['TableNumber', 'OrderID'], inplace=True)

# Sort the index
df.sort_index(inplace=True)

print("\nHierarchical Index DataFrame:\n", df)

# AGGREGATION
# Aggregate total quantity and revenue per table
aggregated_data = df.groupby('TableNumber').agg(
    TotalQuantity=('Quantity', 'sum'),
    TotalRevenue=('Price', 'sum')
)

print("\nAggregated Data by TableNumber:\n", aggregated_data)

# Reset index to perform aggregation on Waiter
df_reset = df.reset_index()

# Aggregate total orders and average price per waiter
waiter_aggregation = df_reset.groupby('Waiter').agg(
    TotalOrders=('OrderID', 'count'),
    AveragePrice=('Price', 'mean')
)

print("\nAggregated Data by Waiter:\n", waiter_aggregation)
