import streamlit as st
from datetime import date
from blood_fun import BookListCreateRetrieveUpdateDelete
tab1,tab2,tab3,tab4,tab5=st.tabs(["ADD","VIEW","RETRIEVE","UPDATE","DELETE"])
b=BookListCreateRetrieveUpdateDelete()



with tab1:
    st.title("ADD NEW DONOR")

    name = st.text_input("Enter the name of the donor:")
    blood_group = st.selectbox("Enter the blood group of the donor:",["A+","A-","B+","B-","O+","O-","AB+","AB-"])
    phone_no = st.number_input("Enter the phone number of the donor:",min_value=0)
    city = st.text_input("Enter the donor city:")
    last_donation = st.date_input("enter the donor date:")
    btn=st.button("ADD DONOR")

    if btn:
       b.post(name,blood_group,phone_no,city,last_donation)
       st.success("Donor record has been added successfully!")


with tab2:
    st.title("VIEW DONOR")

    result= b.get()
    if result:
        for row in result:
            with st.container(border=True):

                st.subheader(f"Donor ID :{row[0]}")

                st.write("Donor Name :",row[1])
                st.write("blood_group:",row[2])
                st.write("phone_no:",row[3])
                st.write("city:",row[4])
                st.write("last_donation:",row[5])
    else:
        st.info("No donors found.")

with tab3:
    st.title("RETRIEVE DONOR")

    id = st.number_input("Enter the Donor ID:", min_value=1,step=1,key="retrieve_donor_id")
    btn =st.button("SEARCH DONOR")
    if btn:
        result=b.get_id(id)
        if result:
            row = result[0]
            st.success("DONOR FOUND!")
            with st.container(border=True):

                st.subheader(f"Donor ID :{row[0]}")
                st.write("Donor Name :", row[1])
                st.write("blood_group:", row[2])
                st.write("phone_no:", row[3])
                st.write("city:", row[4])
                st.write("last_donation:", row[5])


with tab4:
    st.title("UPDATE DONOR")

    id = st.number_input("Enter the Donor ID:", min_value=1,step=1,key="update_donor_id")
    name = st.text_input("Enter the updated name of the donor:")
    blood_group = st.selectbox("Enter the updated blood group of the donor:",["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    phone_no = st.text_input("Enter the updated phone number of the donor",)
    city =st.text_input("Enter the updated city of the donor")
    last_donation =st.date_input("Enter the updated last donation date of the donor")

    btn =st.button("UPDATED DONOR DATA")

    if btn:

        result=b.put(
            id,
            name,
            blood_group,
            phone_no,
            city,
            last_donation
        )

        if result>0:
            st.success("Donor data updated successfully")
        else:
            st.error("No Donor found with that ID")


with tab5:
    st.title("DELETE DONOR")


