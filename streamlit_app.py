import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/ask")  # Default local FastAPI endpoint

# Streamlit page configuration
st.set_page_config(page_title="Agentic AI Chat", page_icon="🤖")
st.title("Agentic AI Chat Interface")
st.write("Ask your AI agent anything!")

# Input box for user query
user_query = st.text_input("Your question:")

# Button to send query
if st.button("Ask Agent"):
    if user_query:
        payload = {"query": user_query}
        try:
            response = requests.post(API_URL, json=payload)
            
            # Ensure FastAPI returns a dict with {"response": ...}
            if response.status_code == 200:
                # response.json() should be a dict
                data = response.json()
                
                # Display the response
                if "response" in data:
                    st.success(data["response"])
                else:
                    st.warning("Unexpected response format from API.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to API: {e}")
