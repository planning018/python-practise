import pandas as pd
import numpy as np

# create Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# create DateFrame
dates = pd.date_range('20230730', periods=6)
print(dates)

# create a DateFrame by passing a Numpy array, with a datetime index and labeled columns
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
print(df)

# create a DateFrame by passing a dictionary of objects that can be converted into a series-like structure
df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20230620"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
})
print(df2)
print(df2.dtypes)