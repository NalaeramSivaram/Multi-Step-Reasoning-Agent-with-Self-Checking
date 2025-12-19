import streamlit as st
from solver import ReasoningAgent

st.set_page_config(page_title="Ask a Question", layout="centered")

st.title("Ask a Question ❓")

question = st.text_area("Enter your question:", height=150)
st.write("""
         Instructions:
            1. Type your question in the input field.
            2. Press the "Solve" button.
            3. The system will display the computed answer.  """)

if st.button("Solve"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        agent = ReasoningAgent()
        output = agent.solve(question)

        # Store solution in session state
        st.session_state["last_question"] = question
        st.session_state["last_answer"] = output["answer"]
        st.session_state["last_explanation"] = output["reasoning_visible_to_user"]
        st.session_state["last_metadata"] = output["metadata"]

        st.subheader("Final Answer")
        st.success(output["answer"])

        st.info("Go to **Solution Explanation** page to view details.")
