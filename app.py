import streamlit as st
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(page_title="LPU Campus Toolkit", layout="wide")

# --- Sidebar ---
st.sidebar.image("assets/logo.png", width=150)
st.sidebar.markdown("## 👤 Student Details")

name = st.sidebar.text_input("Enter Your Name", "Ayush Panigrahi")
roll_no = st.sidebar.text_input("Roll Number", "123456789")
section = st.sidebar.text_input("Section", "K22PA")

st.sidebar.markdown("---")
page = st.sidebar.radio("📚 Navigate", [
    "Home",
    "Timetable",
    "Attendance Tracker",
    "CGPA Calculator",
    "AI Study Buddy 🤖",
    "Smart Study Planner 📅",
    "Study Timer ⏱"
])

# --- Sidebar: LPU Courses Section ---
st.sidebar.markdown("---")
with st.sidebar.expander("📘 LPU Courses"):
    st.markdown("""
    - B.Tech - CSE  
    - B.Tech - ECE  
    - B.Tech - Civil  
    - B.Tech - Mechanical  
    - BCA / MCA  
    - BBA / MBA  
    - B.Com / M.Com  
    - B.Sc / M.Sc  
    - B.A / M.A  
    - Pharmacy  
    - Law  
    - Design  
    - Architecture  
    - Hotel Management  
    - Journalism  
    """)

# --- Home Page ---
if page == "Home":
    st.markdown(f'''
        <div style="background-color: #f3e5f5; padding: 30px; border-radius: 10px;">
            <h2 style="color: #6a1b9a;">🌟 Welcome, <span style="color: #4a148c;">{name}</span>!</h2>
            <p style="font-size: 17px; color: #4a148c;">
                This is your all-in-one <b>LPU Campus Toolkit</b> designed to make your student life easier! 🧠📚<br><br>
                Use the tools on the left sidebar to:
                <ul>
                    <li>🤖 Ask questions with the <b>AI Study Buddy</b></li>
                    <li>📅 Manage your <b>Timetable</b></li>
                    <li>📊 Track your <b>Attendance</b></li>
                    <li>🎓 Calculate your <b>CGPA</b></li>
                    <li>🧠 Plan using the <b>Smart Study Planner</b></li>
                </ul>
                Keep growing, keep shining at LPU! 💜✨
            </p>
        </div>
    ''', unsafe_allow_html=True)

# --- Timetable Page ---
elif page == "Timetable":
    st.title("📅 Timetable Manager")
    st.info("Coming soon...")

# --- Attendance Tracker Page ---
elif page == "Attendance Tracker":
    st.title("📊 Attendance Tracker")
    st.info("Coming soon...")

# --- CGPA Calculator Page ---
elif page == "CGPA Calculator":
    st.title("🎓 CGPA Calculator")
    st.info("Coming soon...")

# --- AI Study Buddy Page ---
elif page == "AI Study Buddy 🤖":
    st.title("🤖 AI Study Buddy")
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
    user_question = st.text_area("Ask a study question...")
    if st.button("Get Answer"):
        if openai_api_key and user_question:
            try:
                import openai
                openai.api_key = openai_api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_question}]
                )
                st.success(response['choices'][0]['message']['content'])
            except Exception as e:
                st.error("❌ Failed to get response. Check your API key or question.")
        else:
            st.warning("Please enter both your API key and a question.")

# --- Smart Study Planner Page ---
elif page == "Smart Study Planner 📅":
    st.title("🧠 Smart Study Planner")
    st.info("Coming soon...")

# --- Study Timer Page ---
elif page == "Study Timer ⏱":
    st.title("⏱ Study Timer")
    st.info("Coming soon...")

# --- Floating LPU Courses Button in Right Bottom Corner ---
components.html("""
<style>
.floating-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #6a1b9a;
    color: white;
    padding: 12px 18px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    z-index: 9999;
}
.floating-box {
    display: none;
    position: fixed;
    bottom: 70px;
    right: 20px;
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 10px;
    width: 280px;
    z-index: 9998;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
}
</style>

<div class="floating-button" onclick="toggleCourses()">📘 LPU Courses</div>
<div class="floating-box" id="courses-box">
    <b style="font-size: 16px;">LPU All Courses</b><br><br>
    <ul style="padding-left: 20px;">
        <li>B.Tech - CSE</li>
        <li>B.Tech - ECE</li>
        <li>B.Tech - Civil</li>
        <li>B.Tech - Mechanical</li>
        <li>BCA / MCA</li>
        <li>BBA / MBA</li>
        <li>B.Com / M.Com</li>
        <li>B.Sc / M.Sc</li>
        <li>B.A / M.A</li>
        <li>Pharmacy</li>
        <li>Law</li>
        <li>Design</li>
        <li>Architecture</li>
        <li>Hotel Management</li>
        <li>Journalism</li>
    </ul>
</div>

<script>
function toggleCourses() {
    var box = document.getElementById("courses-box");
    box.style.display = (box.style.display === "none" || box.style.display === "") ? "block" : "none";
}
</script>
""", height=0)

# --- Footer ---
st.markdown("---")
st.markdown(
    "<center><small style='color: grey;'>Made by Ayush Panigrahi ❤ | LPU Campus Toolkit</small></center>",
    unsafe_allow_html=True
)
