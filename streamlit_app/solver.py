from llm_mock import MockLLM
from prompts import PLANNER_PROMPT, EXECUTOR_PROMPT, VERIFIER_PROMPT

class ReasoningAgent:
    def __init__(self, max_retries=2):
        self.llm = MockLLM()
        self.max_retries = max_retries

    def solve(self, question):
        retries = 0
        checks = []

        while retries <= self.max_retries:

            plan = self.llm.call(PLANNER_PROMPT, question=question)
            exec_out = self.llm.call(EXECUTOR_PROMPT, question=question, plan=plan)

            result = exec_out["result"]
            explanation = exec_out["explanation"]

            verify = self.llm.call(
                VERIFIER_PROMPT,
                question=question,
                proposed_result=result,
                explanation=explanation
            )

            checks.append(verify)

            if verify["passed"]:
                return {
                    "answer": result,
                    "status": "success",
                    "reasoning_visible_to_user": explanation,
                    "metadata": {
                        "plan": plan,
                        "checks": checks,
                        "retries": retries
                    }
                }

            retries += 1

        return {
            "answer": None,
            "status": "failed",
            "reasoning_visible_to_user": "Verification failed.",
            "metadata": {
                "plan": plan,
                "checks": checks,
                "retries": retries
            }
        }
