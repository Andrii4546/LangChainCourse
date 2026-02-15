from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    
    """Schema of the source used by agent"""
    
    url: str = Field(description="The URL  of the source")
    
class AgentResponse(BaseModel): 
    """Schema for agent response with sources and an answer"""   
    
    sources: list[Source] = Field(default_factory=list, 
                                  description="List of sources used to generate the answer ")
    answer: str = Field(description="The agent's answer to the query")
