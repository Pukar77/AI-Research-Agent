"""FastMCP server instance with registered tools"""
from fastmcp import FastMCP
from backend.src.tools.search_tool import SearchTool
from backend.src.tools.summarize_tool import SummarizeTool
from backend.src.tools.document_tool import DocumentTool

# Initialize FastMCP server
mcp = FastMCP("AI Research Assistant")

# Initialize tools
search_tool = SearchTool()
summarize_tool = SummarizeTool()
document_tool = DocumentTool()


@mcp.tool()
async def search_web(query: str, max_results: int = 5) -> list:
    """
    Search the web using Tavily API
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return (default: 5)
    
    Returns:
        List of search results with title, URL, content, and metadata
    """
    return await search_tool.search_web(query, max_results)


@mcp.tool()
async def summarize_content(title: str, url: str, content: str) -> dict:
    """
    Summarize web content using Groq AI
    
    Args:
        title: Title of the content
        url: Source URL
        content: Content to summarize
    
    Returns:
        Summary with key points and word count
    """
    return await summarize_tool.summarize_content(title, url, content)


@mcp.tool()
async def summarize_search_results(search_results: list) -> list:
    """
    Summarize multiple search results in batch
    
    Args:
        search_results: List of search result dictionaries from search_web tool
    
    Returns:
        List of summaries with key points
    """
    return await summarize_tool.summarize_search_results(search_results)


@mcp.tool()
async def generate_research_document(
    query: str,
    search_results: list,
    summaries: list,
    citation_style: str = "APA"
) -> dict:
    """
    Generate a complete research document with citations
    
    Args:
        query: Original search query
        search_results: List of search results from search_web
        summaries: List of summaries from summarize_search_results
        citation_style: Citation format - "APA" or "MLA" (default: APA)
    
    Returns:
        Complete research document in markdown format with citations
    """
    return await document_tool.generate_document(
        query, search_results, summaries, citation_style
    )


@mcp.tool()
async def create_citation(
    title: str,
    url: str,
    published_date: str = None,
    citation_style: str = "APA"
) -> dict:
    """
    Create a formatted citation for a source
    
    Args:
        title: Title of the source
        url: URL of the source
        published_date: Publication date (optional)
        citation_style: Citation format - "APA" or "MLA" (default: APA)
    
    Returns:
        Formatted citation
    """
    return await document_tool.create_citation(
        title, url, published_date, citation_style
    )


@mcp.tool()
async def research_assistant(query: str, max_results: int = 5, citation_style: str = "APA") -> dict:
    """
    Complete research workflow: search, summarize, and generate document
    
    This is an all-in-one tool that performs the entire research process:
    1. Searches the web using Tavily
    2. Summarizes all results using Groq
    3. Generates a formatted research document with citations
    
    Args:
        query: Research query or topic
        max_results: Number of sources to research (default: 5)
        citation_style: Citation format - "APA" or "MLA" (default: APA)
    
    Returns:
        Complete research document with summaries and citations in markdown
    """
    # Step 1: Search
    search_results = await search_tool.search_web(query, max_results)
    
    if not search_results:
        return {
            "error": "No search results found",
            "query": query
        }
    
    # Step 2: Summarize
    summaries = await summarize_tool.summarize_search_results(search_results)
    
    # Step 3: Generate document
    document = await document_tool.generate_document(
        query, search_results, summaries, citation_style
    )
    
    return document
