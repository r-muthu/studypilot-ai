from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent

from app.models.chat import llm
from app.agents.prompts import SYSTEM_PROMPT
from app.agents.tools import TOOLS

study_agent = create_agent(
    model=llm,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=InMemorySaver(),
    debug=True,
)