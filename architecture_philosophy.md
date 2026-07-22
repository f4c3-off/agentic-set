# Architecture and Philosophy: The Evolution Towards ICM

This document records the transition from a simple prompt collection (legacy) to a native **Agentic Operating System based on ICM (Interpretable Context Methodology)**.

## The "Filesystem as Architecture" Paradigm (Pure ICM)
Unlike commercial frameworks or "Control Planes" like **Paperclip** (which use databases, Node.js servers, React interfaces, and schedulers to manage agents as "employees"), our ecosystem embraces absolute minimalism.
In our system, the architecture **is** the filesystem:
- **No Database**: The project state is defined by the files present in the folders.
- **No SaaS Server**: Agents (Antigravity, Goose, etc.) operate entirely locally.
- **Transparency**: Instructions are not buried in the source code of a framework, but are written clearly in `CONTEXT.md` files inside the numbered folders (`1.1 - RAW/`, `1.3 - ANALYSIS/`).
- **How we borrow it:** We add a pattern to the system. When a sub-agent (e.g., the Explorer) has a highly complex task on data, instead of forcing it to use dozens of Bash commands, its `CONTEXT.md` will tell it: *"Write a temporary Python script in `0-SYSTEM/tmp/temp_script.py`, execute it to process the data, and then delete it"*. It leverages 100% of the agent's coding capabilities while keeping the SKILLS folder clean.

## The Role of the Architect
The Architect is not a framework, but a **Skill**. It acts like a compiler: it interviews the user, selects a predefined Stack Configuration (e.g., `Intelligence & Academy OS`), and materializes the folder pipeline, injecting the *Task Routing* rules into the global registry `0-SYSTEM/CONTEXT.md`.

## Extraction from Competing Frameworks
To keep the project at the cutting edge, we observe competitors (CrewAI, LangGraph, AutoGen) and extract their conceptual patterns ("gems") to transform them into simple textual instructions:
1. **From LangGraph (State Graphs)**: Instead of using a graph framework in Python, we map states as **folder paths**. We leverage the advantage of direct chat interaction. Since the agent executes the workflow "live" with the user, we do not need complex automated fallback routing (e.g., moving files back and forth). If a condition is not met or an error occurs, the instruction in `CONTEXT.md` will simply state: *"Stop, do not proceed, and notify the user in chat to request instructions"*. The chat becomes the error handler, ensuring maximum control.
2. **From SmolAgents (Code-as-Action)**: The inclination to have Python code written to solve tasks, rather than generating slow JSON, which we will integrate into the operational prompts of Coders.
3. **From CrewAI (Role-Playing)**: The rigid assignment of a "Persona" (Librarian, Explorer), which we inject via Van Clief's `<Identity>` tag in `CONTEXT.md`.
