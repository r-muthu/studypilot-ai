from langchain_core.messages import AIMessage


def get_agent_text(message) -> str:
    """
    Extract readable text from an AIMessage.
    """

    if isinstance(message, AIMessage):
        if isinstance(message.content, str):
            return message.content

        if isinstance(message.content, list):
            return "".join(
                block.get("text", "")
                for block in message.content
                if isinstance(block, dict)
            )

    return str(message)