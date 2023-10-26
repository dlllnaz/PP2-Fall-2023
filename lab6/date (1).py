#task1 Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
current_d = datetime.now()
new_d = current_d - timedelta(days=5)
new_d_str = new_d.strftime("%Y-%m-%d")
print("Current Date:", current_d)
print("Date 5 days ago (formatted):", new_d_str)

#task2 Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#task3 Write a Python program to drop microseconds from datetime.
from datetime import datetime
datetime_without_micros = datetime.now().replace(microsecond=0)
print("datetime:", datetime.now())
print("without microseconds:", datetime_without_micros)

#task4 Write a Python program to calculate two date difference in seconds.
import datetime
date_s1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_s2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date_format = '%Y-%m-%d %H:%M:%S'
date1 = datetime.datetime.strptime(date_s1, date_format)
date2 = datetime.datetime.strptime(date_s2, date_format)
time_difference = date2 - date1
difference_in_seconds = time_difference.total_seconds()
print(f"{difference_in_seconds}")