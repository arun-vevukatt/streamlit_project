# import streamlit as st
# from streamlit import text_input
#
# #
# # num1=st.number_input("enter first number: ",min_value=0)
# # num2=st.number_input("enter second number: ",min_value=0)
# #
# # num=num1+num2
# # # st.write("total: ",num)
# #
# # #text input
# # name=st.text_input("enter your name: ")
# # # st.write(name)
# #
# # #date
# # date=st.date_input("enter date")
# # # st.write(date)
# #
# # #button
# # btn=st.button("ADD")
# #
# # if btn:
# #     st.write("Your name: ",name)
# #     st.write("total: ", num)
# #     st.write(date)
# #
# #
#
#
#
# #BMI CALCULATOR
#
# st.title("BMI CALUCULATOR")
#
# weight=st.number_input("enter weight(kg): ",min_value=0)
# height=st.number_input("enter height(cm): ",min_value=0)
#
#
# btn=st.button("ADD")
# if btn:
#     bmi = weight / ((height / 100) ** 2)
#     if bmi<18.5:
#         st.error("underweight")
#     elif bmi>=18.5 and bmi<25:
#         st.success("normal")
#     elif bmi>=25 and bmi<30:
#         st.warning("overweight")
#     else:
#         st.error("obesity")
#

import streamlit as st
from datetime import date
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

