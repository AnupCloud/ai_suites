# OCR Latex Project using Llama3.2-vision and GPT models

A Python-based OCR project to convert the Equation/Formula image to latex code conversion

## 📥 Ollama Setup

1. Install Ollama:
   
   **For macOS:**
   ```bash
   curl https://ollama.ai/install.sh | sh
   ```

   **For Linux:**
   ```bash
   curl https://ollama.ai/install.sh | sh
   ```

   **For Windows:**
   - Download the installer from [Ollama Releases](https://github.com/ollama/ollama/releases)
   - Or use Windows Subsystem for Linux (WSL)

2. Start Ollama Service:
   ```bash
   ollama serve
   ```

3. Pull and Run Models:
   ```bash
   # Pull Llama models
   ollama pull llama2
   ollama pull llama2:3.2
   ollama pull llama2:3.3

   # Pull Mistral
   ollama pull mistral

   # Test a model
   ollama run llama2 "Tell me a joke"
   ```

4. Verify Installation:
   ```bash
   ollama --version
   ```

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnupCloud/ai_suites.git
   cd ai_suites
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
## 📁 File path
[openai:gpt-4o-mini](https://github.com/AnupCloud/ai_suites/blob/main/src/ollama_gpt4o-mini_vision_ocr.py) \
[llama3.2-vision-latest](https://github.com/AnupCloud/ai_suites/blob/main/src/ollama_llama3.2-vision_ocr.py)

## 📸 Image sample
[Data](https://github.com/AnupCloud/ai_suites/blob/main/src/ocr_data/1.jpg)

## ⌛️ Run Command
```bash
streamlit run ../src/ollama_gpt4o-mini_vision_ocr.py
```