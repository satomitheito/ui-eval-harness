import time, os
from pathlib import Path
from .base import BaseBackend, GenerationResult

class OllamaBackend(BaseBackend):
    name = "ollama"
    def __init__(self, model: str = "llama3"):
        self.model = model

    def generate(self, brief: str, acceptance: list[str], template: str, out_dir: Path) -> GenerationResult:
        # Placeholder: write a minimal HTML doc. Replace with real Ollama call.
        out_dir.mkdir(parents=True, exist_ok=True)
        start = time.time()
        html = f"""<html><body><h3>{brief}</h3><button>Create account</button></body></html>"""
        path = out_dir / "index.html"
        path.write_text(html, encoding="utf-8")
        return GenerationResult(content_path=path, duration_ms=int((time.time()-start)*1000), metadata={"model": self.model})
