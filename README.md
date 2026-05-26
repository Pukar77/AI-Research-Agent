# 🔬 AI Research Assistant

An intelligent research assistant that searches the web, summarizes content using AI, and generates professional research documents with citations.

---

## ✨ Features

- 🔍 **Web Search** - Powered by Tavily API for accurate results
- 📝 **AI Summarization** - Uses Groq LLM to generate concise summaries
- 📚 **Citations** - Automatic APA or MLA citation formatting
- 📄 **Document Generation** - Creates complete research reports in Markdown
- 🎯 **Multiple Interfaces** - CLI, Web UI (Streamlit), and MCP server mode

---

---

## 🚀 Quick Start

### 1. Install Dependencies

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here
MODEL=llama-3.3-70b-versatile
MAX_RESULTS=5
CITATION_STYLE=APA
```

**Get your API keys:**
- Tavily: https://tavily.com
- Groq: https://console.groq.com

---

---

## 🎯 Usage

### Option A: Web Interface (Recommended) 🌐

```bash
streamlit run frontend/app.py
```

Then open: http://localhost:8501

**Features:**
- Beautiful, modern UI
- Real-time progress tracking
- Research history
- Export to multiple formats

### Option B: Command Line Interface 💻

```bash
cd backend
python main.py
```

**Single Query:**
```bash
cd backend
python main.py "artificial intelligence"
```

### Option C: MCP Server Mode 🔌

For integration with Kiro, Claude Desktop, etc.:

```bash
cd backend
python main.py --server
```

---

---

## 🎯 How It Works

1. **Search** - Queries Tavily API for relevant web sources
2. **Summarize** - Uses Groq AI to generate summaries with key points
3. **Generate** - Creates a formatted research document with citations
4. **Export** - Saves results to markdown files

---

---

## 📁 Project Structure

```
ai-research-assistant/
├── frontend/              # Streamlit web interface
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── backend/               # Backend services
│   ├── src/
│   │   ├── server/       # MCP tools
│   │   ├── tools/        # Research tools
│   │   ├── services/     # API integrations
│   │   └── models/       # Data models
│   ├── tests/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── .env                   # API keys
└── README.md
```

---

---

## 🔧 Configuration

Edit `.env` to customize:

```env
# API Keys (required)
TAVILY_API_KEY=your_key
GROQ_API_KEY=your_key

# Model Configuration
MODEL=llama-3.3-70b-versatile

# Search Settings
MAX_RESULTS=5

# Citation Style
CITATION_STYLE=APA
```

**Available Groq Models:**
- `llama-3.3-70b-versatile` (recommended)
- `llama-3.1-70b-versatile`
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

---

---

## 🧪 Testing

Run unit tests:

```bash
cd backend
pytest tests/
```

---

## 📝 Output Format

Research results are saved as markdown files with:

- **Summary of Findings** - AI-generated summaries from each source
- **Key Points** - Bullet-point highlights
- **References** - Properly formatted citations (APA or MLA)

Example: `research_artificial_intelligence.md`

---

---

## 🐛 Troubleshooting

### API Key Errors

Check your `.env` file exists and contains:
```env
TAVILY_API_KEY=tvly-...
GROQ_API_KEY=gsk_...
```

### Module Not Found

Reinstall dependencies:
```bash
cd backend
pip install -r requirements.txt

cd ../frontend
pip install -r requirements.txt
```

### No Results Found

- Check internet connection
- Verify API keys are valid
- Try a different search query

### Port Already in Use

```bash
streamlit run frontend/app.py --server.port 8502
```

---

---

## 📖 Documentation

- **README.md** - Project overview (this file)
- **QUICK_START.md** - Fast installation guide
- **frontend/README.md** - Streamlit frontend guide
- **backend/README.md** - Backend API documentation
- **USAGE.md** - Detailed usage guide

---

## 🎓 Use Cases

- ✅ Academic research with citations
- ✅ Market research and analysis
- ✅ Technical documentation
- ✅ Content research for writing
- ✅ Quick fact-checking
- ✅ Learning and education

---

## 📄 License

MIT License - feel free to use for any purpose.

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io) - Beautiful web interface
- [Tavily](https://tavily.com) - Web search API
- [Groq](https://groq.com) - Fast LLM inference
- [FastMCP](https://github.com/jlowin/fastmcp) - MCP server framework

---

<div align="center">

**Built with ❤️ for researchers, students, and curious minds**

</div>
#
