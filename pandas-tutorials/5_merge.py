import pandas as pd
import numpy as np

# prepare data
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

# Concat
# Concatenating pandas objects together with concat()
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# Join
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on="key"))