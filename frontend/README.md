# 🔬 AI Research Assistant - Streamlit Frontend

A beautiful **dark-themed** web interface for the AI Research Assistant.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install streamlit
```

Or install from requirements:

```bash
pip install -r frontend/requirements.txt
```

### 2. Run the Frontend

```bash
streamlit run frontend/app.py
```

Or from the frontend directory:

```bash
cd frontend
streamlit run app.py
```

### 3. Open in Browser

The app will automatically open at: `http://localhost:8501`

## ✨ Features

### 🎨 Modern Dark Theme
- Sleek dark interface
- Cyan accent colors
- Compact, efficient design
- Easy on the eyes

### 🔍 Research Tab
- Clean input form
- Quick example buttons
- Compact settings in sidebar

### 📄 Results Tab
- Statistics cards
- Expandable summaries
- Formatted citations
- Compact layout

### 💾 Export Tab
- Markdown preview
- Download buttons (.md, .txt)
- Copy functionality

### 📚 Sidebar
- Adjust research settings
- View research history (last 5)
- Quick access to previous queries
- Compact about section

## 🎨 Design Features

- **Dark Theme**: Easy on the eyes, modern look
- **Compact Layout**: More content, less scrolling
- **Responsive**: Works on desktop and mobile
- **Real-time**: Live updates during research
- **History**: Keep track of previous queries
- **Export**: Multiple export formats
- **Statistics**: Visual metrics and stats

## 🔧 Configuration

The frontend uses the same backend as the CLI:
- Tavily API for web search
- Groq API for summarization
- Same `.env` configuration

### Custom Theme

The dark theme is configured in `frontend/.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#00d4ff"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#1a1d29"
textColor = "#fafafa"
```

## 🐛 Troubleshooting

### "Module not found" error
```bash
# Make sure you're in the project root
cd D:/Websearch-project
streamlit run frontend/app.py
```

### Port already in use
```bash
# Use a different port
streamlit run frontend/app.py --server.port 8502
```

### API key errors
- Check your `.env` file in the project root
- Ensure `TAVILY_API_KEY` and `GROQ_API_KEY` are set

## 🎯 Usage Tips

1. **Start Simple**: Try example queries first
2. **Adjust Sources**: More sources = more comprehensive (but slower)
3. **Use History**: Click previous queries to reload results
4. **Export Early**: Download results before starting new research
5. **Citation Style**: Choose APA for science, MLA for humanities

## 🚀 Advanced

### Custom Port
```bash
streamlit run frontend/app.py --server.port 8080
```

### Custom Host
```bash
streamlit run frontend/app.py --server.address 0.0.0.0
```

### Development Mode
```bash
streamlit run frontend/app.py --server.runOnSave true
```

## 📝 Notes

- Research takes 10-20 seconds depending on sources
- Results are stored in session (cleared on refresh)
- History shows last 5 queries only
- Markdown export includes all formatting
- Dark theme is default (configured in config.toml)

---

**Enjoy researching with a beautiful dark interface! 🔬**
