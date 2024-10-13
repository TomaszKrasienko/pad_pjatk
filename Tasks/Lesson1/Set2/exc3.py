import pandas as pd
import numpy as np

rainfall = pd.read_csv('Data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape
print(inches)
#%%
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot styles
plt.hist(inches, 40);
#%%
days_without_rain = (inches == 0).sum()
print(f"Number days without rain: {days_without_rain}")
#%%
days_with_rain = (inches != 0).sum()
print(f"Number days with rain: {days_with_rain}")
#%%
days_with_more_05_inches = (inches > 0.5).sum()
print(f"Days with more than 0.5 inches: {days_with_more_05_inches}")
#%%
rainy_with_less_02 = ((inches != 0) & (inches < 0.2)).sum()
print(f"Rainy days with < 0.2 inches : {rainy_with_less_02}")
#%% md

#%%
seattle_data = pd.read_csv('Data/Seattle2014.csv')
#%%
print(seattle_data)
#%%
seattle_data['PRCP'] = seattle_data['PRCP'] / 254.0  # 1/10mm -> inches
#%%
seattle_data['DATE'] = pd.to_datetime(seattle_data['DATE'], format="%Y%m%d")
#%%
print(seattle_data)
#%%
seattle_data_2014 = seattle_data[seattle_data['DATE'].dt.year == 2014]
#%%
print(seattle_data_2014)
#%%
rainy_days = seattle_data_2014[seattle_data_2014['PRCP'] != 0]
print(rainy_days)
#%%
rainy_days_median = np.median(rainy_days['PRCP'])
print(f"Median precip on rainy days in 2014 (inches): {rainy_days_median}")
#%%
no_rainy_days = seattle_data_2014[seattle_data_2014['PRCP'] != 0]
# print("Median precip on non-summer rainy days (inches):")
#%%
print(rainy_days)
#%%
# 22.06
# 22.09
summer_start_date = pd.to_datetime('2014-06-22')
summer_end_date = pd.to_datetime('2014-09-22')
summer_days_2014 = seattle_data_2014[((seattle_data_2014['DATE'] >= summer_start_date) 
                                      & (seattle_data_2014['DATE'] < summer_end_date))]
#%%
print(summer_days_2014)
#%%
print(f"Median precip on summer days in 2014 (inches):  {np.median(summer_days_2014['PRCP'])}")

#%%
print(f"Maximum precip on summer days in 2014 (inches): {summer_days_2014['PRCP'].max()}")
#%%
non_summer_days = seattle_data_2014[((seattle_data_2014['DATE'] < summer_start_date) 
                                      | (seattle_data_2014['DATE'] > summer_end_date))]
#%%
print(f"Median precip on non-summer rainy days (inches): {np.median(non_summer_days['PRCP'])}")