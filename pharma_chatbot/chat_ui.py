import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Pharma AI Assistant", page_icon="💊")

st.title("💊 Pharma AI Assistant")
st.write("Ask questions about medicines and pharmacology.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user input
prompt = st.chat_input("Ask about drugs, side effects, dosage...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(API_URL, json={"question": prompt})

    if response.status_code == 200:
        data = response.json()

        if "response" in data:
            answer = data["response"]
        elif "answer" in data:
            answer = data["answer"]
        else:
            answer = str(data)
    else:
        answer = f"API Error: {response.status_code}"

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})