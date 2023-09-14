import pandas as pd
import numpy as np

# converting secondly data into 5-minutely data
rng = pd.date_range("1/1/2021", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print(ts.resample("5Min").sum())

print("***" * 20)

# Series.tz_localize() localizes a time series to a time zone
rng = pd.date_range("1/1/2021", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize("UTC")
print(ts_utc)
print(ts_utc.tz_convert("US/Eastern"))
print("***" * 20)

# converting between time span representation
rng = pd.date_range("1/1/2021", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())
print("***" * 20)

# Converting between period and timestamp enables some convenient arithmetic functions to be used.
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
print(ts.head())