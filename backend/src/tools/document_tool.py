"""Document generation MCP tool with citations"""
from typing import List
from datetime import datetime
from backend.src.services import CitationService
from backend.src.models.schemas import (
    Document, Summary, Citation, CitationStyle, SearchResult
)
from backend.src.models.config import settings


class DocumentTool:
    """MCP tool for generating research documents with citations"""
    
    def __init__(self):
        self.citation_service = CitationService()
    
    async def generate_document(
        self,
        query: str,
        search_results: List[dict],
        summaries: List[dict],
        citation_style: str = None
    ) -> dict:
        """
        Generate a research document with citations
        
        Args:
            query: Original search query
            search_results: List of search result dictionaries
            summaries: List of summary dictionaries
            citation_style: Citation style (APA or MLA)
            
        Returns:
            Complete research document with markdown format
        """
        # Determine citation style
        if citation_style is None:
            citation_style = settings.citation_style
        
        style = CitationStyle.APA if citation_style.upper() == "APA" else CitationStyle.MLA
        
        # Convert search results to SearchResult objects
        results = [
            SearchResult(
                title=r["title"],
                url=r["url"],
                content=r.get("content", ""),
                score=r.get("score"),
                published_date=r.get("published_date")
            )
            for r in search_results
        ]
        
        # Generate citations
        citations = self.citation_service.format_citations(results, style)
        
        # Convert summaries to Summary objects
        summary_objects = [
            Summary(
                original_url=s["url"],
                summary=s["summary"],
                key_points=s.get("key_points", []),
                word_count=s.get("word_count", 0)
            )
            for s in summaries
        ]
        
        # Create document
        document = Document(
            query=query,
            summaries=summary_objects,
            citations=citations,
            generated_at=datetime.now(),
            total_sources=len(results)
        )
        
        # Convert to markdown
        markdown = document.to_markdown()
        
        return {
            "query": document.query,
            "total_sources": document.total_sources,
            "generated_at": document.generated_at.isoformat(),
            "markdown": markdown,
            "summaries": [
                {
                    "url": s.original_url,
                    "summary": s.summary,
                    "key_points": s.key_points
                }
                for s in document.summaries
            ],
            "citations": [
                {
                    "text": c.text,
                    "style": c.style.value,
                    "url": c.url
                }
                for c in document.citations
            ]
        }
    
    async def create_citation(
        self,
        title: str,
        url: str,
        published_date: str = None,
        citation_style: str = None
    ) -> dict:
        """
        Create a single citation
        
        Args:
            title: Title of the source
            url: URL of the source
            published_date: Publication date (optional)
            citation_style: Citation style (APA or MLA)
            
        Returns:
            Formatted citation
        """
        if citation_style is None:
            citation_style = settings.citation_style
        
        style = CitationStyle.APA if citation_style.upper() == "APA" else CitationStyle.MLA
        
        # Create SearchResult
        result = SearchResult(
            title=title,
            url=url,
            content="",
            published_date=published_date
        )
        
        # Generate citation
        citation = self.citation_service.format_citation(result, style)
        
        return {
            "text": citation.text,
            "style": citation.style.value,
            "url": citation.url
        }
