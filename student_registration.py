import streamlit as st
from streamlit.elements.widgets import checkbox

st.title("STUDENT FORM")

name=st.text_input("Enter Name: ")
age=st.number_input("enter age")
dob=st.date_input("input date")
mail=st.text_input("enter mailid: ")

gender=st.radio("gender",["male","female"])

course=st.selectbox("course",["python","dotnet","testing"])

btn=st.button("done")
if btn:
    st.write(name)
    st.write(age)
    st.write(dob)
    st.write(mail)
    st.write(gender)
    st.write(course)