import os

from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("MODEL_PROVIDER", "openai").lower()

if provider == "openai":
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
    )

elif provider == "bedrock":
    from langchain_aws import ChatBedrockConverse

    llm = ChatBedrockConverse(
        model_id=os.getenv(
            "BEDROCK_MODEL",
            "anthropic.claude-3-5-sonnet-20241022-v2:0",
        ),
        region_name=os.getenv("AWS_REGION", "us-east-1"),
        api_key=os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
        temperature=0,
    )

elif provider == "gemini":
    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0,
    )

else:
    raise ValueError(f"Unsupported MODEL_PROVIDER: {provider}")