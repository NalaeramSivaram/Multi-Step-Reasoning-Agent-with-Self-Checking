from solver import ReasoningAgent
import json

agent = ReasoningAgent()

questions = [
    "If a train leaves at 14:30 and arrives at 18:05, how long is the journey?",
    "Alice has 3 red apples and twice as many green apples. Total?",
]

for q in questions:
    print("\nQUESTION:", q)
    print(json.dumps(agent.solve(q), indent=2))
