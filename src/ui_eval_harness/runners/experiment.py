# Batch runner (stub). Wire up backends, templates, tasks; write GenerationEvents.
from pathlib import Path
from ..backends.ollama import OllamaBackend

def main():
    out = Path("artifacts/samples/demo")
    backend = OllamaBackend(model="llama3")  # placeholder
    res = backend.generate("Two-column signup", ["email", "password", "OAuth"], "template-A", out)
    print(f"Wrote sample HTML to {res.content_path}")

if __name__ == "__main__":
    main()
