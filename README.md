# Finance AI Agent (Phi/Agno + Groq + YFinance + DuckDuckGo)

AI-powered financial analysis agent built with the **Phi (Agno) framework**.  
It combines:
- **Market data + company info/news** via **YFinance**
- **Web search** via **DuckDuckGo**
- A **Groq-hosted LLaMA model** to generate structured, readable financial analysis

> Repo description: AI-powered financial analysis agent using Groq LLaMA, YFinance, and DuckDuckGo - built with the Phi (Agno) framework

---

## What this project does

This project provides a small “agent playground” with two agents:

1. **Finance AI Agent**
   - Pulls: stock price, fundamentals, analyst recommendations, company info, company news
   - Formats output cleanly (tables / sections)
   - Adds a timestamp instruction for relevance

2. **Web Search Agent**
   - Uses DuckDuckGo to find up-to-date information
   - Instructed to cross-check sources and cite links in responses

---

## Tech stack

- **Framework:** Phi (Agno) (`phidata`)
- **LLM Provider:** Groq
- **Model:** `llama-3.2-90b-vision-preview` (as configured in `playg.py`)
- **Tools:**
  - `YFinanceTools` (stock data, fundamentals, recommendations, news)
  - `DuckDuckGo` (web search)
- **App runner / UI:** Phi Playground served as a FastAPI app (via `serve_playground_app`)
- **Runtime:** `uvicorn`

---

## Project structure

- `playg.py` — defines the two agents + starts the Playground app
- `.env.example` — environment variables template
- `requirements.txt` — dependencies
- `LICENSE` — MIT

---

## Setup (local)

### 1) Clone
```bash
git clone https://github.com/dhrxv8/finance_ai_agent.git
cd finance_ai_agent
```

### 2) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

`.env` should include:
- `PHI_API_KEY` (Phi/Agno platform key)
- `GROQ_API_KEY` (Groq API key)

> Note: `playg.py` calls `load_dotenv()`, so `.env` is loaded automatically.

### 5) Run the Playground app
```bash
python playg.py
```

Then open the local URL printed in your terminal (served via `uvicorn`).

---

## How it works (based on the code)

- The app loads env vars using `python-dotenv`
- It creates:
  - `web_search_agent` using `DuckDuckGo()`
  - `finance_agent` using `YFinanceTools(...)`
- Both agents use Groq as the model backend
- A Phi `Playground` is created with both agents and served via:
  ```py
  serve_playground_app("playg:app", reload=True)
  ```

---

## Notes / limitations

- Financial outputs depend on data availability from Yahoo Finance and may vary by ticker/region.
- Web results can change over time; always verify critical information.
- This is not financial advice — intended for educational/demo use.

---

## License

MIT (see `LICENSE`).
