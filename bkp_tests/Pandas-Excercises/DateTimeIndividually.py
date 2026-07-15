from datetime import date, datetime

now = datetime.now()

print(f'Current Year is:{now.year}')
print(f'Current Month is:{now.strftime("%B")}')
print(f'Current Date is:{now.day}')
print(f'Today is:{now.strftime("%A")}')
print(f'Current Time is {now.strftime("%I:%M %p")}')
