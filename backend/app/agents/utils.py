from langchain_core.messages import AIMessage


def get_agent_text(message) -> str:
    """
    Extract all user-visible text from a LangChain AIMessage.
    """

    if not isinstance(message, AIMessage):
        return str(message)

    content = message.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_blocks = [
            block["text"]
            for block in content
            if (
                isinstance(block, dict)
                and block.get("type") == "text"
            )
        ]

        return "\n".join(text_blocks)

    return ""