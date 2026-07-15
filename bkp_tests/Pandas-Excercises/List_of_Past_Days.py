from datetime import date, timedelta
start_dt = date.today().isoformat()

inp = input("Enter the number of days to Subtract: ")
date_list = []

for i in range(int(inp)+1):
    start_dt = date.today() - timedelta(days=i)
    date_list.append(start_dt.isoformat())

print(date_list)