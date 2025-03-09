```markdown
# Finance AI Agent Playground

This project demonstrates two intelligent agents built with the Phi framework, which provide financial analysis and web search capabilities using Groq models.

## Overview

The application sets up two agents:
- **Web Search Agent**: Uses DuckDuckGo to perform reliable, up-to-date web searches and returns summarized results with source citations.
- **Finance AI Agent**: Leverages YFinance tools to fetch real-time stock data, analyst recommendations, key financial metrics, recent company news, and detailed company profiles.

Both agents are integrated into a playground app that serves a FastAPI application for interactive use.

## Technologies Used

- **Phi Framework** for building and managing AI agents.
- **Groq Models** (e.g., `llama-3.2-90b-vision-preview`) for processing language and vision tasks.
- **DuckDuckGo Search** for retrieving web data.
- **YFinance API** for financial data.
- **FastAPI & Uvicorn** for serving the web application.
- **Python-dotenv** to manage environment variables (e.g., API keys).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/dhrxv8/finance_ai_agent.git
   cd finance_ai_agent
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root with the following content:

   ```env
   PHI_API_KEY=your_phi_api_key_here
   ```

   **Note:** The `.env` file is ignored by Git (as specified in `.gitignore`), so your API keys remain private.

## Usage

To run the application, execute the following command:

```bash
python playg.py
```

This command will start the Phi Playground app with both agents. The application is served using FastAPI (via Uvicorn), and it will be accessible at the default address provided by the terminal output.

## Project Structure

```
finance_ai_agent/
├── .env                # Environment file (not tracked by Git)
├── .gitignore          # Specifies files/folders to ignore (e.g., .env, venv)
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── playg.py            # Main application script for the Phi Playground
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for improvements or additional features.


## Contact

- **Author:** Dhruv  
- **GitHub:** [dhrxv8](https://github.com/dhrxv8)
```
