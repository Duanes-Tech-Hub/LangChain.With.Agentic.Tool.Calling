# LangChain with Agentic Tool Calling : AI-Powered Contact Management & Search Assistant

The purpose of this project was to test agentic tool calling based on the task assignment. This code will serve as a basis for an AI helper to take tasks and interact with the users contact list. The goal is for an intelligent AI assistant that combines contact management, email automation, and web search capabilities using Google's Gemini AI and LangChain framework. The channels for interaction with this agent will be via Telgram messages and APIs.

## 📋 Table of Contents

- [💡 About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [💻 Technologies Used](#-technologies-used)
- [🛠️ Installation & Setup](#️-installation--setup)
- [▶️ Running Locally](#️-running-locally)
- [🧪 Testing](#-testing)
- [📌 Project Status](#-project-status)
- [🗺️ Future Roadmap](#-future-roadmap)

## 💡 About The Project

This project demonstrates the power of combining **Large Language Models (LLMs)** with **structured tool calling** to create an intelligent assistant capable of:

- **Problem Solved**: Managing contact information and automating email communications while providing intelligent web search capabilities
- **Real-world Application**: A virtual assistant that can look up contacts, send emails, and research information - perfect for business automation and personal productivity
- **Key Learning**: Mastered **LangChain's agent framework** and **Google Gemini's function calling** capabilities to create a multi-tool AI system with proper error handling and structured outputs

The assistant showcases **critical thinking** by validating contact information before attempting actions and **problem-solving** by gracefully handling failures and providing meaningful feedback to users.

## ✨ Key Features

- 🔍 **Intelligent Contact Lookup**: Search for contacts with structured validation
- 📧 **Automated Email System**: Send emails to found contacts with custom subjects and body content
- 🌐 **Web Search Integration**: Research information using Tavily search API
- 🛡️ **Error Handling**: Robust validation prevents actions on missing contacts
- 🧠 **AI-Powered Reasoning**: Google Gemini 2.5 Flash provides intelligent decision-making
- 📊 **Structured Outputs**: Pydantic models ensure type-safe data handling
- 🔄 **Streaming Responses**: Real-time agent updates for better user experience

## 💻 Technologies Used

### Core Technologies
- **Python 3.8+** - Primary programming language
- **Google Gemini 2.5 Flash** - Advanced LLM for AI reasoning
- **LangChain** - Framework for building LLM applications
- **Pydantic** - Data validation and settings management

### APIs & Services
- **Google Generative AI** - Gemini model integration
- **Tavily Search API** - Web search functionality

### Development Tools
- **python-dotenv** - Environment variable management
- **Git** - Version control system
- **VS Code/PyCharm** - IDE support

### Key Concepts Demonstrated
- **Agent-Based Architecture**
- **Function Calling & Tool Integration**
- **Structured Output Validation**
- **Error Handling & Graceful Failures**
- **Streaming AI Responses**
- **CRUD Operations** (Contact management)
- **RESTful API Integration**

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Gemini API key
- Tavily Search API key

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-contact-assistant.git
   cd ai-contact-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

5. **Get API Keys**
   - [Google Gemini API Key](https://makersuite.google.com/app/apikey)
   - [Tavily Search API Key](https://app.tavily.com/)

## ▶️ Running Locally

### Basic Usage

1. **Activate your virtual environment**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the main application**
   ```bash
   python main.py
   ```

3. **Expected Output**: The agent will process the automotive repair query and display streaming responses from the AI assistant.

### Available Test Cases

The application includes several test scenarios:
- **Automotive Repair Query**: Research brake replacement for Ford Fusion 2012
- **Contact Lookup**: Find and email contacts (Alice/Bob)
- **Error Handling**: Demonstrates graceful failure for unknown contacts

### Custom Usage

Modify the `inputs_success` variable in `main.py` to test your own queries:
```python
inputs_success = {"messages": [{"role": "user", "content": "Your custom query here"}]}
```

## 🧪 Testing

### Running Tests

Currently, the project uses manual testing through the main execution block. Future versions will include:

```bash
# Planned test commands
python -m pytest tests/
python -m unittest discover tests/
```

### Test Framework Integration

- **Unit Testing**: Planned with pytest
- **Integration Testing**: Agent workflow validation
- **API Testing**: Tool function verification
- **Error Handling Tests**: Edge case validation

### Manual Testing Examples

The main.py file includes comprehensive test cases that demonstrate:
- ✅ Successful contact lookup and email sending
- ❌ Graceful handling of missing contacts
- 🔍 Complex web search queries with automotive data

## 📌 Project Status

**🟢 Active Development** - Version 1.0 Core Features Complete

- ✅ Core agent functionality implemented
- ✅ Contact lookup system with validation
- ✅ Email automation with error handling
- ✅ Web search integration
- ✅ Structured output handling


## 🗺️ Future Roadmap

This code will serve as a building block for other projects. The tooling structure used here will be
used to build a more capable LLM integration that has long term memory for conversations. Also Telegram
and API channel will be integrated for triggering access to the LLM along with structured output.
The current output was to validate tool choosing based on task received.

### Technologies & Resources
- Built with [LangChain](https://langchain.com) - Amazing LLM framework
- Powered by [Google Gemini](https://ai.google.dev/) - Advanced AI model
- Search functionality by [Tavily](https://tavily.com/) - AI-powered search

### Learning Resources
- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API Guide](https://ai.google.dev/tutorials)
- [Pydantic Documentation](https://docs.pydantic.dev/)

<div align="center">

**⭐ Star this repository if you found it helpful!**

*Built with ❤️ using Python, LangChain, and Google Gemini*

</div>