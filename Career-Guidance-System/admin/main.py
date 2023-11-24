import streamlit as st
from functions import *
from custom_query import custom_query

menu = ["Home", "Students", "Counsellors", "Appointments","Custom Query Tab"]

tab = st.tabs(menu)

with tab[0]:
    st.title("Admin Page")

with tab[1]:
    students()

with tab[2]:
    counsellors()

with tab[3]:
    appointments()

with tab[4]:
    custom_query()
