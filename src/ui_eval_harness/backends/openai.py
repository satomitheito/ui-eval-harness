# Optional: scaffold for OpenAI provider (no key included)
from .base import BaseBackend, GenerationResult
from pathlib import Path

class OpenAIBackend(BaseBackend):
    name = "openai"
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model

    def generate(self, brief: str, acceptance: list[str], template: str, out_dir: Path) -> GenerationResult:
        # TODO: implement with openai SDK using env var OPENAI_API_KEY
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / "index.html"
        path.write_text("<html><body><h3>OpenAI placeholder output</h3></body></html>", encoding="utf-8")
        return GenerationResult(content_path=path, metadata={"model": self.model})
