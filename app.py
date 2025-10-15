st.set_page_config(page_title="My Family Tree", layout="centered")
st.title("👨‍👩‍👧‍👦 My Family Tree App")


if "members" not in st.session_state:
    st.session_state.members = []

st.subheader("➕ Add New Family Member")
with st.form("member_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    anniversary = st.date_input("Wedding Anniversary (optional)", value=None)
    phone = st.text_input("Mobile Number")
    address = st.text_area("Address")
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Add Member")
    if submitted:
        member_data = {
            "Name": name,
            "DOB": dob,
            "Anniversary": anniversary,
            "Phone": phone,
            "Address": address,
            "Image": image
        }
        st.session_state.members.append(member_data)

st.success(f"{name} added successfully!")

st.subheader("📋 Family Members List")

for i, member in enumerate(st.session_state.members):
    with st.expander(f"{i+1}. {member['Name']}"):
        st.write(f"📅 DOB: {member['DOB']}")
        st.write(f"💍 Anniversary: {member['Anniversary']}")
        st.write(f"📞 Phone: {member['Phone']}")
        st.write(f"🏠 Address: {member['Address']}")
        if member["Image"]:
            img = Image.open(member["Image"])
            st.image(img, width=150)

