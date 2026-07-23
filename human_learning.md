# 📚 Human Learning & Research

This file contains resources designed for human study and learning about Agentic AI (papers, articles, guides, courses). Beyond theoretical concepts, each resource is evaluated to understand its practical potential in Advanced Research and Training work.

## Courses & Guides
- **[D2L (Dive into Deep Learning)](https://github.com/d2l-ai/d2l-en)** `#learning:course #purpose:training`: Interactive Deep Learning book with code and mathematics.
  - **✅ Pros**: The academic reference par excellence (used in 500+ universities), perfect for understanding "under the hood" of neural networks.
  - **❌ Cons**: Very steep learning curve, oriented towards mathematics and not rapid agent development.
  - **💡 Recommendations**: Use it as a theoretical reference to explain core concepts (attention, gradient descent) to learners, but not for daily development.
- **[Hello Agents](https://github.com/datawhalechina/hello-agents)** `#learning:course #purpose:training`: "Build agents from scratch", practical course on the principles of intelligent agents.
  - **✅ Pros**: Excellent step-by-step approach for beginners.
  - **❌ Cons**: Very basic project, not suitable for enterprise multi-agent architectures.
  - **💡 Recommendations**: Pass it to learners in the first weeks of Training to help them understand the fundamentals (reasoning, tools, action).
- **[Learn Anything](https://learn-anything.xyz/)** `#learning:course #purpose:training`: Tree-based search engine for educational mind maps.
  - **✅ Pros**: Visually powerful for exploring new topics.
  - **❌ Cons**: Maps are user-generated and sometimes lack depth.
  - **💡 Recommendations**: Use it to quickly search for the "big picture" of a new concept (e.g., "Retrieval Augmented Generation").
- **[Claude Code Playbook](https://duet.so/guides/claude-code-playbook-building-a-skill-first-workflow-that-actually-sticks)** `#learning:course #purpose:training`: Guide to "skill-first" workflows with Claude Code without writing code.
  - **✅ Pros**: Ideal for non-coder professionals who want immediate results.
  - **❌ Cons**: Too tied to the Anthropic ecosystem.
  - **💡 Recommendations**: Incorporate it as a "Quick Wins" module in courses for executive levels (C-Level).
- **[AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** `#learning:course #purpose:training`: Practical guide (Learn it. Build it. Ship it.).
  - **✅ Pros**: Perfectly balances theory and AI software engineering.
  - **❌ Cons**: Requires prior skills in programming and DevOps.
  - **💡 Recommendations**: Great as advanced study material for structuring your pipelines.
- **[Agents From Scratch](https://agentsfromscratch.com/)** `#learning:course #purpose:training`: Course for building AI agents locally without frameworks.
  - **✅ Pros**: Demystifies magical frameworks like LangChain; makes you truly understand how loops and tools work.
  - **❌ Cons**: Vanilla code is difficult to scale and maintain in production.
  - **💡 Recommendations**: Highly recommended for understanding the principles of the reasoning loop.
  - **🔄 Better Alternative**: Combine this course with the study of native code, but then use *LangGraph* or *Goose* in production for stability.
- **[LLM Step by Step](https://github.com/P-Slark/LLM-Step-by-Step)** `#learning:course #purpose:training`: PyTorch guide inspired by Stanford's CS336.
  - **✅ Pros**: Academic depth on how to "train" an LLM.
  - **❌ Cons**: Irrelevant for those who only want to *use* LLMs and not pre-train them.
  - **💡 Recommendations**: Keep it as a curiosity or academic extra.
- **[Don't Feed The AI](https://github.com/zeroc00I/DontFeedTheAI)** `#learning:course #purpose:training`: Transparent anonymization proxy for pentesting and security (removes PII and IP).
  - **✅ Pros**: Crucial in high-security/intelligence environments to prevent leaks of classified data.
  - **❌ Cons**: Can incorrectly block or obfuscate data useful to the context.
  - **💡 Recommendations**: Implement as a security standard if using Cloud APIs. For zero risk, however, use a local approach with private models and *OmniRoute*.

## Papers & Research
- **[Context Engineering 2.0](https://arxiv.org/pdf/2510.26493v1)** `#learning:paper #purpose:research`: Paper on context management methodology.
  - **✅ Pros**: Mathematically/theoretically formalizes why immense prompts fail.
  - **❌ Cons**: Very verbose and academic.
  - **💡 Recommendations**: Extract metrics from here to validate the effectiveness of memory files.
- **[ICM: Interpretable Context Methodology (Folder Structure as Agent Architecture)](#)** `#learning:paper #purpose:research`: Methodology on using the file system and Markdown as orchestration code.
  - **✅ Pros**: The revolutionary paradigm for the "Wiki LLM". Eliminates the need for complex Python scripts to manage agent state.
  - **❌ Cons**: Requires a radical mindset shift in directory management.
  - **💡 Recommendations**: Use this as a *manifesto* for a "Second Brain". Always pair it with the [Interpreted-Context-Methdology](https://github.com/RinDig/Interpreted-Context-Methdology) repository.
- **[HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249)** `#learning:paper #purpose:research`: Paper on dynamic creation of agent harnesses.
  - **✅ Pros**: Defines the future of environments in which agents live (not just chat, but complete OSs).
  - **❌ Cons**: Very advanced concepts, difficult for immediate application without tools.
  - **💡 Recommendations**: Useful reading to understand the industry direction towards "Agentic OSs".

## ⚙️ Methodologies & Design Principles (Agentic Patterns)
This section covers architectural frameworks and mental models extracted from industry best practices, essential for programming and orchestrating behaviors (System Prompts).

- **[12-Factor Agents](https://github.com/humanlayer/12-factor-agents)**
  - **What it is**: A prompt injection and structuring methodology inspired by software development's `12-Factor App`. It is based on abandoning conversational prompts in favor of a rigid architecture structured to minimize dependence on implicit context.
  - **✅ Pros**: Makes agent behavior highly deterministic, testable, and hallucination-proof, protecting production pipelines.
  - **💡 Recommendations**: It is the gold standard to use when generating sub-agent `CONTEXT.md` files. Every agentic identity should obey clear formal rules.

- **[Loop Engineering & Agent Harnesses](https://addyosmani.com/blog/agent-harness-engineering/)** (and the associated course *Agent Factory*)
  - **What it is**: The design of the environment surrounding the agent. Instead of asking the agent to "do everything in a single prompt", *Loop Engineering* involves an external system (a timer, a *harness*, a script, or framework like Goose) that retrieves work, assigns it to the agent, passes the output to a second validator agent, and consolidates results autonomously (Unattended AI).
  - **✅ Pros**: Allows safe unsupervised execution and breaks down titanic tasks into digestible, verifiable cycles.
  - **💡 Recommendations**: Never delegate repetition logic (while-loop) to the LLM itself. Build external pipelines that "nudge" the agent at each iterative step.

## Articles & Maps
- **[Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** `#learning:article #purpose:inspiration`: Pattern for building LLM-maintained knowledge bases.
  - **✅ Pros**: The foundational text for the "Second Brain" idea. Simple and intuitive.
  - **❌ Cons**: It is only a "concept" described in a Gist, no official implementation.
  - **💡 Recommendations**: Use as mandatory reading for anyone starting the academic course.
- **[L'Agente non ha una forma](https://pinperepette.github.io/signal.pirate/articoli/l-agente-non-ha-una-forma.html?t=d)** `#learning:article #purpose:inspiration`: Italian theoretical article ("The Agent has no shape").
  - **✅ Pros**: Explores abstractions and interfaces for agents uncoupled from the concept of a "chatbot".
  - **❌ Cons**: Very philosophical/theoretical.
  - **💡 Recommendations**: Stimulating reading to understand current limitations of chat-based interfaces (like ChatGPT).
- **[The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)** `#learning:article #purpose:inspiration`: LangChain article on harnesses.
  - **✅ Pros**: Clearly defines the difference between "model", "agent", and "the environment" (the harness) in which the agent runs and operates.
  - **❌ Cons**: Rather commercial towards LangChain products.
  - **💡 Recommendations**: Great for clarifying technical glossary.
- **[Gemini Memoria Persistente](https://www.smartworld.it/news/gemini-memoria-persistente-import-chat-chatgpt-claude.html)** `#learning:article #purpose:inspiration`: News on cross-platform persistence in Gemini.
  - **✅ Pros**: Demonstrates the market trend towards continuous memory.
  - **❌ Cons**: "Closed" cloud solution, not suitable for local intelligence or sensitive data.
  - **💡 Recommendations**: Cite as a "consumer" example in contrast to private and secure "Agentic Stacks".
- **[Agentic AI Landscape](https://github.com/antgroup/agentic-ai-landscape)** `#learning:article #purpose:inspiration`: Overview of the agentic ecosystem.
  - **✅ Pros**: Highly useful data-driven snapshot for presentations and board analysis.
  - **❌ Cons**: Ages quickly.
  - **💡 Recommendations**: Check quarterly to extract market insights for reports.

## Case Studies (Alignment & Jailbreak)
Intelligence involves understanding the weaknesses of LLMs and how to manipulate (or protect) their alignment:
- **[CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S)** `#learning:case_study #purpose:audit`: Leak of original System Prompts from major models (Claude, ChatGPT).
  - **✅ Pros**: Exposes exactly "how" big tech controls their base models.
  - **❌ Cons**: Prompts change over time.
  - **💡 Recommendations**: Study the file to learn the "tone of voice" and professional prompt engineering techniques used at the enterprise level.
- **[OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS)** `#learning:case_study #purpose:audit`: Repository on extreme jailbreak techniques.
  - **✅ Pros**: Essential for cybersecurity (Red Teaming) and understanding how to bypass censorship on "sensitive" Analytical Research (OSINT) topics (e.g., weapons, cyber-attacks).
  - **❌ Cons**: Techniques are often patched quickly; risk of generating toxic/unstable output.
  - **💡 Recommendations**: Use for defensive research purposes or to test the robustness of government "Guardrails" in Agentic OSs.
