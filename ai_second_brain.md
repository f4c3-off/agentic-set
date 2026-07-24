# 🧠 AI Second Brain: Knowledge Factory

> **[AGENT INSTRUCTION]**
> You are reading a "Second Brain", now structured as a "Knowledge Factory". Follow the pipeline from 1 to 6 based on the task you need to perform. Each level provides specific skills, tools, and frameworks to acquire, process, store, or produce knowledge. 
> *Nota: Tutti i framework pesanti e orchestratori complessi sono stati spostati in `software_ecosystem.md`. Qui trovi solo tool "Plug & Play", Skill e server MCP installabili direttamente dall'Architetto su agenti host.*

---

## 1. 🔍 Ingest & Research
*Tools for web search, raw information extraction, and standardization into LLM-readable formats.*

### Autonomous Research & Analytical Research (OSINT)
- **[Agent Reach](https://github.com/Panniantong/Agent-Reach)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Skill to give the agent "eyes" on the Internet (Twitter, Reddit, YouTube, GitHub) via CLI.
- **[Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Search engine driven by an AI agent that searches across people and engagement over the last 30 days.
- **[GPT Researcher](https://github.com/assimp/gpt-researcher)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Automates the "Plan → Search → Read → Reflect → Synthesize" cycle.
- **[OWASP Social OSINT Agent](https://github.com/OWASP/SocialOSINTAgent)** `#workflow:osint #role:data_gathering #archetype:intelligence`: OSINT agent focused on social media, images, and text.
- **[Perplexica](https://github.com/ItzCrazyKns/Perplexica)** `#workflow:osint #role:data_gathering #archetype:intelligence`: Privacy-focused AI search engine supporting local and cloud LLMs.
- **[Brave Search MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** `#workflow:osint #role:data_gathering #archetype:intelligence`: MCP Server for parallel web search in full transparency.
- **[Strix](https://github.com/strix-project)** `#workflow:osint #role:security #archetype:intelligence`: CLI utility per penetration testing e validazione OSINT autonoma eseguibile dall'Architetto.
- **[OpenClaw / KiloClaw](https://github.com/OpenClaw/openclaw)** `#workflow:osint #archetype:integration`: Strumenti e fork "Plug & Play" per integrare OSINT, Discord, e Telegram nativamente nell'agente.
- **[CyberScraper 2077](https://github.com/itsOwen/CyberScraper-2077)** `#tool:infrastructure #purpose:api`: Advanced web scraper con bypass Cloudflare, parsing HTML diretto per agenti.
- **[OpenOSINT](https://github.com/OpenOSINT/OpenOSINT)** `#tool:utility #purpose:support`: Analytical Research (OSINT) tool alimentato da automazioni AI (Classic recon tools + LLM).

### Data Extraction: PDF-to-Markdown Solutions
- **[MinerU (by OpenDataLab)](https://github.com/opendatalab/MinerU)** `#workflow:raw_ingestion #tool:extraction`: Uses a vision-language model for unbeatable accuracy on complex layouts.
- **[Marker (by Datalab)](https://github.com/VikParuchuri/marker)** `#workflow:raw_ingestion #tool:extraction`: High-performance conversion model for bulk ingestion.
- **[Docling (by IBM)](https://github.com/DS4SD/docling)** `#workflow:raw_ingestion #tool:extraction`: Enterprise framework (MIT license), runs excellently on CPU.
- **[Unstructured](https://github.com/Unstructured-IO/unstructured)** `#workflow:raw_ingestion #tool:extraction`: Industrial RAG tool for stable pipelines.
- **[MarkItDown](https://github.com/microsoft/markitdown)** `#workflow:raw_ingestion #tool:extraction`: Essential Microsoft utility for quick text document conversion.
- **[Omniparse](https://github.com/adithya-s-k/omniparse)** `#tool:infrastructure #purpose:api`: Estrazione di audio, video, web, docs in Markdown. Molto flessibile come coltellino svizzero.
- **[Hyper-Extract](https://github.com/yifanfeng97/hyper-extract)** `#workflow:raw_ingestion #workflow:knowledge_base #tool:extraction`: Extract and analyze documents directly into linked markdown notes.
  - **💡 Tips per The Architect**: L'Architetto DEVE automatizzare tutti i passaggi intermedi tramite questa libreria per fornire una pipeline "documento -> note collegate" senza intervento umano.

---

## 2. 🧠 Sense-Making & Strategy
*Frameworks for breaking down complex problems, deliberating, and logically structuring information.*

- **[Strategy Consultant Frameworks](https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks)** `#workflow:reasoning`: Transforms agent reasoning from simple text into BCG/McKinsey logic.
- **[CC Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills)** `#workflow:reasoning`: Over 18 mental models (e.g., OODA Loop, useful for tactics).

---

## 3. 🗂️ Knowledge Management & Storage
*The "foundations" where knowledge is stored, structured, and maintained over time by the Agent.*

- **[Second Brain](https://github.com/NicholasSpisak/second-brain)** `#workflow:knowledge_base`
- **[Ariadne](https://github.com/pariyar07/ariadne)** `#workflow:knowledge_base`: Agents can map and use complex Obsidian architectures.
- **[ICM Architect and ICM Core Repo](https://github.com/RinDig/Interpreted-Context-Methdology)** `#workflow:knowledge_base`: Transforms standard file folders into an environment natively understandable by AI.
- **[Obsidian Skills (gmickel & kepano)](https://github.com/kepano/obsidian-skills)** `#workflow:knowledge_base`: Teaches the AI to handle JSON Canvas.
- **[Graphify](https://github.com/Graphify-Labs/graphify)** `#workflow:knowledge_base`: Drastic token reduction, semantic correlation understanding within a true local Knowledge Graph.
- **[Agentic Stack](https://github.com/codejunkie99/agentic-stack)** `#workflow:knowledge_base`: True episodic memory (`lessons.jsonl`); agent doesn't make the same mistake twice.
- **[OpenWiki](https://github.com/langchain-ai/openwiki)** `#workflow:knowledge_base`: Scans directories and automatically produces interlinked, readable wikis.
- **[Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)** `#workflow:knowledge_base`: Ready-to-use MCP for vector search of files and text.
- **[MemPalace](https://github.com/MemPalace/mempalace)** `#tool:infrastructure #purpose:api`: High-performance vector AI memory system. Memorizza terabyte di testo grezzo da interrogare occasionalmente.

---

## 4. ✨ Polish & Aesthetic
*Stylistic alignment: taste, art direction, semantic refinement, and formatting.*

- **[Taste Skill](https://github.com/leonxlnx/taste-skill)** `#workflow:refinement`: Removes classic GPT "slop" (buzzwords like "Crucial", "Revolutionary").
- **[no-ai-slop (by petergyang)](https://github.com/petergyang/no-ai-slop)** `#workflow:refinement`: Specialized skill to improve AI-generated writing by detecting and removing over 20 common patterns of "AI slop".
- **[Awesome NotebookLM Prompts](https://github.com/serenakeyitan/awesome-notebookLM-prompts)** `#workflow:refinement`: Prompts for complex NotebookLM-style summaries.
- **[The Gemini Notebook Style Pack](https://truetraction.notion.site/The-Gemini-Notebook-Style-Pack-formerly-NotebookLM-3a4eca2dc63381eba726d5e10e15ca50)** `#workflow:refinement`: Un set di stili e pattern specifici per trasformare output AI crudi in Knowledge Notes formattate e professionali per Gemini/NotebookLM.
- **[StyleSeed](https://github.com/bitjaru/styleseed)** `#workflow:refinement`: Gives AI an "eye" for design (color consistency, spacing, typography).
- **[Awesome Design Markdown (by VoltAgent)](https://github.com/VoltAgent/awesome-design-md)** `#workflow:refinement #tool:collection`: Una collezione curata per il design avanzato in Markdown. Utilissima per gli agenti per generare UI/UX, report visivamente accattivanti e documentazione estetica all'interno del Second Brain.

---

## 5. 📦 Output & Production
*The factory's "printers": tools and engines to generate complete, verified, ready-to-use deliverables.*

### General Production
- **[agentic (by transitive-bullshit)](https://github.com/transitive-bullshit/agentic)** `#tool:mcp`: Istantanea funzionalità API-to-MCP per convertire servizi in contesti agentici (archiviato ma utile storicamente).
- **[Ego-Lite (by citrolabs)](https://github.com/citrolabs/ego-lite)** `#tool:automation`: Un browser basato su Chromium progettato per essere condiviso da umani e agenti (preserva log-in, cookies, estensioni per automazioni).
- **[Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar)** `#tool:utility #purpose:support`: Tool per connettere Claude a database accademici per citazioni rigorose in output finali.
- **[Flint](https://github.com/microsoft/flint)** `#tool:infrastructure #purpose:api`: Linguaggio chart-friendly per LLM (creazione automatica di grafici corretti nei report).

### Video Production & Editing
- **[video-shotcraft (by Vincentwei1021)](https://github.com/Vincentwei1021/video-shotcraft)** `#workflow:production #tool:video`: Una skill di produzione video per Claude Code e Codex con template "production-ready" per creare cinematic product video usando Remotion.
- **[ai-video-editor (by MartinDelophy)](https://github.com/MartinDelophy/ai-video-editor)** `#workflow:production #tool:video`: Video editor AI local-first, browser-based, con supporto ONNX, Whisper, e talking avatars.
- **[FableCut](https://github.com/fablecut/fablecut)** `#tool:infrastructure`: Generazione video (JS editor) guidabile localmente via script per creare trailer di indagini OSINT.

---

## 6. 🛠️ Core Toolbelt & MCP Servers
*Core infrastructure, standard prompt collections, and standard MCPs.*

### Standard MCP Servers
- **[A2A Search MCP](https://github.com/tadas-github/a2asearch-mcp)** `#tool:mcp`: Il "Google degli agenti". L'agente può usarlo per trovare e autoinstallarsi nuovi MCP Server per compiti imprevisti.
- **Context7 MCP** `#tool:mcp`: Per iniezione di documentazione in tempo reale e prevenzione allucinazioni.
- **Playwright MCP** `#tool:mcp`: Per automazione web e visual debugging (perfetto per OSINT o QA).
- **Postgres MCP Pro / Supabase** `#tool:mcp`: Per accesso e analisi diretta di database SQL.
- **GitHub MCP** `#tool:mcp`: Per gestione issue, PR e CI/CD.

### Tool & Script Collections
- **[agentic-awesome-skills (by sickn33)](https://github.com/sickn33/agentic-awesome-skills)** `#tool:collection`: Control plane locale per agenti con oltre 1.900 skill agentiche, discovery, e supporto MCP locale (compatibile con Claude Code, Cursor, Gemini).
- **[skills (by mattpocock)](https://github.com/mattpocock/skills)** `#tool:collection`: Collezione di skill pratiche da installare (via CLI o plugin) progettata "per veri ingegneri software" (TDD, review architetturale, debugging).
- **[OneCLI](https://github.com/onecli)** `#tool:security`: OSS credential gateway che mantiene i secret (chiavi API) fuori dalla vista diretta degli agenti AI.
- **[Claude Skills Collection](https://github.com/abubakarsiddik31/claude-skills-collection) and [Agent Skills](https://github.com/addyosmani/agent-skills)** `#tool:collection`: Script Bash, File System, Git.
- **[Application Skills](https://github.com/membranedev/application-skills)** `#tool:collection`: Macros to control desktop apps via UI scripts.
- **[AutoSkills](https://github.com/midudev/autoskills)** `#tool:collection`: Instant stack setup.
- **Prompt Collections (Prompts.chat, Agentic Set, Anthropic Library, LangChain Hub)** `#tool:collection`: Massive databases for setup configurations and roles.
- **[Fabric](https://github.com/danielmiessler/fabric)** `#tool:collection`: The ultimate CLI framework for the Bash ecosystem. Estrai i pattern utili in plain text.
- **[Prompt Master](https://github.com/nidhinjs/prompt-master)** `#tool:infrastructure`: Gestione e test di collezioni di prompt (versioning per prompt di intelligence e accademici).

### Utilities Core
- **[Aict](https://github.com/aict-tools/aict)** `#tool:utility`: Unix coreutils native JSON/XML output. Elimina la necessità per l'agente di usare `sed/awk` su log complessi.
- **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** `#tool:core`: Gateway to save tokens and route traffic.
- **[Colibri](https://github.com/JustVugg/colibri)** `#tool:core`: Enables local execution of giant models (offline, max privacy).
- **[VulnHunter](https://github.com/capitalone/vulnhunter)** `#tool:security`: Agentic security tool (Capital One). Passaci i framework OSINT sconosciuti prima di eseguirli in locale!
