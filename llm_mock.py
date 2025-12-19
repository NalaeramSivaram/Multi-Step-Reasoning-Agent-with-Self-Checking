import re
from datetime import datetime

class MockLLM:
    def call(self, prompt, **kwargs):

        # Planner
        if "Planner module" in prompt:
            return (
                "1. Parse question\n"
                "2. Extract numbers or time\n"
                "3. Compute\n"
                "4. Validate\n"
                "5. Produce answer"
            )

        # Executor
        if "Executor module" in prompt:
            question = kwargs.get("question")
            return self._execute(question)

        # Verifier
        if "Verifier module" in prompt:
            question = kwargs.get("question")
            proposed = kwargs.get("proposed_result")
            return self._verify(question, proposed)

        return "UNKNOWN PROMPT"

    # ------------------------------------------------------
    # EXECUTE
    # ------------------------------------------------------
    def _execute(self, question):
        # Detect time difference
        m = re.search(r"(\d{1,2}:\d{2}).*(\d{1,2}:\d{2})", question)
        if m:
            t1 = datetime.strptime(m.group(1), "%H:%M")
            t2 = datetime.strptime(m.group(2), "%H:%M")
            minutes = (t2 - t1).seconds // 60
            return {
                "result": f"{minutes} minutes",
                "explanation": f"Difference between {m.group(1)} and {m.group(2)}"
            }

        # Apples problem
        if "apples" in question.lower():
            red = int(re.search(r"(\d+) red", question).group(1))
            green = red * 2
            total = red + green
            return {
                "result": str(total),
                "explanation": f"Red={red}, Green={green}, Total={total}"
            }

        return {"result": "unknown", "explanation": "Mock LLM cannot solve this question."}

    # ------------------------------------------------------
    # VERIFY
    # ------------------------------------------------------
    def _verify(self, question, proposed):
        # Re-check time computation
        m = re.search(r"(\d{1,2}:\d{2}).*(\d{1,2}:\d{2})", question)
        if m:
            t1 = datetime.strptime(m.group(1), "%H:%M")
            t2 = datetime.strptime(m.group(2), "%H:%M")
            minutes = (t2 - t1).seconds // 60
            return {
                "passed": str(minutes) in proposed,
                "details": f"Expected {minutes} minutes"
            }

        # Re-check apples
        if "apples" in question.lower():
            red = int(re.search(r"(\d+) red", question).group(1))
            total = red + (red * 2)
            return {
                "passed": str(total) in proposed,
                "details": f"Expected {total}"
            }

        return {"passed": False, "details": "Verifier uncertain"}
