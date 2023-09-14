import pandas as pd
import numpy as np

tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
print(df)
df2 = df[:4]
print(df2)

# Stack
# The stack() method compresses a level in the DataFrame's columns
stacked = df2.stack()
print(stacked)

# With a "stacked" DataFrame or Series, the inverse operation of stack() is unstack()
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

# Pivot tables
df = pd.DataFrame({
    "A": ["one", "one", "two", "three"] * 3,
    "B": ["A", "B", "C"] * 4,
    "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
    "D": np.random.randn(12),
    "E": np.random.randn(12),
})
print(df)
print(pd.pivot(df, values="D", index=["A", "B"], columns=["C"]))