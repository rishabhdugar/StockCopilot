import streamlit as st
import requests

# Define the API endpoint
api_endpoint = "https://stockcopilotrd2023-batchfunc.azurewebsites.net/api/apiQnA"

# Initialize an empty list to store the history of asked questions
history = []

def app():
    st.markdown("## Know About Company")

    # Add a hint at the top
    hint = st.empty()
    hint.markdown("Hint: You can ask questions like 'What is the current stock price?'")

    # Create a sidebar for user input
    st.sidebar.title("Chat")
    message = st.text_input("Enter your message:")
    send_button = st.button("Send")

    # When the send button is clicked, send a POST request to the API
    if send_button:
        response = requests.post(api_endpoint, json={"question": message})

        # Add the asked question to the history
        history.append(message)

        # Display the history of asked questions
        st.markdown("## History of Asked Questions")
        for question in history:
            st.write(question)

        # Display the response from the API in the main page
        if response.status_code == 200:
            # Show only the "response" key from the response
            st.write(response.json()["response"])
        else:
            st.write("Error: ", response.status_code)
            st.write("Error: ", response.json())

        # Update the hint
        hint.markdown("Hint: You can ask another question now.")