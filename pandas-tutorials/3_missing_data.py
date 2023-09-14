import pandas as pd
import numpy as np

# prepare data
dates = pd.date_range('20230730', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]: dates[1], "E"] = 1
print(df1)

# To drop any rows that have missing data
print(df1.dropna(how="any"))

# Filling missing data
print(df1.fillna(value=5))

# to get the boolean mask where values are nan
print(pd.isna(df1))
