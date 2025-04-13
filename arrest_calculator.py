import streamlit as st
from datetime import datetime, timedelta

st.title("🕒 Arrest Duration Calculator")

input_date = st.text_input("Enter the date the arrest starts (DD/MM/YYYY):")
arrest_length = st.number_input("Enter the length of the arrest in days:", min_value=1, step=1)

if input_date:
    try:
        date_obj = datetime.strptime(input_date, "%d/%m/%Y").date()
        end_date = date_obj + timedelta(days=(int(arrest_length) - 1))
        st.success(f"The last day of the arrest is: {end_date.strftime('%d/%m/%Y')}")
    except ValueError:
        st.error("Invalid date format. Please use DD/MM/YYYY.")
