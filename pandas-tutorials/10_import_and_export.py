import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

# writing to a csv file
df.to_csv("foo.csv")

# reading from a csv file
print(pd.read_csv("foo.csv"))

# writing to a HDF5 Store
df.to_hdf("foo.h5", "df")
# reading from a HDF5 Store
pd.read_hdf("foo.h5", "df")

# Writing to an Excel file
df.to_excel("foo.excel", sheet_name="Sheet1")
# reading from an Excel file
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])

