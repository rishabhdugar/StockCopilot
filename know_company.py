import streamlit as st
import requests

# Define the API endpoint
api_endpoint = "https://stockcopilotrd2023-batchfunc.azurewebsites.net/api/apiQnA"

# Initialize an empty list to store the history of asked questions
history = []

# Function to add user and AI messages to the conversation
def add_message(role, message):
    history.append((role, message))


if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []
if "just_sent" not in st.session_state:
    st.session_state["just_sent"] = False
if "temp" not in st.session_state:
    st.session_state["temp"] = ""

def clear_text():
    st.session_state["temp"] = st.session_state["input"]
    st.session_state["input"] = ""

def new_chat():
    """
    Clears session state and starts a new chat.
    """
    save = []
    if "generated" not in st.session_state:
        st.session_state["generated"] = []
    if "past" not in st.session_state:
        st.session_state["past"] = []
    if "input" not in st.session_state:
        st.session_state["input"] = ""
    if "stored_session" not in st.session_state:
        st.session_state["stored_session"] = []
    if "just_sent" not in st.session_state:
        st.session_state["just_sent"] = False
    if "temp" not in st.session_state:
        st.session_state["temp"] = ""
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        save.append("User:" + st.session_state["past"][i])
        save.append("Bot:" + st.session_state["generated"][i])        
    st.session_state["stored_session"].append(save)
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["input"] = ""

# Streamlit UI configuration
# st.set_page_config(page_title="Chat UI", layout="wide")

def get_text():
    if "input" not in st.session_state:
        st.session_state["input"] = ""
    """
    Get the user input text.

    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], key="input", 
                            placeholder="Your Stock Copilot assistant here! Ask me anything about companies...", 
                            on_change=clear_text,    
                            label_visibility='hidden')
    input_text = st.session_state["temp"]
    return input_text


new_chat()
def app():
    # Title and description
    st.title("Know Your Company")
    st.write("Ask questions in the chat box below:")

    # Define a placeholder for user input
    user_input = get_text()

    # Display hints at the top of the chat
    st.write("Hints:")
    if st.button("What's the outlook of Microsoft?"):
        user_input = "What's the outlook of Microsoft?"
    
    if st.button("Future Investment by Microsoft News?"):
        user_input = "Future Investment by Microsoft News?"
    
    if st.button("Deepak Nitrite investment plan in chemical? Which chemicals ?"):
        user_input = "Deepak Nitrite investment plan in chemical? Which chemicals ?"
        

    if user_input:
                add_message("User", user_input)
                st.session_state.past.append(user_input)  
                # Make the API call
                response = requests.post(api_endpoint, json={"question": user_input})

                # Extract and display the response
                if response.status_code == 200:
                    ai_response = response.json().get("response", "No response from the API.")
                    
                    st.session_state.generated.append(ai_response) 
                    add_message("AI", ai_response)
                else:
                    add_message("AI", "Error: Failed to get a response from the API.")
                    
                    st.session_state.generated.append("Error: Failed to get a response from the API.") 

                user_input = ""
    # Add a button to send the user's message
    #if st.button("Send"):
        

    download_str = []
    # Display the conversation history using an expander, and allow the user to download it
    with st.expander("Conversation", expanded=True):
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.info(st.session_state["past"][i],icon="🧐")
            st.success(st.session_state["generated"][i], icon="🤖")
            download_str.append(st.session_state["past"][i])
            download_str.append(st.session_state["generated"][i])
                                
        # Can throw error - requires fix
        download_str = '\n'.join(download_str)
        
        if download_str:
            st.download_button('Download',download_str)
    