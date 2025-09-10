from pydantic import BaseModel, conint

class EvalScore(BaseModel):
    design_score: conint(ge=1, le=5)
    func_score: conint(ge=1, le=5)
    a11y_issues: int = 0
    notes: str | None = None

    @property
    def overall(self) -> float:
        return 0.5 * self.design_score + 0.5 * self.func_score
