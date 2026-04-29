import streamlit as st
from database import c

st.title("Admin Panel")

st.write("Users", c.execute("SELECT * FROM users").fetchall())
st.write("Ads", c.execute("SELECT * FROM ads").fetchall())
