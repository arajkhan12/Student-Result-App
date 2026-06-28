# import streamlit as st

# st.title("Workplace_tool")
# st.subheader("Task")
# st.text("Welcome")
# st.write("Task one")
# email = st.text_input("Enter your email")
# password = st.text_input("Enter you password",type = "password")
# button = st.button("Login")

# st.subheader("audio , Image , Select box")

# st.image("LION.jpg")
# st.audio("lion.mp3")
# st.video("Python.mp4")


# M_Com = st.selectbox("Select your favourite Mobile Company", ["Apple" , "Samsung","Xiaomi","Vivo"])
# st.write(M_Com)


# st.success("Success")
# st.error("Error")
# st.slider("Slider",1,20)

# st.text_area("Comments")

# st.date_input("Date")
# st.time_input("Time")

import streamlit as st

st.title("Student Result App")

name = st.text_input("Enter name: ")
marks = st.number_input("Enter marks: ")

if st.button("Show Result"):
    if marks < 101 and marks > 71:
        st.success(f"Passed {name} Congrlaguations ❤️👍❤️💕")
    else:
        st.error("Failed ❌")