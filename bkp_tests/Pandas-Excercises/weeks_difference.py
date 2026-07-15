from datetime import date, datetime, timedelta
from time import strftime, strptime

inp = input("Enter your Date to find the difference in weeks(in YYYY-MM-DD Fomat): ")
inp = datetime.strptime(inp, "%Y-%m-%d")
number_days = date.today()-inp.date()
number_weeks = number_days//7
print(f'There are{number_days} that is {number_weeks} weeks difference between {inp} and {date.today()}')
