
import streamlit as st

from dotenv import load_dotenv

from llm_utils import send_message_to_model
from llm_utils import start_session

load_dotenv()

start_session()

st.title("🍲Sara Dine Chat Assistant🍲")

st.markdown(
    "Serving in Dubai and Sharjah | Free Delivery | Fresh Ingredients | Authentic Flavors"
)

if "messages" not in st.session_state:

    welcome_message = """Hello! Welcome to Sara Dine. How can I assist you today?

You can ask me about our menu or place an order.

Would you like to place an order?"""

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": welcome_message
        }
    ]


for message in st.session_state.messages:

    if message["role"] == "assistant":

        with st.chat_message("assistant"):
            st.markdown(message["content"])

    else:

        with st.chat_message("user"):
            st.markdown(message["content"])


user_input = st.chat_input("Enter your message here...")

if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = send_message_to_model(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
