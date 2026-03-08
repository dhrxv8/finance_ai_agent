# Finance AI Agent

AI-powered financial analysis and web search agent built with the Phi (Agno) framework and Groq's LLaMA model.

## 🚀 Overview

This project features two AI agents working together to provide comprehensive financial insights:

- **Web Search Agent** — Performs real-time web searches via DuckDuckGo, delivering summarized results with source citations
- **Finance AI Agent** — Fetches and analyzes stock data through YFinance, providing:
  - Real-time market data
  - Analyst recommendations
  - Key financial metrics
  - Recent company news
  - Detailed company profiles

Both agents are integrated into an interactive playground application powered by the Phi framework and served via FastAPI.

## ⚙️ How It Works

1. **User query** is submitted through the Phi Playground UI
2. The appropriate agent is invoked — Finance Agent for stock/market queries, Web Search Agent for general research
3. The **Finance Agent** calls YFinance tools to fetch live stock data, fundamentals, and news
4. The **Web Search Agent** queries DuckDuckGo for real-time web results with source citations
5. Both agents generate structured Markdown responses powered by Groq's LLaMA 3.2 model

## 🛠️ Technologies

- **Phi (Agno) Framework** — Core infrastructure for agent development and orchestration
- **Groq LLaMA 3.2** — State-of-the-art language model (`llama-3.2-90b-vision-preview`)
- **DuckDuckGo Search** — Privacy-respecting real-time web data retrieval
- **YFinance API** — Comprehensive financial data access
- **FastAPI & Uvicorn** — High-performance web application serving
- **Python-dotenv** — Secure environment variable management

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

Copy the example environment file and fill in your API credentials:

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```env
PHI_API_KEY=your_phi_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

- Get your **PHI_API_KEY** from [phidata.com](https://www.phidata.com/)
- Get your **GROQ_API_KEY** from [console.groq.com](https://console.groq.com/)

> **Security Note**: The `.env` file is excluded from Git tracking (via `.gitignore`) to protect your API keys.

## ▶️ Usage

Launch the application with a single command:

```bash
python playg.py
```

The Phi Playground will start with both agents active. FastAPI (via Uvicorn) will serve the application at the address shown in your terminal.

## 📁 Project Structure

```
finance_ai_agent/
├── .env                # Environment file (not tracked by Git)
├── .env.example        # Example environment variables template
├── .gitignore          # Specifies files/folders to ignore
├── LICENSE             # MIT License
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

