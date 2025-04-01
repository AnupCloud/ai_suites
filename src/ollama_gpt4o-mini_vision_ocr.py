import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import base64
import aisuite as ai
from config import CREDENTIALS

# Load credentials from environment file
load_dotenv(dotenv_path=CREDENTIALS)

# Initialize AI Suite client
client = ai.Client()

# Page configuration
st.set_page_config(
    page_title="LaTeX OCR with AISuite GPT-4o-mini",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description in main area
st.title("🦙 LaTeX OCR with AISuite GPT models")

# Add clear button to top right
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extract LaTeX code from images using AISuite GPT models!</p>',
            unsafe_allow_html=True)

st.markdown("---")
# Move upload controls to sidebar
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Extract LaTeX 🔍", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    def fetch_latex_response(model: str, image_content: bytes) -> str:
                        """
                        Fetch the LaTeX response for the given model and image content.

                        :param model: The model identifier.
                        :param image_content: The image content in bytes.
                        :return: The LaTeX code extracted by the model.
                        """
                        # Convert binary image data to Base64 string
                        base64_image = base64.b64encode(image_content).decode("utf-8")

                        # Prepare the conversation messages
                        messages = [
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": """Understand the mathematical equation in the provided image and output the corresponding LaTeX code.
                                    Here are some guidelines you MUST follow or you will be penalized:
                                    - NEVER include any additional text or explanations.
                                    - DON'T add dollar signs ($) around the LaTeX code.
                                    - DO NOT extract simplified versions of the equations.
                                    - NEVER add documentclass, packages or begindocument.
                                    - DO NOT explain the symbols used in the equation.
                                    - Output only the LaTeX code corresponding to the mathematical equations in the image."""},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{base64_image}",
                                        },
                                    },
                                ],
                            }
                        ]

                        # Create a completion request
                        response = client.chat.completions.create(
                            model=model,
                            messages=messages,
                            temperature=1,
                        )
                        return response.choices[0].message.content

                    # Fetch response from GPT-4o-mini
                    st.session_state['ocr_result'] = fetch_latex_response("openai:o1", uploaded_file.getvalue())
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")

# Main content area for results
if 'ocr_result' in st.session_state:
    st.markdown("### LaTeX Code")
    st.code(st.session_state['ocr_result'], language='latex')

    st.markdown("### LaTeX Rendered")

    cleaned_latex = st.session_state['ocr_result'].replace(r"\[", "").replace(r"\]", "")
    st.latex(cleaned_latex)

else:
    st.info("Upload an image and click 'Extract LaTeX' to see the results here.")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using AISuite GPT")
