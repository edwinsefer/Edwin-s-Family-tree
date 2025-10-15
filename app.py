import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

firebase init
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
        submitted = st.form_submit_button("Add Member")

        if submitted:
            doc_ref = db.collection("family").document(name)
            doc_ref.set({
                "name": name,
                "dob": dob.strftime("%Y-%m-%d"),
                "phone": phone,
                "address": address,
"spouse": spouse,
                "children": [c.strip() for c in children.split(",") if c.strip()],
                "created_at": datetime.datetime.now()
            })
            st.success("Family Member Added!")

elif choice == "View Family Tree":
    members = db.collection("family").stream()
    for m in members:
        data = m.to_dict()
        st.subheader(data["name"])
        st.write(f"📅 DOB: {data['dob']}")
        st.write(f"📞 Phone: {data['phone']}")
        st.write(f"🏠 Address: {data['address']}")
        st.write(f"❤️ Spouse: {data['spouse']}")
        st.write(f"👶 Children: {', '.join(data['children'])}")

        st.markdown("---")

