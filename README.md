# AI Suite Integration Project

A Python-based project that demonstrates integration with multiple AI models through a unified interface using the AI Suite library.

## 🔍 Official Github Page ai-suites[Andrewy NG]
https://github.com/andrewyng/aisuite

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [API Models Supported](#api-models-supported)

## 🔍 Overview

This project provides a unified interface to interact with various AI models including OpenAI, Anthropic's Claude, Google's Gemini, and Ollama models. It demonstrates how to fetch responses from multiple AI models using a consistent API approach.

## 📁 Project Structure

```
ai_suite/
├── src/
│   ├── config.py          # Configuration settings
│   └── main.py           # Main application logic
├── .gitignore           # Git ignore rules
├── .env                 # API credentials
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🛠️ Prerequisites

- Python 3.12.8 or higher
- AI Suite library (`pip install aisuite[all]`)
- Valid API keys for:
  - OpenAI API
  - Anthropic Claude API
  - Google Gemini API
  - Ollama (local installation)

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
   ```

## ⚙️ Configuration

1. Configure your environment variables in `.env`:
   ```env
   ANTHROPIC_API_KEY = "your-anthropic-key"
   OPENAI_API_KEY = "your-openai-key"
   GOOGLE_PROJECT_ID = "your-project-id"
   GOOGLE_REGION = "your-region"
   GOOGLE_APPLICATION_CREDENTIALS = "path/to/credentials.json"
   ```

## 🚀 Usage

The project provides a simple interface to interact with multiple AI models:

1. Import the required modules
2. Initialize the AI Suite client
3. Send prompts to multiple models
4. Receive and process responses

Run the example:
```bash
python src/main.py
```

## ✨ Features

- Unified interface for multiple AI models
- Consistent API approach across different providers
- Easy configuration through environment variables
- Support for both cloud-based and local AI models
- Extensible architecture for adding new models

## 🤖 API Models Supported

1. **OpenAI Models**
   - GPT-4
   - GPT-3.5-turbo
   - GPT-4o
   - GPT-O1

2. **Anthropic Models**
   - Claude 3 Opus
   - Claude 3.5 Sonnet
   - Claude 3.5 Haiku

3. **Google Models**
   - Gemini Pro
   - Gemini Pro Vision
   - Gemini Flash 2.0

4. **Ollama Models**
   - Llama 2, 3.2, 3.3
   - Mistral
   - Custom models

## 🔒 Security

- Never commit your `.env` file containing API keys
- Use environment variables for sensitive information
- Follow security best practices when handling API keys

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AI Suite library developers
- OpenAI team
- Anthropic team
- Google AI team
- Ollama community






