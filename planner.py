from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Dict, Any, List


class Step(BaseModel):
    tool: str = Field(description="Nmae of the tool to execute")
    params: Dict[str, Any] = Field(
        default_factory=dict, description="Params for the tool"
    )


class Plan(BaseModel):
    steps: List[Step]


llm = ChatOllama(model="llama3", temperature=0)
parser = PydanticOutputParser(pydantic_object=Plan)

SYSTEM_PROMPT = """
You are a professional video editing planner.

Your job is to generate a structured editing plan
based on the user request and the video metadata.

You MUST:
- Only use the available tools.
- Never invent tools.
- Never reference files that do not exist.
- Respect the video duration.
- Ensure trim ranges are within duration.
- Return only valid JSON matching the schema instructions.

Available tools:

1. trim_video(start: float, end: float)
   - start and end must be within video duration
   - start < end

2. remove_silence()

3. add_subtitles(subtitle_file: str)

Video Metadata:
- Duration (seconds): {duration}
- FPS: {fps}
- Resolution: {width}x{height}

If the user asks for:
- "first 30 seconds" → start=0, end=30 (if duration >= 30)
- "short version" → reduce duration but keep meaningful section
- vertical output but video is landscape → include cropping step (if supported)

{format_instructions}

Return only the structured plan.
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", SYSTEM_PROMPT), ("user", "{request}")]
)


def create_plan(user_request: str, metadata: Dict[str, Any]) -> Plan:
    formatted_prompt = prompt.format_messages(
        request=user_request,
        duration=metadata["duration"],
        fps=metadata["fps"],
        width=metadata["resolution"][0],
        height=metadata["resolution"][1],
        format_instructions=parser.get_format_instructions(),
    )
    response = llm.invoke(formatted_prompt)
    # Parse + validate
    plan = parser.parse(response.content)
    return plan
