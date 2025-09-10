from ui_eval_harness.eval.rubric import EvalScore

def test_evalscore_overall():
    s = EvalScore(design_score=4, func_score=2)
    assert s.overall == 3.0
