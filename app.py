import streamlit as st
import time
import openai

# 🔑 OpenAI API Key
openai.api_key = "your-api-key-here"

# 🌙 Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# 💡 Apply dark mode CSS
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #0e1117;
                color: white;
            }
            .stTextInput, .stTextArea, .stNumberInput, .stSlider, .stButton {
                background-color: #21262d;
                color: white;
            }
            .css-1d391kg, .css-18e3th9 {
                background-color: #0e1117;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# 🧱 Mobile CSS (still applies for responsiveness)
st.markdown("""
    <style>
    @media only screen and (max-width: 600px) {
        .css-1d391kg {padding: 1rem;}
        .stTextInput, .stTextArea, .stNumberInput, .stSlider, .stButton {
            width: 100% !important;
        }
        .st-bw, .st-cq, .st-bv {
            flex-direction: column !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 📄 Page Setup
st.set_page_config(page_title="LPU Student Toolkit", layout="wide")
st.title("🎓 LPU Student Toolkit")
st.markdown("Welcome Ayush! Manage your student life like a pro 🚀")

# 📂 Sidebar Menu
menu = st.sidebar.selectbox("📂 Select a Tool", [
    "📅 Timetable",
    "📊 Attendance Tracker",
    "⏰ Study Timer",
    "🤖 AI Study Buddy"
])

# 📅 Timetable Tool
if menu == "📅 Timetable":
    st.header("📅 Your Weekly Timetable")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        st.subheader(day)
        st.text_area(f"Enter your schedule for {day}", key=day)

# 📊 Attendance Tracker
elif menu == "📊 Attendance Tracker":
    st.header("📊 Attendance Tracker")
    subject = st.text_input("Enter subject name")
    attended = st.number_input("Lectures attended", min_value=0)
    total = st.number_input("Total lectures", min_value=1)
    if st.button("Calculate Attendance"):
        percentage = (attended / total) * 100
        st.success(f"Your attendance is {percentage:.2f}%")
        if percentage < 75:
            st.warning("⚠ You need to attend more classes!")

# ⏰ Study Timer
elif menu == "⏰ Study Timer":
    st.header("⏰ Study Timer")
    study_minutes = st.slider("Set Study Timer (in minutes)", 1, 120, 25)
    if st.button("Start Timer"):
        with st.empty():
            for i in range(study_minutes * 60, 0, -1):
                mins, secs = divmod(i, 60)
                st.metric("⏱ Time Remaining", f"{mins:02d}:{secs:02d}")
                time.sleep(1)
            st.success("🎉 Time's up! Great job!")

# 🤖 AI Study Buddy
elif menu == "🤖 AI Study Buddy":
    st.header("🤖 Ask your AI Study Buddy")
    st.markdown("Ask anything related to your studies and get an AI-powered response!")

    question = st.text_area("📘 Type your study question:")
    if st.button("Get Answer"):
        if question:
            with st.spinner("Thinking..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful study assistant for college students."},
                        {"role": "user", "content": question}
                    ]
                )
                st.success(response['choices'][0]['message']['content'])
        else:
            st.warning("Please type a question to get an answer.")

# 📱 Footer
st.markdown("""
    <hr style='margin-top: 50px;'>
    <center style='font-size:14px;'>📱 Mobile + 🌙 Dark Mode • Made with ❤ by Ayush at LPU</center>
""", unsafe_allow_html=True)