import streamlit as st
from datetime import datetime, timedelta
import calendar

st.title("🕒 Arrest Duration Calculator")

input_date = st.text_input("Enter the date the arrest starts (DD/MM/YYYY):")
date_obj = datetime.strptime(input_date, "%d/%m/%Y").date()
arrest_length=0
on = st.toggle("DAYS/MONTHS",True)



if on:
    st.write("You have selected the duration of arrest in days.")
    arrest_length = st.number_input("Enter the length of the arrest in days:", min_value=1, step=1)
    if input_date:
        try:
            
            end_date = date_obj + timedelta(days=(int(arrest_length) - 1))
            st.success(f"The last day of the arrest is: {end_date.strftime('%d/%m/%Y')}")
        except ValueError:
            st.error("Invalid date format. Please use DD/MM/YYYY.")

else:
    st.write("You have selected the duration of arrest in months.")
    arrest_length = st.number_input("Enter the length of the arrest in months:", min_value=1, step=1)
    if input_date:
        try:
            # Calculate the end date by adding the number of months to the start date
            month = date_obj.month + int(arrest_length)
            year = date_obj.year + (month) // 12
            month = month % 12
            if month == 0:
                month = 12
                year -= 1
            day= date_obj.day
            if day!=1:
                day-=1
            else:
                if month!=1:
                    month-=1
                    day=calendar.monthrange(year,month)[1]
                else:
                    month=12
                    year-=1
                    day=calendar.monthrange(year,month)[1]

            end_date = date_obj.replace(year=year, month=month, day=day)
            st.success(f"The last day of the arrest is: {end_date.strftime('%d/%m/%Y')}")
        except ValueError:
            st.error("Invalid date format. Please use DD/MM/YYYY.")
