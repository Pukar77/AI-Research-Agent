"""Pydantic data schemas for the AI Research Assistant"""
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class CitationStyle(str, Enum):
    """Citation format styles"""
    APA = "APA"
    MLA = "MLA"


class SearchResult(BaseModel):
    """Individual search result from Tavily"""
    title: str = Field(..., description="Title of the webpage")
    url: str = Field(..., description="URL of the webpage")
    content: str = Field(..., description="Extracted content from the webpage")
    score: Optional[float] = Field(None, description="Relevance score")
    published_date: Optional[str] = Field(None, description="Publication date if available")


class Summary(BaseModel):
    """Summarized content from Groq"""
    original_url: str = Field(..., description="Source URL")
    summary: str = Field(..., description="AI-generated summary")
    key_points: List[str] = Field(default_factory=list, description="Key takeaways")
    word_count: int = Field(..., description="Summary word count")


class Citation(BaseModel):
    """Formatted citation"""
    text: str = Field(..., description="Formatted citation text")
    style: CitationStyle = Field(..., description="Citation style used")
    url: str = Field(..., description="Source URL")


class Document(BaseModel):
    """Final research document with citations"""
    query: str = Field(..., description="Original search query")
    summaries: List[Summary] = Field(..., description="Summarized content from sources")
    citations: List[Citation] = Field(..., description="Formatted citations")
    generated_at: datetime = Field(default_factory=datetime.now, description="Document creation timestamp")
    total_sources: int = Field(..., description="Number of sources used")
    
    def to_markdown(self) -> str:
        """Convert document to markdown format"""
        md = f"# Research Report: {self.query}\n\n"
        md += f"*Generated on: {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        md += f"**Total Sources:** {self.total_sources}\n\n"
        md += "---\n\n"
        
        # Add summaries
        md += "## Summary of Findings\n\n"
        for idx, summary in enumerate(self.summaries, 1):
            md += f"### Source {idx}\n\n"
            md += f"{summary.summary}\n\n"
            
            if summary.key_points:
                md += "**Key Points:**\n"
                for point in summary.key_points:
                    md += f"- {point}\n"
                md += "\n"
            
            md += f"*Source: [{summary.original_url}]({summary.original_url})*\n\n"
            md += "---\n\n"
        
        # Add citations
        md += "## References\n\n"
        for idx, citation in enumerate(self.citations, 1):
            md += f"{idx}. {citation.text}\n\n"
        
        return md
