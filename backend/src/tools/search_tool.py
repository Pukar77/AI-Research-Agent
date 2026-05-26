"""Tavily search MCP tool"""
from typing import List
from backend.src.services import TavilyService
from backend.src.models.schemas import SearchResult


class SearchTool:
    """MCP tool for web search using Tavily"""
    
    def __init__(self):
        self.tavily_service = TavilyService()
    
    async def search_web(self, query: str, max_results: int = 5) -> List[dict]:
        """
        Search the web for information
        
        Args:
            query: Search query string
            max_results: Maximum number of results (default: 5)
            
        Returns:
            List of search results with title, URL, and content
        """
        results = await self.tavily_service.search(query, max_results)
        
        # Convert to dict for MCP response
        return [
            {
                "title": r.title,
                "url": r.url,
                "content": r.content[:500] + "..." if len(r.content) > 500 else r.content,
                "score": r.score,
                "published_date": r.published_date
            }
            for r in results
        ]
