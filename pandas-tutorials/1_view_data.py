import pandas as pd
import numpy as np

# prepare data
index = pd.date_range("1/1/2000", periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
print(df)

# how to view the top and bottom rows of the frame
print(df.head())
print(df.tail(3))

# display the index and columns
print(df.index)
print(df.columns)

#  to_numpy()
print(df.to_numpy())

# show a quick statistic summary of your data
print(df.describe())

# transposing your data
print(df.T)

# sorting by an axis
print(df.sort_index(axis=1, ascending=False))

# sorting by values
print(df.sort_values(by="B"))