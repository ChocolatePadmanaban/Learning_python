#Global Stocks

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


st_price = pd.read_csv('stock_px.csv')
st_imp = st_price[['AAPL','MSFT']]
print(st_imp)
# st_imp[['AAPL','MSFT']].plot()
# st_imp.loc['13-02-2003':'20-06-2003'].plot()
# plt.show()
close_px = st_price[['AAPL','MSFT','XOM']]
close_px.AAPL.rolling(250).mean().plot()
plt.show()