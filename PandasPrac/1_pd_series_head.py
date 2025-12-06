import pandas as pd
import numpy as np


s = pd.Series([a for a in range(20)])
print(s)
print(s.head())
print(s.head(10))
print(s.tail())
print(s.head(-2))
print((s.tail(10)))