import numpy as np
import pandas as pd

# Read the csv file with the rainfall data
data = pd.read_csv('data/data_in_csv.csv')

# Remove rows with missing data
data = data.dropna(how="any", axis=0)
data.cov()
data.corr()

# Classify annual rainfall of more than 3000mm as flood = True else False
data['FLOOD'] = data.apply(
    lambda row: True if row['annual'] > 3000 else False, axis=1)

# Convert the [True False] values to [1,0] for easy processing
data['FLOOD'].replace([True, False], [1, 0], inplace=True)

# Separate the concept values and the target values
x = data.iloc[:, 1:19]
y = data.iloc[:, -1]
print(x)
print(y)
