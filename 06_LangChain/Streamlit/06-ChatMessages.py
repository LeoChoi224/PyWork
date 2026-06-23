import streamlit as st
import time

# Chat elements
#  공식] https://docs.streamlit.io/develop/api-reference/chat

st.set_page_config(
    page_title="ChatMessages",
    page_icon="👀",
)

st.title("Chat Messages")

# session_state 는 여러번 재실행해도 data 가 보존될수 있도록 해준다.
#   보존되는 데이터는 key-value 형태로 session에 저장됨

if "messages" not in st.session_state:
    st.session_state['messages'] = []

message = st.chat_input(placeholder="Send a message to AI")

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state['messages'].append({"message": message, "role": role})


for msg in st.session_state['messages']:
    send_message(msg['message'], msg['role'], save=False)


if message:
    send_message(message, 'human')  # save=True
    time.sleep(2)
    send_message(f"You said: {message}", "ai")

















# with st.status("Embedding file..."):
#     time.sleep(3)
#     st.write("Getting the file")
#     time.sleep(3)
#     st.write("Embedding the file")
#     time.sleep(3)
#     st.write("Caching the file")

# with st.status("Embedding file...", expanded=True) as status:
#     time.sleep(3)
#     st.write("Getting the file")
#     time.sleep(3)
#     st.write("Embedding the file")
#     time.sleep(3)
#     st.write("Caching the file")
#     # status.update(label='Error', state='error')
#     status.update(label='완료', state='complete')

