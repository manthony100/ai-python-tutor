# import streamlit as st
# from openai import OpenAI

# st.set_page_config(page_title="AI Python Tutor", page_icon="📘") # Page title
# st.title("AI Python Tutor")
# # Description
# st.write("A simple tutor for beginner Python topics like variables, loops, functions, and lists.")

# # Client with API Key
# client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": "You are a helpful Python tutor for beginners. Answer clearly and include examples when useful."}
#     ]

# for message in st.session_state.messages[1:]:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# user_input = st.chat_input("Ask a Python question...")

# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     with st.chat_message("assistant"):
#         response_placeholder = st.empty()
#         response_placeholder.markdown("Thinking...")

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=st.session_state.messages
#         )

#         answer = response.choices[0].message.content
#         response_placeholder.markdown(answer)

#     st.session_state.messages.append({"role": "assistant", "content": answer})


# Importing Libraries and Setting up the App UI
    # Imports Streamlit
        # Streamlit - framework to turn data scripts into web apps quickly
    # Imports OpenAI client  
import streamlit as st
from openai import OpenAI # Might have to change to Llama

  
# Create the visual headers and text on my web page
st.set_page_config(page_title="AI Python Tutor", page_icon="📘")
st.title("AI Python Tutor")
st.write("A simple tutor for beginner Python topics like variables, loops, functions, and lists.")

# Connecting the LLM API
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Defining the Tutor's Persona and Memory
if "messages" not in st.session_state:
    # st.session_state acts as the app's memory so it doesn't forget chat history between reruns
    st.session_state.messages = [
        {
            # Initializes the convo with a 'system' role
            # The system prompt tells the AI how to behave
            "role": "system",
            "content": "You are a helpful Python tutor for beginners. Answer clearly and include examples when useful."
        }
    ]

# Display the chat history

# Loops through all saved messages
# Displays them on the screen using Streamlit's built-in chat UI components
for message in st.session_state.messages[1:]: # skips the 1st hidden "system" prompt
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accepting User Input

    # Creates a text box where the user types
user_input = st.chat_input("Ask a Python question...")

    # When the user submits a question
if user_input:
    # It saves the question into the session memory as the user role
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Displays it on the screen
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generating and Displays the AI's Response


    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Thinking...")

        # Sends the entire saved conversation history - st.session_state.messages
        # to the gpt-4o-mini model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        # Extracts the text of Ai's reply
        answer = response.choices[0].message.content
        placeholder.markdown(answer)

# Displays the text on the screen and appends it to the messages list under the assistant role so the AI remembers for the next question
    st.session_state.messages.append({"role": "assistant", "content": answer})

# # Importing Libraries and Setting up the App UI
#     # Imports Streamlit - framework to turn data scripts into web apps quickly
# import streamlit as st

#     # Replaces the OpenAI client with Hugging Face imports
# from transformers import pipeline 
# from huggingface_hub import login 

# # Create the visual headers and text on my web page
# st.set_page_config(page_title="AI Python Tutor", page_icon="📘")
# st.title("AI Python Tutor")
# st.write("A simple tutor for beginner Python topics like variables, loops, functions, and lists.")

# # Connecting the LLM API
#     # Authenticates using the token saved in your .streamlit/secrets.toml file
# login(token=st.secrets["HF_TOKEN"]) 

#     # Initialize the text-generation pipeline with Llama 3.2 
#     # This replaces the OpenAI client initialization
# model_id = "meta-llama/Llama-3.2-1B-Instruct"
# pipe = pipeline("text-generation", model=model_id)

# # Defining the Tutor's Persona and Memory
# if "messages" not in st.session_state:
#     # st.session_state acts as the app's memory so it doesn't forget chat history between reruns
#     st.session_state.messages = [
#         {
#             # Initializes the convo with a 'system' role
#             # The system prompt tells the AI how to behave
#             "role": "system",
#             "content": "You are a helpful Python tutor for beginners. Answer clearly and include examples when useful."
#         }
#     ]

# # Display the chat history
# # Loops through all saved messages and displays them on the screen 
# for message in st.session_state.messages[1:]: # skips the 1st hidden "system" prompt
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accepting User Input
# # Creates a text box where the user types
# user_input = st.chat_input("Ask a Python question...")

# # When the user submits a question
# if user_input:
#     # It saves the question into the session memory as the user role
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     # Displays it on the screen
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Generating and Displays the AI's Response
#     with st.chat_message("assistant"):
#         placeholder = st.empty()
#         placeholder.markdown("Thinking...")

#         # Sends the entire saved conversation history to the Llama 3.2 pipeline
#         # max_length controls how long the generated response can be
#         response = pipe(st.session_state.messages, max_length=1000)

#         # The pipeline returns the entire conversation dictionary. 
#         # This extracts the 'content' of the very last message in the generated list.
#         answer = response["generated_text"][-1]["content"]
        
#         placeholder.markdown(answer)

#     # Displays the text on the screen and appends it to the messages list under the assistant role so the AI remembers for the next question
#     st.session_state.messages.append({"role": "assistant", "content": answer})