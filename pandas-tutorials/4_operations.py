import pandas as pd
import numpy as np

# prepare data
dates = pd.date_range('20230730', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

# Stats
# Operations in general exclude missing data
#  Performing a descriptive statistic
print(df.mean())
# Same operation on the other axis
print(df.mean(1))
# Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
print(df.sub(s, axis="index"))

# Apply
# np.cumsum 是累加函数
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

# String Methods
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s.str.lower())