# 🧠 Multi-Step Reasoning Agent with Self-Checking

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LLM](https://img.shields.io/badge/LLM-API%20Based-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

This project implements a **Multi-Step Reasoning Agent** capable of solving structured **math, logic, and constraint-based word problems**.  
The agent reasons in multiple phases, **verifies its own work**, and returns **only the final answer** to the user in a structured JSON format.

The design focuses on **correctness, reliability, and transparency**, while avoiding exposure of raw chain-of-thought reasoning.

---

## 🎯 Objective

To build a reasoning agent that:
- Solves problems step-by-step internally
- Performs self-checking and validation
- Retries automatically on failure
- Outputs a clean, user-facing answer
- Separates planning, execution, and verification logic

---

## 🧠 Problem Domain

The agent handles problems such as:

- **Time calculations**
  - *If a train leaves at 14:30 and arrives at 18:05, how long is the journey?*
- **Arithmetic & logic**
  - *Alice has 3 red apples and twice as many green apples. How many apples in total?*
- **Constraint satisfaction**
  - *A meeting needs 60 minutes. Available slots: 09:00–09:30, 09:45–10:30, 11:00–12:00. Which slot fits?*

Input: plain text question  
Output: structured JSON response

---

## 📤 Output Schema

```json
{
  "answer": "<final short answer>",
  "status": "success | failed",
  "reasoning_visible_to_user": "<short explanation>",
  "metadata": {
    "plan": "<abbreviated internal plan>",
    "checks": [
      {
        "check_name": "<string>",
        "passed": true,
        "details": "<string>"
      }
    ],
    "retries": 0
  }
}
```
---
## 🏗️ Agent Architecture

  The agent follows a three-phase internal loop:

# 1️⃣ Planner

  *  Reads the user question

  *  Produces a concise step-by-step plan

    Example:

    parse → extract quantities → compute → validate → format answer

---

# 2️⃣ Executor

  *  Executes the plan

  *  Performs intermediate calculations

  *  May call:

      *  LLM (for reasoning)

      *  Python code (for arithmetic)

---

# 3️⃣ Verifier

   *  Re-checks the solution using one or more methods:

       *  Independent re-solving

       *  Constraint validation

       *  Consistency checks

  If verification fails:
  
      *  Retries up to a fixed limit

      *  Otherwise marks status as failed

---

## 🔍 Key Design Principles

  *  No raw chain-of-thought exposed

  *  Clean separation of concerns

  *  Deterministic validation wherever possible

  *  Retry-based robustness

  *  Debug metadata preserved for evaluation


## 🧪 Evaluation & Test Cases

The project includes a small test suite with:

  *  Easy cases

      *  Basic arithmetic

      *  Simple time differences

  *  Tricky cases

      *  Multi-step reasoning

      *  Boundary conditions

      *  Ambiguous quantities

For each test, the following are logged:

  * Input question
  
  * Final JSON output

  * Verification status

  * Retry count

## 🚧 Challenges & Solutions
|Challenge |	Solution |
|----|----|
|Arithmetic errors |	Explicit calculation and validation|
|Logical inconsistencies	| Verifier phase with re-checking|
|Over-verbose reasoning	| Hid chain-of-thought from user|
|Ambiguous inputs	| Conservative parsing and checks|
|False confidence	| Retry or fail with explanation|

---

## 🛠️ Technologies Used
*  Python
*  LLM API (OpenAI / Anthropic / Gemini or mock)
*  JSON-based input/output
*  Modular prompt design
