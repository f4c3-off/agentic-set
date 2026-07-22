# 🧠 AI Second Brain: Knowledge Factory

> **[AGENT INSTRUCTION]**
> You are reading a "Second Brain", now structured as a "Knowledge Factory". Follow the pipeline from 1 to 6 based on the task you need to perform. Each level provides specific skills, tools, and frameworks to acquire, process, store, or produce knowledge.

---

## 1. 🔍 Ingest & Research
*Tools for web search, raw information extraction, and standardization into LLM-readable formats.*

### Autonomous Research & Analytical Research (OSINT)
- **[Agent Reach](https://github.com/Panniantong/Agent-Reach)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Skill to give the agent "eyes" on the Internet: allows searching and reading Twitter, Reddit, YouTube, GitHub for free via CLI.
  - **✅ Pros**: Free, easy CLI integration, supports multiple platforms.
  - **❌ Cons**: Limited to supported public sources, risk of instability if unofficial APIs change.
  - **💡 Tips**: Use it for quick social trend checks (e.g., "what is being said today about a certain topic").
- **[Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Skill that performs in-depth searches across the last 30 days (web and social) and synthesizes a factual summary.
  - **✅ Pros**: Precise temporal focus, useful for staying up to date.
  - **❌ Cons**: Limited to the 30-day window, less useful for deep historical research.
  - **💡 Tips**: Implement it to generate automated morning briefings on trending topics.
- **[Perplexica](https://github.com/ItzCrazyKns/Perplexica)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Privacy-focused AI search engine supporting local and cloud LLMs.
  - **✅ Pros**: Complete privacy, interfaces with Ollama, open-source.
  - **❌ Cons**: Requires hardware resources if used 100% locally.
  - **💡 Tips**: Replace Google with Perplexica if processing sensitive intelligence data.
- **[STORM (Stanford)](https://github.com/stanfordnlp/storm)** `#workflow:analytical_research #domain:osint`: Framework for asynchronous analytical research (OSINT) (digital experts debating and synthesizing).
  - **✅ Pros**: "Wikipedia"-quality output, rigorous citations, multi-perspective approach.
  - **❌ Cons**: Slow to run, high token cost if not used with local models.
  - **💡 Tips**: Use it only to generate final deliverables (whitepapers) for C-Level executives.
- **[GPT Researcher](https://github.com/assimp/gpt-researcher)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Automates the "Plan → Search → Read → Reflect → Synthesize" cycle.
  - **✅ Pros**: Highly flexible and configurable for various output formats.
  - **❌ Cons**: Less structured in using debating "personas" compared to STORM.
  - **💡 Tips**: The generic search engine (the daily "Agentic Google").
- **[Agent Laboratory](https://github.com/agent-laboratory/agent-laboratory)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Framework for the full research cycle.
  - **✅ Pros**: Deep academic rigor, hypothesis testing.
  - **❌ Cons**: Overly complex for quick analytical research (OSINT) queries.
  - **💡 Tips**: Ideal if you are producing a document or course requiring scientific validation.
- **[OWASP Social OSINT Agent](https://github.com/OWASP/SocialOSINTAgent)** `#workflow:osint #role:data_gathering #archetype:intelligence`: OSINT agent focused on social media, images, and text.
  - **✅ Pros**: Created for cybersecurity (OWASP), deep cross-analysis.
  - **❌ Cons**: Sector-specific, focused primarily on threat intelligence and profiling.
  - **💡 Tips**: Use it when you need to investigate or trace specific profiles.
- **[Brave Search MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** `#workflow:osint #role:data_gathering #archetype:intelligence`: MCP Server for parallel web search.
  - **✅ Pros**: Native web browsing for MCP agents (like Goose or Claude Code) in full transparency.
  - **❌ Cons**: Subject to Brave Search free rate limits.
  - **💡 Tips**: Essential plugin to keep running in the background on the local agent.

### Data Extraction: PDF-to-Markdown Solutions
- **[MinerU (by OpenDataLab)](https://github.com/opendatalab/MinerU)** `#workflow:raw_ingestion #tool:extraction`: Uses a vision-language model.
  - **✅ Pros**: Unbeatable accuracy for complex layouts (intricate tables, formulas).
  - **❌ Cons**: Requires high-performance GPUs, difficult to configure on standard laptops.
  - **💡 Tips**: Indispensable if working with long, chart-heavy high-security/financial reports.
- **[Marker (by Datalab)](https://github.com/VikParuchuri/marker)** `#workflow:raw_ingestion #tool:extraction`: High-performance conversion model.
  - **✅ Pros**: Very fast (batch processing), includes a `--use_llm` flag to fix unusual formatting.
  - **❌ Cons**: Mixed licenses that may restrict certain commercial edge cases.
  - **💡 Tips**: Ideal for bulk ingestion of most downloaded OSINT documents.
- **[Docling (by IBM)](https://github.com/DS4SD/docling)** `#workflow:raw_ingestion #tool:extraction`: Enterprise framework (MIT license).
  - **✅ Pros**: Runs excellently on CPU, reads DOCX and PPTX for RAG (LlamaIndex/LangChain).
  - **❌ Cons**: Slight loss of visual fidelity on highly fragmented documents.
  - **💡 Tips**: Use it if you lack a dedicated GPU or are processing presentations and Word documents.
- **[Unstructured](https://github.com/Unstructured-IO/unstructured)** `#workflow:raw_ingestion #tool:extraction`: Industrial RAG tool.
  - **✅ Pros**: Proven enterprise reliability, zero workflow bottlenecks.
  - **❌ Cons**: Heavy architecture with numerous dependencies (not "agile").
  - **💡 Tips**: Choose it for highly stable multi-user RAG pipelines.
- **[MarkItDown](https://github.com/microsoft/markitdown)** `#workflow:raw_ingestion #tool:extraction`: Essential Microsoft utility.
  - **✅ Pros**: Lightweight, instantaneous on plain text.
  - **❌ Cons**: Fails to preserve nested tables or perform OCR on complex images.
  - **💡 Tips**: Use it only for converting old plain text documents (e.g., notes and text files).

---

## 2. 🧠 Sense-Making & Strategy
*Frameworks for breaking down complex problems, deliberating, and logically structuring information.*

- **[Strategy Consultant Frameworks](https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks)**
  - **✅ Pros**: Transforms agent reasoning from simple text into BCG/McKinsey logic.
  - **❌ Cons**: Risks constraining the LLM if the task requires creative flexibility.
  - **💡 Tips**: Set it to use "Issue Trees" to deconstruct complex intelligence problems.
- **[Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence)**
  - **✅ Pros**: Simulates a committee (reducing hallucinations and bias).
  - **❌ Cons**: Consumes huge amounts of tokens and time for internal deliberations.
  - **💡 Tips**: Activate it only before making final decisions on critical OSINT analysis.
- **[CC Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills)**
  - **✅ Pros**: Over 18 mental models (e.g., OODA Loop, useful for tactics).
  - **❌ Cons**: Requires knowing how to trigger the right skill at the right time (not automatic).
  - **💡 Tips**: Integrate "OODA Loop" into basic training for situational analysis.
- **[Agentic OS](https://github.com/KbWen/agentic-os)**
  - **✅ Pros**: Enforced rules (Plan, Build, Review, Test, Ship) that prevent the agent from skipping QA checks.
  - **❌ Cons**: Validation workflow can slow down drafting simple notes.
  - **💡 Tips**: Extract its policies and place them in a global `AGENTS.md` file to protect the workspace.

---

## 3. 🗂️ Knowledge Management & Storage
*The "foundations" where knowledge is stored, structured, and maintained over time by the Agent.*

- **[Second Brain](https://github.com/NicholasSpisak/second-brain)**
  - **✅ Pros**: Demonstrates a pure implementation of an "LLM Wiki".
  - **❌ Cons**: Heavily dependent on its specific setup.
  - **💡 Tips**: Study the repository to extract logic and scripts for ingesting Markdown notes.
- **[Ariadne](https://github.com/pariyar07/ariadne)**
  - **✅ Pros**: Agents can map and use complex Obsidian architectures (tags, links).
  - **❌ Cons**: Works exclusively if the core is Obsidian.
  - **💡 Tips**: If you take courses and write notes via Obsidian, install it as a tool for Goose.
- **[ICM Architect and ICM Core Repo](https://github.com/RinDig/Interpreted-Context-Methdology)**
  - **✅ Pros**: Transforms standard file folders into an environment natively understandable by AI (MWP).
  - **❌ Cons**: Requires time to rename and structure the archive according to specified standards.
  - **💡 Tips**: Apply the templates to structure educational material directories.
- **[Obsidian Skills (gmickel & kepano)](https://github.com/kepano/obsidian-skills)**
  - **✅ Pros**: Teaches the AI to handle JSON Canvas (Obsidian whiteboards) and clean formatting.
  - **❌ Cons**: Only a collection of specific instructions, not a persistent server.
  - **💡 Tips**: Feed this to the agent before asking it to summarize Canvas diagrams.
- **[Graphify](https://github.com/Graphify-Labs/graphify)**
  - **✅ Pros**: Drastic token reduction, semantic correlation understanding within a true local Knowledge Graph.
  - **❌ Cons**: Requires parsers (tree-sitter) and is a recent project (may have edge-case bugs).
  - **💡 Tips**: Move away from basic vector RAG for querying notes: use this MCP server.
- **[Agentic Stack](https://github.com/codejunkie99/agentic-stack)**
  - **✅ Pros**: True episodic memory (`lessons.jsonl`); agent doesn't make the same mistake twice.
  - **❌ Cons**: If poorly managed, the lesson log becomes bloated and confusing.
  - **💡 Tips**: Set it up right away: when you correct a report for C-Level executives, the agent will learn stylistic preferences for next time.
- **[OpenWiki](https://github.com/langchain-ai/openwiki)**
  - **✅ Pros**: Scans directories and automatically produces interlinked, readable wikis.
  - **❌ Cons**: Primarily designed for software/codebase documentation (needs adaptation for text intelligence files).
  - **💡 Tips**: Use it to dynamically present generated OSINT reports on a web server or GitHub Pages.
- **[Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)**
  - **✅ Pros**: Ready-to-use MCP for vector search of files and text for LLMs.
  - **❌ Cons**: Suffers from classic vector limitations (poor understanding of file relationship logic compared to Graphify).
  - **💡 Tips**: Keep as a fallback (Plan B) for log searches when Knowledge Graph returns no results.

---

## 4. ✨ Polish & Aesthetic
*Stylistic alignment: taste, art direction, semantic refinement, and formatting.*

- **[Taste Skill](https://github.com/leonxlnx/taste-skill)**
  - **✅ Pros**: Removes classic GPT "slop" (buzzwords like "Crucial", "Revolutionary", etc.).
  - **❌ Cons**: Imposes the skill author's personal tone.
  - **💡 Tips**: Modify its internal prompt to enforce a structured, detached, or analytical tone.
- **[Awesome NotebookLM Prompts](https://github.com/serenakeyitan/awesome-notebookLM-prompts)**
  - **✅ Pros**: Extracts maximum performance for complex summaries, including audio/podcast outputs.
  - **❌ Cons**: Text resource (not a script or actual server).
  - **💡 Tips**: Use them to prepare briefings for people with very little time to read who prefer quick summaries (NotebookLM style).
- **[StyleSeed](https://github.com/bitjaru/styleseed)**
  - **✅ Pros**: Gives AI an "eye" for design (color consistency, spacing, typography).
  - **❌ Cons**: Useful only for web UI and Frontend, useless for PDF/Markdown reports.
  - **💡 Tips**: Leverage it if you decide to build a visual OSINT dashboard for the web.

---

## 5. 📦 Output & Production
*The factory's "printers": tools and engines to generate complete, verified, ready-to-use deliverables.*

- **[Lunaris](https://github.com/PouyanJay/lunaris)**
  - **✅ Pros**: "Anti-hallucination" algorithm, fact-checking via PgVector, structured for deep educational content.
  - **❌ Cons**: Laborious setup (dedicated vector database).
  - **💡 Tips**: The tool to master for creating AI course architectures.
- **[Dair Academy Plugins](https://github.com/dair-ai/dair-academy-plugins)**
  - **✅ Pros**: Proven plugins for managing academic AI syllabi.
  - **❌ Cons**: Rigid, built specifically for DAIR.AI.
  - **💡 Tips**: Analyze its structural approach for building local training/courses.
- **[Baoyu Design](https://github.com/JimLiu/baoyu-design)**
  - **✅ Pros**: Instantly transforms design concepts into functional HTML files.
  - **❌ Cons**: Limited to quick-prototyping.
  - **💡 Tips**: Less useful today compared to native features (e.g., Claude Artifacts); use only as an emergency tool.

---

## 6. 🛠️ Core Toolbelt
*Core infrastructure and standard prompt collections.*

- **[Claude Skills Collection](https://github.com/abubakarsiddik31/claude-skills-collection) and [Agent Skills](https://github.com/addyosmani/agent-skills)**
  - **✅ Pros**: High-quality, ready-to-use scripts (Bash, File System, Git).
  - **❌ Cons**: Using all scripts together risks confusing the agent.
  - **💡 Tips**: "Cherry Pick": take only Python/JS scripts that enable new APIs and discard generic ones.
- **[Application Skills](https://github.com/membranedev/application-skills)**
  - **✅ Pros**: Macros to control desktop apps (via UI scripts).
  - **❌ Cons**: Easily broken by OS/App updates.
  - **💡 Tips**: Useful for local automation (e.g., opening an intelligence PDF received via email and extracting data).
- **[AutoSkills](https://github.com/midudev/autoskills)**
  - **✅ Pros**: Instant stack setup.
  - **❌ Cons**: Low modularity, installs unnecessary items.
  - **💡 Tips**: Avoid for a precision Second Brain; prefer installing MCP Servers manually for full control.
- **Prompt Collections (Prompts.chat, Agentic Set, Anthropic Library, LangChain Hub)**
  - **✅ Pros**: Massive databases for setup configurations and roles (personas), plus advanced techniques (e.g., RAG with LangChain, coding with Anthropic).
  - **❌ Cons**: Some community-driven patterns are verbose or obsolete (e.g., optimized for GPT-3.5).
  - **💡 Tips**: Use as inspiration to extract snippets for injection into your agents' `CONTEXT.md` files via Cherry Picking.
- **[Fabric](https://github.com/danielmiessler/fabric)**
  - **✅ Pros**: The ultimate CLI framework for the Bash ecosystem. Hundreds of ready patterns for wisdom extraction, claim analysis, and report writing.
  - **❌ Cons**: High risk of "Slop" (bloat). Cloning in full bloats the system.
  - **💡 Tips**: Don't install it all; use our *Curated Index Strategy* by extracting only vital patterns (e.g., `extract_wisdom`) and converting them to plain text for `CONTEXT.md`.
- **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)**
  - **✅ Pros**: Brilliant gateway to save up to 90% on tokens (compression) and route traffic between Ollama (free) and Cloud.
  - **❌ Cons**: Adds a local network step and requires JSON configuration.
  - **💡 Tips**: Beating heart of the system: use it as the base API for Goose to avoid wasting budget on tokens.
- **[Colibri](https://github.com/JustVugg/colibri)**
  - **✅ Pros**: Enables local execution of giant models that would otherwise not run.
  - **❌ Cons**: Streaming from NVMe drive is much slower than VRAM.
  - **💡 Tips**: Use if you want to process huge classified documents in complete privacy and offline (overnight or asynchronously).
- **[jcode](https://github.com/1jehuang/jcode)**
  - **✅ Pros**: Lightweight, written in Rust, perfect for complex code workflows.
  - **❌ Cons**: Completely misaligned with "Second Brain" logic for notes and OSINT research.
  - **💡 Tips**: Ignore for this specific use case; keep on your list if you decide to program an independent OS tomorrow.



---

## 7. 🏢 Standalone Agent Frameworks & Platforms

This file contains platforms, multi-agent frameworks, and complex orchestration solutions that are standalone.

- [Example Resource Name](./resources/example-resource.md) `#archetype:operational_pipeline #purpose:automation` - [Briefly describe the resource, e.g., "Internal style guide for Python projects"]
- [Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence) `#archetype:operational_pipeline #purpose:automation` - Framework multi-agente
- [EpicStaff](https://github.com/EpicStaff/EpicStaff) `#archetype:operational_pipeline #purpose:automation` - Piattaforma self-hosted per costruire flussi di agenti AI
- [PraisonAI](https://github.com/MervinPraison/PraisonAI) `#archetype:operational_pipeline #purpose:automation` - Framework multi-agente per automazione
- [Agent Reach](https://github.com/Panniantong/Agent-Reach) `#archetype:operational_pipeline #purpose:automation` - Framework per l'espansione delle capacità degli agenti
- [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) `#archetype:operational_pipeline #purpose:automation` - Piattaforma e framework open source per AI
- [GOD](https://github.com/XiaoLuoLYG/GOD) `#archetype:operational_pipeline #purpose:automation` - Framework sperimentale per agenti
- [Hivemind](https://github.com/activeloopai/hivemind) `#archetype:operational_pipeline #purpose:automation` - Framework decentralizzato per AI
- [Bytechef](https://github.com/bytechefhq/bytechef) `#archetype:operational_pipeline #purpose:automation` - Piattaforma e harness per workflow agentici
- [Agentic Inbox](https://github.com/cloudflare/agentic-inbox) `#archetype:operational_pipeline #purpose:automation` - Tool di gestione flussi agentici
- [Agency Agents](https://github.com/msitarzewski/agency-agents) `#archetype:operational_pipeline #purpose:automation` - Framework per agenzie di agenti AI
- [Omnigent](https://github.com/omnigent-ai/omnigent) `#archetype:operational_pipeline #purpose:automation` - Framework agentico universale
- [Ouroboros](https://github.com/razzant/ouroboros) `#archetype:operational_pipeline #purpose:automation` - Framework di esecuzione ciclica e autonoma
- [Ruflo](https://github.com/ruvnet/ruflo?utm_source=chatgpt.com) `#archetype:operational_pipeline #purpose:automation` - Framework per flussi di lavoro AI
- [OpenFugu](https://github.com/trotsky1997/OpenFugu) `#archetype:operational_pipeline #purpose:automation` - Framework agentico Open Source
- [Clowder AI](https://github.com/zts212653/clowder-ai) `#archetype:operational_pipeline #purpose:automation` - Framework multi-agente
- [Paperclip](https://github.com/paperclipai/paperclip) `#archetype:operational_pipeline #purpose:automation` - Framework e harness agentico
- [GStack](https://github.com/garrytan/gstack) `#archetype:operational_pipeline #purpose:automation` - Stack e framework di sviluppo AI
- [AutoResearch](https://github.com/karpathy/autoresearch) `#archetype:operational_pipeline #purpose:automation` - Framework per ricerca automatizzata
- [Midday](https://github.com/midday-ai/midday) `#archetype:operational_pipeline #purpose:automation` - Piattaforma operativa e framework AI
- [jcode](https://github.com/1jehuang/jcode) `#archetype:operational_pipeline #purpose:automation` - Tool e ambiente di sviluppo
- [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) `#archetype:operational_pipeline #purpose:automation` - Tool per ricerca accademica con Claude
- [Claw Empire](https://github.com/GreenSheep01201/claw-empire) `#archetype:operational_pipeline #purpose:automation` - Progetto di test e orchestrazione AI
- [AI Job Search](https://github.com/MadsLorentzen/ai-job-search) `#archetype:operational_pipeline #purpose:automation` - Automazione per ricerca lavoro tramite AI
- [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) `#archetype:operational_pipeline #purpose:automation` - Tool OSINT integrato con AI
- [Alexandrie](https://github.com/Smaug6739/Alexandrie) `#archetype:operational_pipeline #purpose:automation` - Gestore di librerie e memoria per AI
- [OpenKB](https://github.com/VectifyAI/OpenKB) `#archetype:operational_pipeline #purpose:automation` - Knowledge Base open source per RAG
- [PageIndex](https://github.com/VectifyAI/PageIndex) `#archetype:operational_pipeline #purpose:automation` - Strumento di indicizzazione vettoriale
- [Agentic AI Landscape](https://github.com/antgroup/agentic-ai-landscape) `#archetype:operational_pipeline #purpose:automation` - Mappa e raccolta dell'ecosistema agentico
- [Crucix](https://github.com/calesthio/Crucix) `#archetype:operational_pipeline #purpose:automation` - Tool sperimentale
- [OpenMontage](https://github.com/calesthio/OpenMontage) `#archetype:operational_pipeline #purpose:automation` - Tool per manipolazione media
- [Headroom](https://github.com/headroomlabs-ai/headroom) `#archetype:operational_pipeline #purpose:automation` - Piattaforma AI integrata
- [SciWrite](https://github.com/labarba/sciwrite) `#archetype:operational_pipeline #purpose:automation` - Tool AI per scrittura scientifica
- [Open Notebook](https://github.com/lfnovo/open-notebook) `#archetype:operational_pipeline #purpose:automation` - Ambiente di notebook sperimentale
- [Guild](https://github.com/mathomhaus/guild) `#archetype:operational_pipeline #purpose:automation` - Sistema di orchestrazione task
- [Memanto](https://github.com/moorcheh-ai/memanto) `#archetype:operational_pipeline #purpose:automation` - Tool di memorizzazione AI
- [CLI Printing Press](https://github.com/mvanhorn/cli-printing-press) `#archetype:operational_pipeline #purpose:automation` - Automazione per pubblicazione via terminale
- [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) `#archetype:operational_pipeline #purpose:automation` - Estrattore di testo da PDF per RAG
- [Heretic](https://github.com/p-e-w/heretic) `#archetype:operational_pipeline #purpose:automation` - Tool e framework sperimentale
- [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus) `#archetype:operational_pipeline #purpose:automation` - Tool di navigazione autonoma per agenti
- [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) `#archetype:operational_pipeline #purpose:automation` - Guida e codice per l'ingegneria AI
- [TDoc](https://github.com/serenakeyitan/tdoc) `#archetype:operational_pipeline #purpose:automation` - Strumento di generazione documentazione
- [Supertonic](https://github.com/supertone-inc/supertonic) `#archetype:operational_pipeline #purpose:automation` - Tool AI per l'audio
- [https://pinperepette.github.io/signal.pirate/articoli/l-agente-non-ha-una-forma.html?t=d](https://pinperepette.github.io/signal.pirate/articoli/l-agente-non-ha-una-forma.html?t=d) `#archetype:operational_pipeline #purpose:automation` - Articolo: L'Agente non ha una forma
- [https://www.langchain.com/blog/the-anatomy-of-an-agent-harness#can-someone-please-define-a-harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness#can-someone-please-define-a-harness) `#archetype:operational_pipeline #purpose:automation` - Articolo che definisce Agent Harness
- [https://www.smartworld.it/news/gemini-memoria-persistente-import-chat-chatgpt-claude.html](https://www.smartworld.it/news/gemini-memoria-persistente-import-chat-chatgpt-claude.html) `#archetype:operational_pipeline #purpose:automation` - Articolo: Gemini porta la memoria persistente in Italia e permette di importare le chat da ChatGPT e Claude
- [https://agentsfromscratch.com/](https://agentsfromscratch.com/) `#archetype:operational_pipeline #purpose:automation` - Learn to build AI agents locally without frameworks


---

## 8. 🌟 Awesome Collections

This file contains huge curated directories and "Awesome" lists of resources.

- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) `#archetype:operational_pipeline #purpose:automation` - Collezione di skill per agenti AI #collection
- [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering) `#archetype:operational_pipeline #purpose:automation` - Risorse, articoli e tool per la costruzione di AI harness #collection
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) `#archetype:operational_pipeline #purpose:automation` - Dataset pubblici per addestramento e validazione #collection
- [Awesome AI Security](https://github.com/ottosulin/awesome-ai-security) `#archetype:operational_pipeline #purpose:automation` - Collezione di risorse sulla sicurezza AI #collection
- [Awesome AI OSINT](https://github.com/ubikron/Awesome-AI-OSINT) `#archetype:operational_pipeline #purpose:automation` - Risorse su Open Source Intelligence con AI #collection
