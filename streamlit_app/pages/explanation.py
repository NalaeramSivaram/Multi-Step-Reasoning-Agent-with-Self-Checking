import streamlit as st

st.set_page_config(page_title="Solution Explanation", layout="centered")

st.title("📝 Detailed Explanation")

if "last_question" not in st.session_state:
    st.warning("No previous solution found. Please ask a question first.")
else:
    st.subheader("Question")
    st.write(st.session_state["last_question"])

    st.subheader("Final Answer")
    st.success(st.session_state["last_answer"])

    st.subheader("Explanation (User-visible reasoning)")
    st.write(st.session_state["last_explanation"])

    st.subheader("Verification Metadata")
    st.json(st.session_state["last_metadata"])
