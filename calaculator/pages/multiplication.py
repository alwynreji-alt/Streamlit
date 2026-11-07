import streamlit as st

st.title("multiplication")

x = st.number_input("enter the number 1",min_value=0)
y = st.number_input("enter the number 2",min_value=0)

btn=st.button("mul")

if btn:
    result=x*y

    st.write("product:",result)