import streamlit as st

st.title('Uber pickups in NYC')
st.header('This is a header with a divider')

st.subheader('This is a subheader with a divider', divider='rainbow')

import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")


import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

def sqr(num):
    return num*num

num = st.number_input('Insert a number')

if(st.button("Calculate square")):
    res = sqr(num)
    st.text(res)

