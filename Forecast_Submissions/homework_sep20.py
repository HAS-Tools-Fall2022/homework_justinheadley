import numpy as np 
import math 
import matplotlib as plt

filename =('https://raw.githubusercontent.com/HAS-Tools-Fall2022'
'/Course-Materials22/main/data/verde_river_daily_flow_cfs.csv')
flows = np.loadtxt(filename, delimiter=',', usecols= 1)
print(flows) #this shows that for the past 4 weeks, there has been a gradual decline in streamflow, and I expect this trend will continue. 

week_1 = (flows[-1] - flows[-2])
week_2 = (flows[-2] - flows[-3])
week_3 = flows[-3] - flows[-4]

mean_weekly_decline = (week_1 + week_2 + week_3) / 3
print('The average weekly decline in streamflow for the past 3 weeks has been ', np.round(mean_weekly_decline, 2), ' cfs.')
week_1_fcst = flows[-1] + mean_weekly_decline
week_2_fcst = week_1_fcst + mean_weekly_decline
print('If this trend continues, the flow will be ', np.round(week_1_fcst,2), ' in one week and ', np.round(week_2_fcst), ' in two weeks.')
