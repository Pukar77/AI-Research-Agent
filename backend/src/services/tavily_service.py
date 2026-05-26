"""Tavily API integration for web search"""
from typing import List
from tavily import TavilyClient
from backend.src.models.schemas import SearchResult
from backend.src.models.config import settings


class TavilyService:
    """Service for interacting with Tavily search API"""
    
    def __init__(self):
        """Initialize Tavily client"""
        self.client = TavilyClient(api_key=settings.tavily_api_key)
    
    async def search(self, query: str, max_results: int = None) -> List[SearchResult]:
        """
        Search the web using Tavily
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of SearchResult objects
        """
        if max_results is None:
            max_results = settings.max_results
        
        try:
            # Perform search with content extraction
            response = self.client.search(
                query=query,
                max_results=max_results,
                search_depth="advanced",
                include_raw_content=False,
                include_answer=False
            )
            
            # Parse results
            results = []
            for result in response.get("results", []):
                search_result = SearchResult(
                    title=result.get("title", ""),
                    url=result.get("url", ""),
                    content=result.get("content", ""),
                    score=result.get("score"),
                    published_date=result.get("published_date")
                )
                results.append(search_result)
            
            return results
            
        except Exception as e:
            raise Exception(f"Tavily search failed: {str(e)}")
    
    async def extract_content(self, url: str) -> str:
        """
        Extract content from a specific URL
        
        Args:
            url: URL to extract content from
            
        Returns:
            Extracted text content
        """
        try:
            response = self.client.extract(urls=[url])
            if response and len(response.get("results", [])) > 0:
                return response["results"][0].get("raw_content", "")
            return ""
        except Exception as e:
            raise Exception(f"Content extraction failed: {str(e)}")
