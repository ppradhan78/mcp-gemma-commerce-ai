from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Gemini
    gemini_api_key: str
    default_gemma_model: str = "gemma-4-26b-a4b-it"

    # MCP
    mcp_server_url: str = "http://127.0.0.1:8000/mcp"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()