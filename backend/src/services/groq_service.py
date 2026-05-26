"""Groq API integration for content summarization"""
from typing import List
from groq import Groq
from backend.src.models.schemas import Summary, SearchResult
from backend.src.models.config import settings


class GroqService:
    """Service for interacting with Groq LLM API"""
    
    def __init__(self):
        """Initialize Groq client"""
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.model
    
    async def summarize(self, search_result: SearchResult) -> Summary:
        """
        Summarize content from a search result
        
        Args:
            search_result: SearchResult object containing content to summarize
            
        Returns:
            Summary object with summarized content and key points
        """
        try:
            # Create prompt for summarization
            prompt = f"""Analyze and summarize the following content from "{search_result.title}":

{search_result.content}

Provide:
1. A concise summary (2-3 paragraphs)
2. 3-5 key points or takeaways

Format your response as:
SUMMARY:
[Your summary here]

KEY POINTS:
- [Point 1]
- [Point 2]
- [Point 3]
"""
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional research assistant. Provide clear, concise, and accurate summaries of web content."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            # Parse response
            content = response.choices[0].message.content
            summary_text, key_points = self._parse_response(content)
            
            return Summary(
                original_url=search_result.url,
                summary=summary_text,
                key_points=key_points,
                word_count=len(summary_text.split())
            )
            
        except Exception as e:
            raise Exception(f"Groq summarization failed: {str(e)}")
    
    def _parse_response(self, content: str) -> tuple[str, List[str]]:
        """
        Parse Groq response to extract summary and key points
        
        Args:
            content: Raw response from Groq
            
        Returns:
            Tuple of (summary_text, key_points_list)
        """
        summary_text = ""
        key_points = []
        
        # Split by sections
        if "SUMMARY:" in content and "KEY POINTS:" in content:
            parts = content.split("KEY POINTS:")
            summary_text = parts[0].replace("SUMMARY:", "").strip()
            
            # Extract key points
            key_points_section = parts[1].strip()
            for line in key_points_section.split("\n"):
                line = line.strip()
                if line.startswith("-") or line.startswith("•"):
                    key_points.append(line[1:].strip())
        else:
            # Fallback: use entire content as summary
            summary_text = content.strip()
        
        return summary_text, key_points
    
    async def summarize_batch(self, search_results: List[SearchResult]) -> List[Summary]:
        """
        Summarize multiple search results
        
        Args:
            search_results: List of SearchResult objects
            
        Returns:
            List of Summary objects
        """
        summaries = []
        for result in search_results:
            try:
                summary = await self.summarize(result)
                summaries.append(summary)
            except Exception as e:
                print(f"Warning: Failed to summarize {result.url}: {str(e)}")
                continue
        
        return summaries
