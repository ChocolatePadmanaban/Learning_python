# spice

import pandas as pd 
import numpy as np 

frame = pd.DataFrame({'MTG':[32,23,45,56,66,44,33,22,32],
                        'Patangali':[98,78,98,97,72,34,23,43,33],
                        'Aachi': [23,43,23,22,43,54,65,76,32]},
                    index=['Tmarind', 'Coriander','Capsicum','Garlic','Ginger','Garam Masala','Mint','Saffron','Turmeric'])
print(frame)
print(frame.groupby("MTG").mean())