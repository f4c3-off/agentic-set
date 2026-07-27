# 🌐 Software Ecosystem & Frameworks

Questo documento raccoglie framework, piattaforme, ottimizzatori e collezioni che costituiscono l'infrastruttura dell'ecosistema agentico. A differenza degli strumenti in `ai_second_brain.md`, questi progetti sono spesso piattaforme standalone, orchestratori complessi o librerie a basso livello che richiedono installazione e configurazione esterne agli agenti (come Claude Code o Goose).

## 1. 🏗️ Standalone Agent Frameworks & Orchestrators
Questi framework servono a costruire o gestire flotte di agenti autonomi:

- **[STORM (Stanford)](https://github.com/stanfordnlp/storm)** `#workflow:analytical_research`: Framework for asynchronous analytical research (digital experts debating).
- **[Agent Laboratory](https://github.com/agent-laboratory/agent-laboratory)** `#workflow:analytical_research`: Framework for the full research cycle.
- **[Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence)** `#archetype:operational_pipeline`: Framework multi-agente per deliberazioni avanzate.
- **[Agentic OS](https://github.com/KbWen/agentic-os)** `#archetype:operational_pipeline`: Sistema operativo con regole enforce (Plan, Build, Review).
- **[PydanticAI](https://github.com/pydantic/pydantic-ai)** `#archetype:operational_pipeline`: Framework emergente type-safe e code-first per agenti.
- **[Mastra](https://github.com/mastra-ai/mastra)** `#archetype:operational_pipeline`: Framework di riferimento per l'ecosistema TypeScript/JavaScript.
- **[Google ADK (Agent Development Kit)](https://github.com/google/agent-development-kit)** `#archetype:operational_pipeline`: Kit modulare per lo sviluppo di agenti enterprise.
- **[EpicStaff](https://github.com/EpicStaff/EpicStaff)** `#archetype:operational_pipeline`
- **[PraisonAI](https://github.com/MervinPraison/PraisonAI)** `#archetype:operational_pipeline`
- **[Agent Reach](https://github.com/Panniantong/Agent-Reach)** `#archetype:operational_pipeline`
- **[OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)** `#archetype:operational_pipeline`
- **[GOD](https://github.com/XiaoLuoLYG/GOD)** `#archetype:operational_pipeline`
- **[Hivemind](https://github.com/activeloopai/hivemind)** `#archetype:operational_pipeline`
- **[Bytechef](https://github.com/bytechefhq/bytechef)** `#archetype:operational_pipeline`
- **[Agentic Inbox](https://github.com/cloudflare/agentic-inbox)** `#archetype:operational_pipeline`
- **[Agency Agents](https://github.com/msitarzewski/agency-agents)** `#archetype:operational_pipeline`
- **[Omnigent](https://github.com/omnigent-ai/omnigent)** `#archetype:operational_pipeline`
- **[Ouroboros](https://github.com/razzant/ouroboros)** `#archetype:operational_pipeline`
- **[Ruflo](https://github.com/ruvnet/ruflo?utm_source=chatgpt.com)** `#archetype:operational_pipeline`
- **[OpenFugu](https://github.com/trotsky1997/OpenFugu)** `#archetype:operational_pipeline`
- **[Clowder AI](https://github.com/zts212653/clowder-ai)** `#archetype:operational_pipeline`
- **[Paperclip](https://github.com/paperclipai/paperclip)** `#archetype:operational_pipeline`
- **[GStack](https://github.com/garrytan/gstack)** `#archetype:operational_pipeline`
- **[AutoResearch](https://github.com/karpathy/autoresearch)** `#archetype:operational_pipeline`
- **[Midday](https://github.com/midday-ai/midday)** `#archetype:operational_pipeline`
- **[Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar)** `#archetype:operational_pipeline`
- **[Claw Empire](https://github.com/GreenSheep01201/claw-empire)** `#archetype:operational_pipeline`
- **[AI Job Search](https://github.com/MadsLorentzen/ai-job-search)** `#archetype:operational_pipeline`
- **[OpenOSINT](https://github.com/OpenOSINT/OpenOSINT)** `#archetype:operational_pipeline`
- **[Alexandrie](https://github.com/Smaug6739/Alexandrie)** `#archetype:operational_pipeline`
- **[OpenKB](https://github.com/VectifyAI/OpenKB)** `#archetype:operational_pipeline`
- **[PageIndex](https://github.com/VectifyAI/PageIndex)** `#archetype:operational_pipeline`
- **[Crucix](https://github.com/calesthio/Crucix)** `#archetype:operational_pipeline`
- **[OpenMontage](https://github.com/calesthio/OpenMontage)** `#archetype:operational_pipeline`
- **[SciWrite](https://github.com/labarba/sciwrite)** `#archetype:operational_pipeline`
- **[Open Notebook](https://github.com/lfnovo/open-notebook)** `#archetype:operational_pipeline`
- **[Guild](https://github.com/mathomhaus/guild)** `#archetype:operational_pipeline`
- **[Memanto](https://github.com/moorcheh-ai/memanto)** `#archetype:operational_pipeline`
- **[CLI Printing Press](https://github.com/mvanhorn/cli-printing-press)** `#archetype:operational_pipeline`
- **[OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf)** `#archetype:operational_pipeline`
- **[Heretic](https://github.com/p-e-w/heretic)** `#archetype:operational_pipeline`
- **[Odysseus](https://github.com/pewdiepie-archdaemon/odysseus)** `#archetype:operational_pipeline`
- **[AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** `#archetype:operational_pipeline`
- **[TDoc](https://github.com/serenakeyitan/tdoc)** `#archetype:operational_pipeline`
- **[Supertonic](https://github.com/supertone-inc/supertonic)** `#archetype:operational_pipeline`
- **[Lunaris](https://github.com/PouyanJay/lunaris)** `#archetype:operational_pipeline`
- **[Dair Academy Plugins](https://github.com/dair-ai/dair-academy-plugins)** `#archetype:operational_pipeline`
- **[Baoyu Design](https://github.com/JimLiu/baoyu-design)** `#archetype:operational_pipeline`

## 2. 🎮 Framework per la Gestione di Agenti (IDE & Harness)
Strumenti che gestiscono agenti locali o flotte parallele:
- **[CAMEL-AI](https://github.com/camel-ai/camel)**: Un framework multi-agente avanzato e una piattaforma di ricerca open-source. Estremamente focalizzato sulle interazioni cooperative tra agenti (role-playing framework) per simulazioni complesse.
- **[Bardeen AI](https://github.com/bardeen-ai)**: Piattaforma di automazione (browser-based) focalizzata sul workflow agentico per delegare all'AI task manuali all'interno del sistema operativo o browser.
- **[stablyai/orca](https://github.com/stablyai/orca)** `#archetype:operational_pipeline`: Un Agent Development Environment (ADE) per gestire una flotta di agenti paralleli (Claude Code, Cursor, ecc.).
- **[Agentic AI Landscape](https://github.com/antgroup/agentic-ai-landscape)** `#archetype:operational_pipeline`

## 3. ⚡ Token Optimizers & Core Libraries
Librerie a basso livello per l'ottimizzazione del ragionamento o della memoria:
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** `#archetype:operational_pipeline`: Ottimizza le interazioni LLM comprimendo output, RAG e log (riduce l'uso dei token fin oltre il 60%). Da usare con tokenjuicer e altre librerie simili.

## 4. 🌟 Awesome Collections
Directory curate di risorse agentiche:
- **[Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills)** `#collection`
- **[Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering)** `#collection`
- **[Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)** `#collection`
- **[Awesome AI Security](https://github.com/ottosulin/awesome-ai-security)** `#collection`
- **[Awesome AI OSINT](https://github.com/ubikron/Awesome-AI-OSINT)** `#collection`

## 5. Articoli & Risorse
- [L'Agente non ha una forma](https://pinperepette.github.io/signal.pirate/articoli/l-agente-non-ha-una-forma.html?t=d) `#archetype:operational_pipeline`
- [The anatomy of an agent harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness#can-someone-please-define-a-harness) `#archetype:operational_pipeline`
- [Gemini porta la memoria persistente...](https://www.smartworld.it/news/gemini-memoria-persistente-import-chat-chatgpt-claude.html) `#archetype:operational_pipeline`
- [Agents from Scratch](https://agentsfromscratch.com/) `#archetype:operational_pipeline`
