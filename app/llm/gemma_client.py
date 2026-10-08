from google import genai

from app.config import settings


class GemmaClient:

    def __init__(self):
        print("GEMINI API KEY LOADED:", bool(settings.gemini_api_key))
        print("GEMMA MODEL:", settings.default_gemma_model)

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=settings.default_gemma_model,
            contents=prompt,
        )
        print("\n========== GEMMA RAW RESPONSE ==========")
        print(response.text)
        print("========================================\n")

        return response.text


# Create shared Gemma client
gemma_client = GemmaClient()