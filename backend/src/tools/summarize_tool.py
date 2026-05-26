"""Groq summarization MCP tool"""
from typing import List
from backend.src.services import GroqService
from backend.src.models.schemas import SearchResult


class SummarizeTool:
    """MCP tool for content summarization using Groq"""
    
    def __init__(self):
        self.groq_service = GroqService()
    
    async def summarize_content(
        self,
        title: str,
        url: str,
        content: str
    ) -> dict:
        """
        Summarize web content
        
        Args:
            title: Title of the content
            url: Source URL
            content: Content to summarize
            
        Returns:
            Summary with key points
        """
        # Create SearchResult object
        search_result = SearchResult(
            title=title,
            url=url,
            content=content,
            score=None,
            published_date=None
        )
        
        # Summarize
        summary = await self.groq_service.summarize(search_result)
        
        return {
            "url": summary.original_url,
            "summary": summary.summary,
            "key_points": summary.key_points,
            "word_count": summary.word_count
        }
    
    async def summarize_search_results(self, search_results: List[dict]) -> List[dict]:
        """
        Summarize multiple search results
        
        Args:
            search_results: List of search result dictionaries
            
        Returns:
            List of summaries
        """
        # Convert dicts to SearchResult objects
        results = [
            SearchResult(
                title=r["title"],
                url=r["url"],
                content=r["content"],
                score=r.get("score"),
                published_date=r.get("published_date")
            )
            for r in search_results
        ]
        
        # Summarize batch
        summaries = await self.groq_service.summarize_batch(results)
        
        return [
            {
                "url": s.original_url,
                "summary": s.summary,
                "key_points": s.key_points,
                "word_count": s.word_count
            }
            for s in summaries
        ]
