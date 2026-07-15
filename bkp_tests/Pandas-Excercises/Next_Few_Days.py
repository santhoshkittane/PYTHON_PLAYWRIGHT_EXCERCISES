from datetime import date, timedelta

start_dt = date.today().isoformat()

date_list = []

x = input("Enter the number of days to add: ")
i=1
for i in range(int(x)+1):
    start_dt = date.today() + timedelta(days=i)
    date_list.append(start_dt.isoformat())


print('Final list is :',date_list)