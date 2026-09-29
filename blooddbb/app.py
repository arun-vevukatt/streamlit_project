import streamlit as st
from donor_db import AddRetrieveUpdateDelete
st.title("BLOOD DONOR DATABASE")


tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETREIVE','UPDATE','DELETE'])
b = AddRetrieveUpdateDelete()
with tab1:
    st.title("CREATE RECORD")

    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    blood_group = st.text_input("Blood group")
    city = st.text_input("City")
    last_donation = st.date_input("Donation Date")

    btn = st.button("Create")
    if btn:

        b.create(name, blood_group, phone_number, city, last_donation)
    st.success("RECORDED CREATED")
with tab2:
    records = b.read()
    if records:
        st.table(records)

with tab3:
    id = st.number_input("enter id", min_value=0)
    records = b.retrieve(id)
    btn = st.button("Retrieve")
    if btn:
        if records:
            st.header("DETAILS")
            st.write("Name: ", records[1])
            st.write("Blood Group: ", records[2])
            st.write("Phone Number: ", records[3])
            st.write("Place: ", records[4])
            st.write("Date: ", records[5])