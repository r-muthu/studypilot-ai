import os

from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("MODEL_PROVIDER", "openai").lower()

if provider == "openai":
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(
        model=os.getenv(
            "OPENAI_EMBEDDING_MODEL",
            "text-embedding-3-small",
        ),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

elif provider == "bedrock":
    from langchain_aws import BedrockEmbeddings

    embeddings = BedrockEmbeddings(
        model_id=os.getenv(
            "BEDROCK_EMBEDDING_MODEL",
            "amazon.titan-embed-text-v2:0",
        ),
        region_name=os.getenv("AWS_REGION", "us-east-1"),
    )

elif provider == "gemini":
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    embeddings = GoogleGenerativeAIEmbeddings(
        model=os.getenv(
            "GEMINI_EMBEDDING_MODEL",
            "models/text-embedding-004",
        ),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

else:
    raise ValueError(f"Unsupported MODEL_PROVIDER: {provider}")