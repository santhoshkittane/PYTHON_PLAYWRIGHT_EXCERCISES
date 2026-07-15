from datetime import date, datetime

current_date = date.today()
current_date=current_date.strftime("%Y-%d-%b")
current_datetime = datetime.now()
current_datetime=current_datetime.strftime("%Y-%d-%b %H:%M")

print(f"Current Date: {current_date}")
print(f"Current DateTime: {current_datetime}")


print("=======================NOW=====================")
now = datetime.now()
current_time = now.strftime("%H:%M")
current_date = now.strftime("%Y-%d-%b")
print(f"Current Time is {current_time} and Date is {current_date}")

