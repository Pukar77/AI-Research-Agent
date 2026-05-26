# 🔬 AI Research Assistant - Backend

Backend services for the AI Research Assistant using Tavily and Groq APIs.

## 📁 Structure

```
backend/
├── src/
│   ├── server/          # MCP server and tools
│   ├── services/        # API integrations (Tavily, Groq, Citations)
│   ├── models/          # Data schemas and config
│   └── tools/           # Research tools
├── tests/               # Unit tests
├── main.py              # Entry point (CLI & MCP server)
├── requirements.txt     # Python dependencies
└── pyproject.toml       # Project configuration
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_key_here
GROQ_API_KEY=your_groq_key_here
```

### 3. Run CLI Mode

```bash
python main.py
```

### 4. Run MCP Server Mode

```bash
python main.py --server
```

## 🔧 Features

- **Tavily Search**: Web search with content extraction
- **Groq AI**: LLM-powered summarization (llama-3.3-70b-versatile)
- **Citations**: APA and MLA format support
- **MCP Server**: Model Context Protocol integration
- **Async Operations**: Fast parallel processing

## 📚 API Services

### TavilyService
- Web search with configurable results
- Content extraction and parsing

### GroqService
- AI-powered summarization
- Key points extraction
- Batch processing support

### CitationService
- APA format citations
- MLA format citations
- Automatic metadata extraction

## 🧪 Testing

```bash
cd backend
pytest tests/
```

## 📖 Usage

### CLI Mode
```bash
python main.py
# Enter your research query when prompted
```

### MCP Server Mode
```bash
python main.py --server
# Connect with Claude Desktop or other MCP clients
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TAVILY_API_KEY` | Tavily API key | Yes |
| `GROQ_API_KEY` | Groq API key | Yes |
| `GROQ_MODEL` | Groq model name | No (default: llama-3.3-70b-versatile) |
| `MAX_RESULTS` | Max search results | No (default: 5) |

## 🛠️ Development

### Project Structure

- `src/server/app.py` - MCP server with tool definitions
- `src/services/` - External API integrations
- `src/tools/` - Research workflow tools
- `src/models/` - Pydantic schemas and settings

### Adding New Features

1. Add service in `src/services/`
2. Create tool in `src/tools/`
3. Register tool in `src/server/app.py`
4. Add tests in `tests/`

---

**Built with FastMCP, Tavily, and Groq** 🚀
