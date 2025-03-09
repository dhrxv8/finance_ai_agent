# Finance AI Agent Playground

A powerful demonstration of intelligent financial analysis and web search capabilities built with the Phi framework and Groq models.

## 🚀 Overview

This project showcases two sophisticated AI agents working together to provide comprehensive financial insights:

- **Web Search Agent** - Performs real-time web searches via DuckDuckGo, delivering summarized results with source citations
- **Finance AI Agent** - Fetches and analyzes stock data through YFinance, providing:
  - Real-time market data
  - Analyst recommendations
  - Key financial metrics
  - Recent company news
  - Detailed company profiles

Both agents are integrated into an interactive playground application built with FastAPI.

## 🛠️ Technologies

- **Phi Framework** - Core infrastructure for agent development and orchestration
- **Groq Models** - State-of-the-art language and vision processing (`llama-3.2-90b-vision-preview`)
- **DuckDuckGo Search** - Web data retrieval with enhanced privacy
- **YFinance API** - Comprehensive financial data access
- **FastAPI & Uvicorn** - Modern, high-performance web application serving
- **Python-dotenv** - Secure environment variable management

## 📋 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhrxv8/finance_ai_agent.git
cd finance_ai_agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your API credentials:

```env
PHI_API_KEY=your_phi_api_key_here
```

> **Security Note**: The `.env` file is excluded from Git tracking (via `.gitignore`) to protect your API keys.

## 🚀 Usage

Launch the application with a single command:

```bash
python playg.py
```

The Phi Playground will start with both agents active. FastAPI (via Uvicorn) will serve the application at the address shown in your terminal.

## 📁 Project Structure

```
finance_ai_agent/
├── .env                # Environment file (not tracked by Git)
├── .gitignore          # Specifies files/folders to ignore
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── playg.py            # Main application script
```

## 👥 Contributing

Contributions are welcome! Please feel free to:
- Submit issues for bugs or feature requests
- Create pull requests with improvements
- Suggest new capabilities for either agent

## 📧 Contact

- **Author:** Dhruv
- **GitHub:** [dhrxv8](https://github.com/dhrxv8)

## 📄 License

[MIT License](LICENSE)
