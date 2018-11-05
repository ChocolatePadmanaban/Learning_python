# hi

import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(6),index= pd.date_range('1/1/2000',
                periods = 6, freq = 'M'))

print(ts)
print(ts.shift(2))
print(ts / ts.shift(1)-1)
ts_local = ts.tz_localize('UTC')
print(ts_local)
print(ts_local.tz_convert('US/Eastern'))