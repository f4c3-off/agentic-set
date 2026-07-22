# 🔄 Loop Engineering: Architecture of Autonomous Agents

> *This document summarizes the key concepts of modern agent orchestration (2026), marking the transition from "Prompt Engineering" to "Loop Engineering".*

## What is Actually a Loop?
A loop is a small program (or orchestration script) that acts as a "manager" for an LLM. It prompts the agent, reads what the agent produces, decides whether the work is finished, and if not, prompts it again. 
The user stops being the human *inside* the loop typing prompts. The user becomes the author of the loop, and the agent becomes a subroutine.

## The Spectrum of Agentic Evolution
1. **Phase 1 (Academic While Loop/ReAct):** The model reasons, uses a tool, reads, repeats. A human watches and intervenes.
2. **Phase 2 (AutoGPT):** Single agent with an open-ended goal, known for ending up in infinite loops without concrete results.
3. **Phase 3 (Single Loop/Ralph):** A bash script that continuously sends the same prompt, resetting context to specific files. Simple but disciplined.
4. **Phase 4 (Commercial Goal Commands):** Tools like Claude Code or OpenCode natively integrate loops (`/goal`) that stop when an automated validator gives the OK.
5. **Phase 5 (Continuous Multi-Agent Orchestration):** The loop is the unit of work. Loops supervise other background loops, managed by a timer (Cron/Harness) with state saved to Git to survive restarts.

## Cron + Decision Maker = Agent Harness
A common criticism is that loops are just "cronjobs". That's partly true: the scheduling layer is `cron` (or webhooks). 
But while a cronjob executes a fixed, deterministic script, **a loop runs a model that evaluates the current state, decides the next action, verifies if it worked, and decides whether to continue.** 
The loop is Cron combined with a decision-maker (the LLM) inside the loop body.

## Feedback and Validation are Everything
A loop without controls is a machine for generating errors very quickly.
The golden rule of Loop Engineering is that **a loop is only as reliable as its ability to inspect its own work.**
- Background review tools are needed.
- The agent must not just execute; a secondary agent (or the agent itself with a critique prompt) must evaluate the result before committing.

## Token Economics and Guardrails
Since models write fast, the expensive part is not inference, but managing a runaway loop. In production, it is mandatory to implement:
1. A maximum iteration limit (Max Steps).
2. Stall detection ("No progress").
3. A maximum ceiling on token or cost budget.

## Skills > Prompts
The loop is just the plumbing. The real value lies in the **Skills** called by the loop. A loop without reusable and tested skills is just an expensive "while loop". If the agent performs a complex operation, it must be crystallized into a skill so that the next agent in the loop can invoke it without context waste.

