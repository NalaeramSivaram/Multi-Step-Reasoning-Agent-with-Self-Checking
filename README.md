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


