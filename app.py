import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Quiz App", page_icon="🧠", layout="centered")

# -----------------------------
# CUSTOM UI
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: black;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Quiz Game App")

# -----------------------------
# QUESTIONS
# -----------------------------
questions = [
    {
        "question": "Capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Python is a ___?",
        "options": ["Snake", "Programming Language", "Game", "Movie"],
        "answer": "Programming Language"
    }
]

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.finished = False

# -----------------------------
# TIMER (30 sec per quiz)
# -----------------------------
TOTAL_TIME = 30
elapsed = int(time.time() - st.session_state.start_time)
remaining = TOTAL_TIME - elapsed

if remaining <= 0:
    st.session_state.finished = True

st.write(f"⏱ Time Left: {remaining} seconds")

# -----------------------------
# PROGRESS BAR
# -----------------------------
progress = st.session_state.index / len(questions)
st.progress(progress)

# -----------------------------
# QUIZ LOGIC
# -----------------------------
if not st.session_state.finished:
    q = questions[st.session_state.index]

    st.subheader(f"Question {st.session_state.index + 1}")
    st.write(q["question"])

    choice = st.radio("Select your answer:", q["options"], key=st.session_state.index)

    if st.button("Submit Answer"):
        if choice == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Correct Answer: {q['answer']}")

        if st.session_state.index < len(questions) - 1:
            st.session_state.index += 1
        else:
            st.session_state.finished = True

        st.rerun()

# -----------------------------
# RESULT PAGE
# -----------------------------
else:
    st.balloons()
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your Score: {st.session_state.score}/{len(questions)}")

    if st.session_state.score == len(questions):
        st.success("💯 Excellent!")
    elif st.session_state.score >= 2:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

    if st.button("Restart Quiz"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.finished = False
        st.rerun()
