# 🧠 NeuroCortex-Lab
### A Local AI Intelligence Hub for Adaptive Reasoning, Coding, Research & Automation

---

## 🚀 Overview

NeuroCortex-Lab is a **local AI orchestration engine** designed to unify multiple models, tools, and intelligent routing systems into a single central hub.

It enables:

- Fast experimentation  
- Deep reasoning  
- Model comparison  
- API access  
- Automation  

The lab automatically:

- Understands the **intent**  
- Selects the **best model**  
- Routes intelligently  
- Returns structured high-quality results  

---

## ⚡ Key Features

### 🔀 Intelligent Model Router
- Reasoning → DeepSeek / GPT-4.1 / Claude  
- Coding → Code LLMs  
- Writing → GPT-4.1 / Claude  
- Research → Claude / GPT-4.1  
- Quick tasks → Lightweight models  

### 🌐 Free Temporary Public URL  
Powered by **Cloudflare Tunnel**.

### 💻 Single-Click Launcher
`Jerry.command`:

- Activates venv  
- Starts backend  
- Starts Cloudflare tunnel  
- Shows clean logs  

### 🧪 Developer-First
- Minimal  
- Modular  
- Extensible  

### 🧩 FastAPI Native  
- `/docs` auto documentation  
- JSON schemas  
- Easy to integrate  

---

# 🧬 System Architecture

```
┌──────────────────────────────────────────────┐
│                NeuroCortex-Lab               │
└──────────────────────────────────────────────┘
                    │
                    ▼
    ┌──────────────────────────────────────────┐
    │         Query Intelligence Engine        │
    │ (intent → routing → model selection → QoS) │
    └──────────────────────────────────────────┘
        │        │        │        │        │
        ▼        ▼        ▼        ▼        ▼
   Reasoning   Coding   Writing  Research  Utility
        │        │        │        │        │
        └───────────────► Response Engine ◄──────────────┘
                            │
                            ▼
                    JSON / Text Output
```

---

# 🏗 Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | FastAPI |
| Server | Uvicorn |
| Runtime | Python 3.x |
| Models | OpenAI, Anthropic, DeepSeek, Custom |
| Environment | venv |
| Public Access | Cloudflare Tunnel |
| Docs | Swagger UI (auto) |

---

# 📁 Project Structure

```
NeuroCortex-Lab/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI bootstrap
│   ├── router.py        # Routing logic
│   └── __pycache__/
│
├── requirements.txt
├── Jerry.command
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

### 1. Clone

```
git clone https://github.com/rushikeshzende/NeuroCortex-Lab.git
cd NeuroCortex-Lab
```

### 2. Create Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add API Keys

Create `.env`:

```
OPENAI_API_KEY="your-key"
ANTHROPIC_API_KEY="your-key"
DEEPSEEK_API_KEY="your-key"
```

---

# ▶️ Running the Lab

### Single Click

```
chmod +x Jerry.command
./Jerry.command
```

### Manual

```
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Access:

- Local → http://127.0.0.1:8000  
- Docs → http://127.0.0.1:8000/docs  

---

# 🌐 Cloudflare Tunnel

```
cloudflared tunnel --url http://localhost:8000
```

Generates a temporary HTTPS URL.

---

# 🔌 API Routes

### `GET /health`
System health.

### `POST /query`

```
{
  "query": "Explain attention mechanism",
  "mode": "reasoning"
}
```

### `POST /model/{model_name}`
Force-specific model call.

---

# 🧠 Routing Logic

Analyzes:

- Task type  
- Complexity  
- Length  
- Reasoning depth  
- Code relevance  
- Writing style  

Then selects an optimal model with fallback logic.

---

# 🧩 Extending the Lab

1. Add provider wrapper  
2. Register in router  
3. Optionally add endpoint  

Done in **3–5 minutes**.

---

# 🧱 Roadmap

### Short-Term  
- Chat UI  
- Model comparison  
- Logging dashboard  

### Mid-Term  
- Vector memory  
- RAG integration  

### Long-Term  
- Autonomous agent system  
- Multi-session intelligence  

---

# 📜 License

MIT License  
© 2025 Rushikesh Vasant Zende

---

# 👤 Author

**Rushikesh Vasant Zende**  
AI/ML Engineer • Research • Automation • Developer

