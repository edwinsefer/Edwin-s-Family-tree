```python
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

Firebase init
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

st.title("Edwin Family Tree App")

menu = ["Add Member", "View Family Tree"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Member":
    with st.form("entry_form"):
        name = st.text_input("Name")
        dob = st.date_input("Date of Birth")
        phone = st.text_input("Mobile Number")
        address = st.text_area("Address")
        spouse = st.text_input("Spouse Name")
        children = st.text_area("Children (comma separated)")