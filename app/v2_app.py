### Streamlit App Main File##
import streamlit as st
from v2_qna import query_response
from time import sleep


#### Streamlit App ####
st.set_page_config(page_title='Ocean Breeze Resort', page_icon='🛌', layout="centered", initial_sidebar_state="collapsed", menu_items=None)

with st.sidebar:
    st.markdown('### **About**')
    st.info('This is a conversational demo chatbot built using ***LangChain and Streamlit.***')
    st.info("It is based on the **FAKE** hotel ***Ocean Breeze Resort*** data to answer user questions.")
    st.info('Data was ***synthetically generated using Gen AI models*** for the demo purpose.')
    st.divider()
    st.success('Created by: Manish Sharma 🤖')


st.markdown(f"## **🌴 Ocean Breeze Resort ChatBot App**")
st.info('🛌 ***Stay. 🏊 Float.. 🏆 Refresh...***')

if "messages" not in st.session_state:
    st.session_state.messages = []

    # adding the first default chatbot message as a welcome to the user
    ai_message = {"role": "assistant", "content": "👋 Hello! I am Ocean Breeze Resort ChatBot. How can I help you?"}
    st.session_state.messages.append(ai_message)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Ask Me!")
if prompt:

    st.chat_message("user").markdown(prompt)
    user_message = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking!"):

            sleep(1)
            response = query_response(prompt)                   # Stream Chat Function Call

        placeholder = st.empty()
        full_response = ""
        for chunk in response:
            full_response += chunk
            placeholder.markdown(full_response + "▌")
            sleep(0.1)

        placeholder.markdown(full_response)

        ai_message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(ai_message)
