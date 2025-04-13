import calendar
from datetime import datetime, timedelta


input_date = input("Enter the date the arrest was started or will start in the next format (DD/MM/YYYY): ")
arrest_length = int(input("Enter the length of the arrest in days: "))
try:
    date_obj = datetime.strptime(input_date, "%d/%m/%Y").date()
    next_day = date_obj + timedelta(days=(arrest_length - 1))
    print("The next day is:", next_day.strftime("%d/%m/%Y"))
except ValueError:
    print("Invalid date format. Please use DD/MM/YYYY.")
