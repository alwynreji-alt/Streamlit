#? BMI CALACULATOR
import streamlit as st
st.title("BMI CALACULATOR ")

name=st.text_input("enter name:")
place=st.selectbox()

wei = st.number_input("enter the weight:",min_value=0)
hei = st.number_input("enter the height:",min_value=0)

st.write(name)
btn=st.button("BMI")

if btn:
    result=wei/((hei/100)**2)
    st.write("result", result)

    if result<18.5:
        st.info("UNDERWEIGHT")
    elif 18.5<=result<25:
        st.success("NORMAL")
    elif 25 <= result < 30:
        st.warning("OVERWIGHT")
    elif result >30:
        st.error("OBESITY")




















