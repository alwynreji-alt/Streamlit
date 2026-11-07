import streamlit as st
from datetime import date
st.title("STUDENT REGISTRATION FORM ")

name = st.text_input("enter name:")
age = st.number_input("enter age:", min_value=0)
dob = st.date_input("enter date of birth:",min_value=date(20,1,1),
                                                 max_value=date.today(),
                                                 value=date.today())
email= st.text_input("enter the email:")
gender = st.radio("gender", ["Male", "Female"])
course = st.selectbox("course",["java","dotnet","testing"])

btn = st.button("Submit")

if btn :
     st.subheader("name : "+ name)
     st.subheader("age : "+ str(age))
     st.subheader("DOB : "+str(dob))
     st.subheader("email : "+email)
     st.subheader("gender : "+gender)
     st.subheader("course : "+course)