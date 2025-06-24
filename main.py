import streamlit as st
from langgraph_flow import run_conversation

st.set_page_config(page_title="SmartOps AI", layout="wide")
st.title("🤖 SmartOps AI - Real-Time Strategy Assistant")

query = st.text_input("Enter your business goal or question:")

if st.button("Run SmartOps AI") and query:
    with st.spinner("Analyzing your query..."):
        result = run_conversation(query)
        st.success("Here's your smart strategy!")
        st.write(result)