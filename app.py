import streamlit as st
from PIL import Image
import time
import openai

# -------- Sidebar Navigation --------
menu = st.sidebar.selectbox("📂 Select a Tool", [
    "🏠 Home",
    "🏫 Timetable",
    "📊 Attendance Tracker",
    "🕒 Study Timer",
    "🧠 AI Study Buddy",
    "🎓 CGPA Calculator"
])

# -------- Home Page --------
if menu == "🏠 Home":
    st.title("🎓 Welcome to LPU Campus Toolkit")
    st.markdown("Made with ❤ by *Ayush Panigrahi*")
    st.markdown("---")
    st.write("This all-in-one web app is designed to simplify your student life at LPU.")
    st.write("Choose a tool from the sidebar to begin!")

# -------- Timetable --------
elif menu == "🏫 Timetable":
    st.subheader("📅 Your Class Timetable")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    timetable = {}
    for day in days:
        subjects = st.text_area(f"{day}'s Classes", "Example: 9AM-10AM: Math, 11AM-12PM: Python")
        timetable[day] = subjects

# -------- Attendance Tracker --------
elif menu == "📊 Attendance Tracker":
    st.subheader("📈 Attendance Calculator")
    attended = st.number_input("Enter classes attended", min_value=0)
    total = st.number_input("Enter total classes", min_value=1)

    if st.button("Calculate Attendance"):
        percentage = (attended / total) * 100
        st.success(f"Your Attendance: {percentage:.2f}%")

# -------- Study Timer --------
elif menu == "🕒 Study Timer":
    st.subheader("⏳ Study Timer")
    study_minutes = st.slider("Select study duration (minutes)", 1, 120, 25)

    if st.button("Start Timer"):
        st.info("Timer started. Stay focused!")
        with st.empty():
            for i in range(study_minutes * 60, 0, -1):
                mins, secs = divmod(i, 60)
                timer_display = f"{mins:02d}:{secs:02d}"
                st.markdown(f"## ⏱ {timer_display}")
                time.sleep(1)
            st.success("⏰ Time's up! Great work!")

# -------- AI Study Buddy --------
elif menu == "🧠 AI Study Buddy":
    st.subheader("🤖 Ask AI Study Buddy")
    openai.api_key = "your-openai-api-key"  # Replace with your actual OpenAI key

    user_question = st.text_input("Ask anything related to your subjects:")

    if st.button("Get Help"):
        if user_question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful study assistant."},
                            {"role": "user", "content": user_question}
                        ]
                    )
                    answer = response['choices'][0]['message']['content']
                    st.success(answer)
                except Exception as e:
                    st.error(f"Error: {e}")

# -------- CGPA Calculator --------
elif menu == "🎓 CGPA Calculator":
    st.subheader("🎯 Calculate Your CGPA")
    num_subjects = st.number_input("How many subjects?", min_value=1, step=1)

    total_grade_points = 0
    for i in range(int(num_subjects)):
        grade = st.selectbox(f"Select grade for subject {i+1}", ["O", "A+", "A", "B+", "B", "C", "P", "F"], key=i)
        grade_point_map = {
            "O": 10,
            "A+": 9,
            "A": 8,
            "B+": 7,
            "B": 6,
            "C": 5,
            "P": 4,
            "F": 0
        }
        total_grade_points += grade_point_map[grade]

    if st.button("Calculate CGPA"):
        cgpa = total_grade_points / num_subjects
        st.success(f"Your CGPA is: {cgpa:.2f}")