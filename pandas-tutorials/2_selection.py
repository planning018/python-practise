import pandas as pd
import numpy as np

# prepare data
dates = pd.date_range('20230730', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

# selecting a single column
print(df["A"])
# slices the rows
print(df[0:3])
print(df["20230801":"20230804"])

# selection by label
print(df.loc[dates[0]])
# selection on a multi-axis by label
print(df.loc[:, ["A", "B"]])
# showing label slicing, both endpoints are included
print(df.loc["20230731":"20230803", ["A", "B"]])
# reduction in the dimensions of the returned objects
print(df.loc["20230731", ["A", "B"]])
# for getting a scalar value
print(df.loc[dates[0], "A"])
# fast access to a scalar
print(df.at[dates[0], "A"])

# selection by position
# select via the position of the passed integers
print(df.iloc[3])
# by integer slices, acting similar to Numpy/Python
print(df.iloc[3:5, 0:2])
# by lists of integer position locations, similar to the Numpy/Python style
print(df.iloc[[1, 2, 4], [0, 2]])
# for slicing rows explicitly
print(df.iloc[1:3, :])
# for slicing columns explicitly
print(df.iloc[:, 1:3])
# for getting a value explicitly
print(df.iloc[1, 1])
# fast access to a scalar
print(df.iat[1, 1])

# Boolean indexing
# Using a single column's values to select data:
print(df[df["A"] > 0])
# Selecting values from a DataFrame where a boolean condition is met
print(df[df > 0])
# Using the isin() method for filtering:
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2["E"].isin(["two", "four"])])

# Setting
# Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20230730", periods=6))
print(s1)
df["F"] = s1
print(df)
# Setting values by label
df.at[dates[0], "A"] = 0
# Setting values by position
df.iat[0, 1] = 0
# Setting by assigning with a Numpy array
df.loc[:, "D"] = np.array([5] * len(df))
print(df)
# A where operation with setting
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
