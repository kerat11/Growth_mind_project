import streamlit as st

st.title("📝 Student List")


if 'students' not in st.session_state:
    st.session_state.students = []


name = st.text_input("Enter student name")
if name:  
    age = st.number_input("Age", min_value=5, max_value=30, value=10)
    grade = st.selectbox("Class", ["1st", "2nd", "3rd", "4th", "5th" ,"6th" ,"7th" ,"8th" ,"9th","10"])

    if st.button("Add Student"):
        st.session_state.students.append(f"{name}, Age: {age}, Class: {grade}")
        st.success("Student added!")


if st.session_state.students:
    st.write("### All Students")
    for student in st.session_state.students:
        st.write(student)
    
    if st.button("Clear List"):
        st.session_state.students = []
        st.success("List cleared!")
else:
    st.info("No students added yet")
