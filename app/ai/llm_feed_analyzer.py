from app.ai.providers.ollama_provider import OllamaProvider
from app.ai.validators import validate_analysis


provider = OllamaProvider()


def analyze_post(content: str):
    return provider.analyze_feed(content)
    analysis = provider.analyze_feed(content)

    analysis = validate_analysis(
        analysis
    )

    return analysis