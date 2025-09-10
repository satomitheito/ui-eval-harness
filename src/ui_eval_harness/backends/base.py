from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class GenerationResult:
    content_path: Path
    tokens_in: Optional[int] = None
    tokens_out: Optional[int] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    metadata: Dict[str, Any] = None

class BaseBackend:
    name = "base"
    def generate(self, brief: str, acceptance: list[str], template: str, **kwargs) -> GenerationResult:
        raise NotImplementedError
