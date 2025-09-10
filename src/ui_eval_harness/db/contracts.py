from pydantic import BaseModel, Field, conint
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List

class GenerationEvent(BaseModel):
    gen_id: str
    task_id: str
    model_id: str
    template_id: str
    started_at: datetime
    duration_ms: int
    tokens_in: Optional[int] = None
    tokens_out: Optional[int] = None
    cost_usd: Optional[float] = None
    output_path: Path
    sandbox_flags: Dict[str, bool] = {}

class EvalRecord(BaseModel):
    eval_id: str
    gen_id: str
    rater_id: str
    design_score: conint(ge=1, le=5)
    func_score: conint(ge=1, le=5)
    a11y_issues: int = 0
    failures: List[str] = []
    notes: Optional[str] = None
    created_at: datetime
