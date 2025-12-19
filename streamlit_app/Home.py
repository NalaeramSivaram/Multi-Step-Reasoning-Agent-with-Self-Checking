import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from solver import ReasoningAgent

st.set_page_config(page_title="Reasoning Agent - Home", layout="centered")


# -------------- BACKGROUND IMAGE CSS ---------------- #
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://seatons.co.uk/wp-content/uploads/2023/03/Why-Use-A-Solicitor-For-Probate-Seatons-Law-1024x538.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}
</style>
"""
# -------------- TEXT COLOR FIX ---------------- #
text_color_css = """
<style>
/* Main text */
html, body, [data-testid="stAppViewContainer"] * {
    color: black !important;
}

/* Input text area text color */
textarea, input {
    color: black !important;
}
</style>
"""

st.markdown(text_color_css, unsafe_allow_html=True)


st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("🧠 Multi-Step Reasoning Agent")
st.subheader("Planner → Executor → Verifier")

st.write("""
This application demonstrates a multi-step reasoning agent that solves structured problems using:
- A **Planner** that creates a step-by-step plan  
- An **Executor** that follows the plan  
- A **Verifier** that re-checks the answer  

Use the page menu (left sidebar) to navigate between:
1. **Home** — overview + sample questions  
2. **Ask Question** — enter your question  
3. **Solution Explanation** — view explanation for the last solved problem
""")

st.divider()

# -------- Sample examples --------
with st.expander(" 📘 Sample Questions & Answers "):
    st.write(" Below are some sample questions and the final answers computed by the reasoning agent.")

    agent = ReasoningAgent()
    
    example_questions = [
        "If a train leaves at 14:30 and arrives at 18:05, how long is the journey?",
        "Alice has 3 red apples and twice as many green apples. Total apples?",
        "What is the time difference between 09:00 and 10:45?",
        "If a meeting needs 60 minutes and free slots are 09:00–09:30, 10:00–11:00, which slot fits?",
        "Alice has 5 red apples and twice as many green apples. Total apples?",
        "Find the duration between 13:10 and 14:00.",
        "A train starts at 08:15 and ends at 09:00. Travel time?",
        "Person has 4 red apples and twice green apples. Total?",
        "Duration between 07:30 and 08:45?",
        "If a meeting lasts 30 minutes, will it fit into 14:00–14:20?"
        ]
    for q in example_questions:
        result = agent.solve(q)
        st.markdown(f"### Sample Question: {q}")
        st.markdown(f"**Answer:** {result['answer']}")
        st.markdown("---")
