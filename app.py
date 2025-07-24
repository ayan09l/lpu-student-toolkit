import streamlit as st

# Page setup
st.set_page_config(page_title="LPU Campus Toolkit", layout="wide")

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", width=150)
    st.markdown("## Student Info")
    name = st.text_input("Name", "Ayush Panigrahi")
    roll = st.text_input("Roll Number", "123456789")
    section = st.text_input("Section", "K22HP")
    
    st.markdown("## Tools")
    choice = st.radio("Select", [
        "🏠 Home", "📅 Timetable", "📊 Attendance", "⏱ Study Timer",
        "🧠 AI Study Buddy", "📈 CGPA Calculator", "🗓 Smart Study Planner"
    ])

    st.image("assets/profile.jpg", width=100)
    st.markdown("<center><small>Made by Ayush Panigrahi</small></center>", unsafe_allow_html=True)

# Floating LPU Courses (bottom-right)
courses = [
    "B.Tech CSE", "B.Tech ECE", "B.Tech ME", "MBA", "BBA", "B.Com",
    "BCA", "MCA", "B.Sc Agri", "B.Design", "B.Pharm", "B.Arch", "BA LLB", "B.Ed", "Others"
]
float_html = f"""
<style>
#lpu-float {{
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #f44336;
    color: white;
    padding: 10px 15px;
    border-radius: 10px;
    z-index: 100;
    cursor: pointer;
}}
#lpu-modal {{
    display: none;
    position: fixed;
    bottom: 70px;
    right: 20px;
    background: white;
    padding: 15px;
    border: 2px solid #aaa;
    border-radius: 10px;
    z-index: 101;
}}
</style>
<button id="lpu-float" onclick="document.getElementById('lpu-modal').style.display='block'">LPU Courses</button>
<div id="lpu-modal">
<b>All Courses:</b><ul>
{''.join([f'<li>{c}</li>' for c in courses])}
</ul>
<button onclick="document.getElementById('lpu-modal').style.display='none'">Close</button>
</div>
"""
st.markdown(float_html, unsafe_allow_html=True)

# Pages
if choice == "🏠 Home":
    st.markdown(f"""
    <div style='background:linear-gradient(to right,#6dd5ed,#2193b0);padding:20px;border-radius:10px;color:white'>
        <h2>Hello, {name}! 👋</h2>
        <p>Roll No: {roll} | Section: {section}</p>
        <p>Welcome to the all-in-one LPU Toolkit!</p>
    </div>
    """, unsafe_allow_html=True)

elif choice == "📅 Timetable":
    st.header("📅 Timetable")
    st.info("Feature coming soon.")

elif choice == "📊 Attendance":
    st.header("📊 Attendance Tracker")
    subjects = st.text_input("Subjects (comma-separated)", "AI, ML, Math")
    for sub in subjects.split(","):
        sub = sub.strip()
        att = st.number_input(f"{sub} Attended", min_value=0)
        total = st.number_input(f"{sub} Total", min_value=1)
        if total:
            st.write(f"📘 {sub}: {(att/total)*100:.2f}%")

elif choice == "⏱ Study Timer":
    st.header("⏱ Study Timer")
    st.info("Coming soon!")

elif choice == "🧠 AI Study Buddy":
    st.header("🧠 Ask AI Study Buddy")
    q = st.text_input("Ask anything:")
    if q:
        st.success("This is where the AI reply will come (API integration coming).")

elif choice == "📈 CGPA Calculator":
    st.header("📈 CGPA Calculator")
    credits = st.number_input("Total Credits", min_value=1)
    points = st.number_input("Total Grade Points")
    if credits:
        st.write(f"🎓 CGPA: {points/credits:.2f}")

elif choice == "🗓 Smart Study Planner":
    st.header("🗓 Smart Study Planner")
    st.warning("Coming soon!")

# Footer
st.markdown("---")
st.markdown("<center><small>© 2025 | Made with ❤ by Ayush Panigrahi</small></center>", unsafe_allow_html=True)
