"""
AI Research Assistant - Streamlit Frontend
A beautiful web interface for the AI Research Assistant
"""
import streamlit as st
import sys
import os
import asyncio
from datetime import datetime

# Add parent directory to path to import from backend
# Get the project root directory (parent of frontend)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from backend.src.server.app import research_assistant

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS - Light Theme
st.markdown("""
<style>
    /* Light theme colors */
    :root {
        --bg-primary: #ffffff;
        --bg-secondary: #f8f9fa;
        --bg-tertiary: #e9ecef;
        --text-primary: #212529;
        --text-secondary: #6c757d;
        --accent-primary: #0d6efd;
        --accent-secondary: #0a58ca;
        --border-color: #dee2e6;
        --success-color: #198754;
    }
    
    /* Main background */
    .stApp {
        background-color: var(--bg-primary);
    }
    
    /* Compact header */
    .main-header {
        font-size: 1.3rem;
        font-weight: 600;
        text-align: center;
        color: var(--accent-primary);
        margin-bottom: 0.2rem;
        padding: 0.2rem 0;
    }
    
    .sub-header {
        text-align: center;
        color: var(--text-secondary);
        margin-bottom: 0.8rem;
        font-size: 0.75rem;
    }
    
    /* Compact buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        color: white;
        font-weight: 600;
        padding: 0.4rem 0.8rem;
        border-radius: 0.4rem;
        border: none;
        font-size: 0.85rem;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 3px 8px rgba(13, 110, 253, 0.25);
    }
    
    /* Compact cards */
    .research-card {
        background-color: var(--bg-secondary);
        padding: 0.8rem;
        border-radius: 0.4rem;
        margin-bottom: 0.6rem;
        border: 1px solid var(--border-color);
    }
    
    .source-card {
        background-color: var(--bg-secondary);
        padding: 0.7rem;
        border-radius: 0.4rem;
        border-left: 3px solid var(--accent-primary);
        margin-bottom: 0.6rem;
    }
    
    .citation-card {
        background-color: var(--bg-secondary);
        padding: 0.6rem;
        border-radius: 0.3rem;
        margin-bottom: 0.4rem;
        font-size: 0.8rem;
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
    }
    
    /* Compact stats box */
    .stats-box {
        background: var(--bg-secondary);
        padding: 0.6rem;
        border-radius: 0.4rem;
        text-align: center;
        border: 1px solid var(--border-color);
    }
    
    /* Compact inputs */
    .stTextInput>div>div>input {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        border-radius: 0.4rem;
        padding: 0.5rem;
        font-size: 0.85rem;
    }
    
    /* Compact selectbox */
    .stSelectbox>div>div>div {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        font-size: 0.85rem;
    }
    
    /* Compact tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.4rem;
        background-color: var(--bg-secondary);
        padding: 0.4rem;
        border-radius: 0.4rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.4rem 0.8rem;
        font-size: 0.85rem;
        background-color: var(--bg-primary);
        border-radius: 0.3rem;
        color: var(--text-secondary);
        border: 1px solid var(--border-color);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        color: white;
        border: none;
    }
    
    /* Compact expander */
    .streamlit-expanderHeader {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 0.4rem;
        padding: 0.5rem;
        font-size: 0.85rem;
    }
    
    /* Compact metrics */
    [data-testid="stMetricValue"] {
        font-size: 1.3rem;
        color: var(--accent-primary);
        font-weight: 600;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem;
        color: var(--text-secondary);
    }
    
    /* Compact sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--bg-secondary);
        padding: 0.8rem 0.6rem;
    }
    
    /* Compact divider */
    hr {
        margin: 0.8rem 0;
        border-color: var(--border-color);
    }
    
    /* Compact code blocks */
    .stCodeBlock {
        font-size: 0.8rem;
    }
    
    /* Reduce spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 900px;
    }
    
    /* Remove fixed header */
    header[data-testid="stHeader"] {
        position: relative;
        background: transparent;
    }
    
    /* Hide streamlit default header */
    header[data-testid="stHeader"] {
        display: none;
    }
    
    /* Compact download button */
    .stDownloadButton>button {
        background-color: var(--bg-primary);
        color: var(--accent-primary);
        border: 1px solid var(--accent-primary);
        padding: 0.4rem 0.8rem;
        font-size: 0.85rem;
    }
    
    .stDownloadButton>button:hover {
        background-color: var(--accent-primary);
        color: white;
    }
    
    /* Smaller icons */
    .stTabs [data-baseweb="tab"] svg {
        width: 14px;
        height: 14px;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
    }
    
    h3 {
        font-size: 1.1rem;
        margin-bottom: 0.6rem;
    }
    
    h4 {
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    h5 {
        font-size: 0.9rem;
        margin-bottom: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'research_history' not in st.session_state:
    st.session_state.research_history = []
if 'current_result' not in st.session_state:
    st.session_state.current_result = None

# Compact Header
st.markdown('<div class="main-header">🔍 AI Research Assistant With Standard Citation</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Tavily Search • Groq AI • Smart Citations</div>', unsafe_allow_html=True)

# Compact Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # Research settings
    max_results = st.slider(
        "Sources",
        min_value=1,
        max_value=10,
        value=5,
        help="Number of web sources"
    )
    
    citation_style = st.selectbox(
        "Citation",
        options=["APA", "MLA"],
        help="Citation format"
    )
    
    st.divider()
    
    # Research history
    st.markdown("### 📚 History")
    if st.session_state.research_history:
        for idx, item in enumerate(reversed(st.session_state.research_history[-5:])):
            if st.button(f"📝 {item['query'][:25]}...", key=f"history_{idx}"):
                st.session_state.current_result = item['result']
                st.rerun()
    else:
        st.caption("No history yet")
    
    st.divider()
    
    # About
    st.markdown("### ℹ️ About")
    st.caption("""
    🔍 Tavily Search  
    🤖 Groq AI  
    📚 Citations  
    📄 Export
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["🔍 Research", "📊 Results", "💾 Export"])

with tab1:
    st.markdown("### 🔍 Start Research")
    
    # Research form
    with st.form("research_form"):
        query = st.text_input(
            "Query",
            placeholder="e.g., What is artificial intelligence?",
            help="Enter your research topic",
            label_visibility="collapsed"
        )
        
        submit_button = st.form_submit_button("🔍 Start Research", use_container_width=True)
    
    # Process research
    if submit_button and query:
        with st.spinner(f"🔍 Researching '{query}'... This may take 10-20 seconds..."):
            try:
                # Run async function
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(
                    research_assistant(
                        query=query,
                        max_results=max_results,
                        citation_style=citation_style
                    )
                )
                loop.close()
                
                # Check for errors
                if "error" in result:
                    st.error(f"❌ {result['error']}")
                else:
                    # Store in session state
                    st.session_state.current_result = result
                    st.session_state.research_history.append({
                        'query': query,
                        'result': result,
                        'timestamp': datetime.now()
                    })
                    st.success("✅ Research completed!")
                    st.rerun()
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Quick examples
    st.divider()
    st.markdown("##### 💡 Examples")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("AI", use_container_width=True):
            st.session_state.example_query = "What is artificial intelligence?"
            st.rerun()
    
    with col2:
        if st.button("Quantum", use_container_width=True):
            st.session_state.example_query = "What is quantum computing?"
            st.rerun()
    
    with col3:
        if st.button("CRISPR", use_container_width=True):
            st.session_state.example_query = "What is CRISPR gene editing?"
            st.rerun()

with tab2:
    st.markdown("### 📊 Results")
    
    if st.session_state.current_result:
        result = st.session_state.current_result
        
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="stats-box">', unsafe_allow_html=True)
            st.metric("Sources", result.get('total_sources', 0))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="stats-box">', unsafe_allow_html=True)
            st.metric("Summaries", len(result.get('summaries', [])))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="stats-box">', unsafe_allow_html=True)
            st.metric("Citations", len(result.get('citations', [])))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="stats-box">', unsafe_allow_html=True)
            st.metric("Query", result.get('query', 'N/A')[:15] + "...")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Summaries
        st.markdown("#### 📝 Summaries")
        
        for idx, summary in enumerate(result.get('summaries', []), 1):
            with st.expander(f"Source {idx}", expanded=(idx == 1)):
                st.caption(summary.get('url', 'Unknown'))
                st.write(summary.get('summary', 'No summary available'))
                
                if summary.get('key_points'):
                    st.markdown("**Key Points:**")
                    for point in summary['key_points']:
                        st.markdown(f"• {point}")
                
                st.markdown(f"[🔗 View Source]({summary.get('url', '#')})")
        
        st.divider()
        
        # Citations
        st.markdown("#### 📚 References")
        
        for idx, citation in enumerate(result.get('citations', []), 1):
            st.markdown(f'<div class="citation-card">{idx}. {citation.get("text", "")}</div>', unsafe_allow_html=True)
    
    else:
        st.info("👈 Start a research query to see results here")

with tab3:
    st.markdown("### 💾 Export")
    
    if st.session_state.current_result:
        result = st.session_state.current_result
        
        # Markdown preview
        st.markdown("#### 📄 Document")
        
        markdown_content = result.get('markdown', 'No content available')
        
        # Display markdown
        with st.expander("Preview", expanded=False):
            st.markdown(markdown_content)
        
        # Download buttons
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="📥 Markdown",
                data=markdown_content,
                file_name=f"research_{result.get('query', 'document').replace(' ', '_')[:30]}.md",
                mime="text/markdown",
                use_container_width=True
            )
        
        with col2:
            # Create plain text version
            plain_text = markdown_content.replace('#', '').replace('*', '').replace('-', '•')
            st.download_button(
                label="📥 Text",
                data=plain_text,
                file_name=f"research_{result.get('query', 'document').replace(' ', '_')[:30]}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        st.divider()
        
        # Copy to clipboard
        st.markdown("#### 📋 Copy")
        with st.expander("View Code", expanded=False):
            st.code(markdown_content, language="markdown")
        
    else:
        st.info("👈 Complete a research query to export results")

# Compact Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: var(--text-secondary); padding: 0.5rem; font-size: 0.8rem;">
    Built with Streamlit • Tavily • Groq
</div>
""", unsafe_allow_html=True)
