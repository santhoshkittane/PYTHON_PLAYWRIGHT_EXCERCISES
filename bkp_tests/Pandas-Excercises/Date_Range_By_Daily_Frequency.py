from datetime import datetime
import pandas as pd

start_date = datetime.strptime("2026-01-17", "%Y-%m-%d")
end_date = datetime.strptime("2026-01-24", "%Y-%m-%d")

D='D'

date_list=pd.date_range(start=start_date, end=end_date, freq=D)
print('Create Date List between two dates with daily frequency')
print('in Original Format:',date_list)
print('in String Format:',date_list.strftime('%Y-%m-%d'))


