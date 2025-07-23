from crewai_tools import tool
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_community.document_loaders import PyPDFLoader

@tool("Descriptive Tool Name")
def MyCustomTool(arg1: type, arg2: type) -> str:
    """
    Clear and concise description of what the tool does.

    Args:
        arg1 (type): Description of the first argument.
        arg2 (type): Description of the second argument.

    Returns:
        str: Description of the output or result of the tool.
    """
    # Core logic

    
    result = ...  # implement your logic here

    # Return formatted result
    return f"Your result is: {result}"

@tool("pdf reader")
class PdfReader(BaseTool):
    path: str = Field(
        "resume file path",
        description="resume file path"
    )
    link: str = Field(
        
    )