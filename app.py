import streamlit as st
from database import init_db

st.set_page_config(page_title="BILIWAKA MarketSpace", layout="wide")
init_db()

st.markdown("""
<style>
body {background:#F7F3EE;}
h1,h2,h3 {color:#3A2A26;}
.card {
    background:white;
    padding:15px;
    border-radius:15px;
    margin-bottom:15px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}
.featured {border:3px solid #C8A96A;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 BILIWAKA MarketSpace")
st.write("Connecting Buyers & Vendors in Your Area")
