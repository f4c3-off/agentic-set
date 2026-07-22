# 🏗️ Stack Configurations (Architectural Archetypes)

This document defines the **Archetypes** (Stack Configurations) that the Architect uses to generate ICM payloads. Each archetype is a pre-tested combination of pipelines (folder structure), workflows (sub-agents), and external skills.

The Architect, after the Triage interview, identifies which of these Archetypes fits the user's project and triggers its deployment.

---

## Archetype 1: Intelligence & Academy OS (Knowledge Base)
- **Tag**: `#tipo:knowledge_base`, `#tipo:ricerca_analitica`
- **Objective**: Build an autonomous "Second Brain" for deep research, academic paper ingestion, OSINT, and the generation of wikis or courses.
- **Pipeline (ICM Folders)**:
  - `0 - SYSTEM/`
    - `0.1 - RULES/`
    - `0.2 - SKILLS/`
      - `tmp/`
  - `1 - SOURCES/`
    - `1.1 - RAW/` (Raw data, PDFs, transcripts)
    - `1.2 - DRAFTS/` (Structuring and human validation)
    - `1.3 - ANALYSIS/`
      - `1.3.1 - WORKFLOW/` (Inbox for loops and fact-checking)
  - `2 - WIKI/` (Promoted notes, ontology, glossary)
  - `3 - OUTPUT/` (Generated reports and final deliverables)
  - `4 - WORKSPACE/` (Area for experiments and scripts)
- **Workflows (Generated Sub-Agents)**:
  - **Explorer**: Analyzes files in `RAW`, executes OSINT queries, and creates extracts in `ANALYSIS`.
  - **Critic**: Applies the `analyze_claims` (Fabric) pattern to find logical fallacies in documents in `ANALYSIS`.
  - **Librarian**: Operates in `WIKI/` to connect the dots, update indices (MOC), and compile the glossary.
- **Skill Discovery Tags (Dynamic Tool Search)**: 
  - `Tags to search`: `#workflow:osint`, `#workflow:ricerca_analitica`, `#workflow:knowledge_base`, `#workflow:ingestion_raw`
  - `Source repository`: [https://github.com/f4c3-off/agentic-set](https://github.com/f4c3-off/agentic-set)

## Archetype 2: Operational Pipeline (Code & Dev)
- **Tag**: `#tipo:sviluppo_software`, `#tipo:pipeline_operativa`
- **Objective**: Iterative generation and validation of code, scripts, or engineering projects.
- **Pipeline (ICM Folders)**:
  - `0 - SYSTEM/`
    - `0.1 - RULES/`
    - `0.2 - SKILLS/`
      - `tmp/`
  - `1 - REQUIREMENTS/` (User specifications)
  - `2 - PLANNING/` (Architecture and design)
  - `3 - BUILD/` (Source code)
  - `4 - REVIEW/` (Testing and audit)
- **Workflows (Generated Sub-Agents)**:
  - **Coder**: Writes code in `BUILD/` based on `REQUIREMENTS`.
  - **Reviewer**: Reads code and creates issues in `REVIEW/`.
- **Suggested Core Skills & Tools**:
  - `Codebase Memory MCP` (To read the context of complex files)
  - `jcode` (Rust code executor)

## Archetype 3: Audit & Security
- **Tag**: `#tipo:cybersecurity`, `#tipo:audit`
- **Objective**: System scanning, vulnerability analysis, and risk reporting.
- **Pipeline (ICM Folders)**:
  - `0 - SYSTEM/`
    - `0.1 - RULES/`
    - `0.2 - SKILLS/`
      - `tmp/`
  - `1 - ASSETS/` (Code, logs, or architecture descriptions to test)
  - `2 - SCANNING/` (Results from automated tools)
  - `3 - THREAT_MODELING/` (Agent analysis)
  - `4 - REMEDIATION/` (Proposed fixes)
- **Workflows (Generated Sub-Agents)**:
  - **Red Team Agent**: Applies the `create_threat_model` pattern to look for flaws.
  - **Blue Team Agent**: Suggests mitigations and writes fixes in `REMEDIATION/`.
- **Suggested Core Skills & Tools**:
  - `OWASP OSINT Agent` 
  - `Fabric (create_threat_model)`
