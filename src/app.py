import os
import sys

#to run the streamlit app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.main import fetch_aisuite_responses

# Set page configuration
st.set_page_config(
    page_title="AI Suite Demo",
    page_icon="🤖",
    layout="wide"
)

# Define available models
AVAILABLE_MODELS = {
    "All Models": [
        "openai:o1",
        "anthropic:claude-3-5-haiku-latest",
        "google:gemini-2.0-flash-exp",
        "ollama:llama3.2"
    ],
    "OpenAI:O1": ["openai:o1"],
    "Claude:claude-3-5-haiku-latest": ["anthropic:claude-3-5-haiku-latest"],
    "Gemini:gemini-2.0-flash-exp": ["google:gemini-2.0-flash-exp"],
    "Ollama:llama3.2": ["ollama:llama3.2"]
}

def main():
    # Title
    st.title("🤖 AI Suite Integration Demo")
    
    # Sidebar
    with st.sidebar:
        st.header("Model Selection")
        selected_model_group = st.selectbox(
            "Choose Model Group",
            options=list(AVAILABLE_MODELS.keys()),
            index=0
        )

    # Main content
    st.subheader("Enter your prompt")
    user_prompt = st.text_area("Type your message here:", height=100)
    
    if st.button("Generate Response", type="primary"):
        if user_prompt:
            try:
                # Show spinner while processing
                with st.spinner("Generating responses..."):
                    # Get selected models
                    models_to_use = AVAILABLE_MODELS[selected_model_group]
                    
                    # Fetch responses
                    responses = fetch_aisuite_responses(models_to_use, user_prompt)
                    
                    # Display responses
                    st.subheader("Responses")
                    for model_name, response in responses:
                        with st.expander(f"Response from {model_name.split(':')[1].upper()}", expanded=True):
                            st.write(response)
                            st.divider()
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a prompt first.")

if __name__ == "__main__":
    main() 