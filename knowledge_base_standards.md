# 📖 Knowledge Base Standards (OKF & Style Guide)

This document defines the architectural and stylistic standards for the generation and maintenance of knowledge bases (Second Brain) by AI agents. Following these rules ensures that the vault remains interoperable, readable, and scalable.

---

## 1. The "OKF" Standard (Open Knowledge Format) `#workflow:okf_standard` `#workflow:formatting`

OKF is an interoperability standard designed to enable seamless dialogue between original Markdown, Graph-RAG indexing engines, and agents.

### Strict YAML Frontmatter
Every note MUST include a YAML frontmatter. NEVER insert the `#` character into YAML tags, as it invalidates the syntax.

```yaml
---
type: "concept" # e.g.: concept, report, profile, log
title: "Note Title"
description: "1-line summary of the content"
parent: "[[MacroTopicName]]"
timestamp: 2026-06-15T12:00:00Z # ISO-8601 format
resource: "[[SourceFileName]]"
tags:
  - MacroTopic/subtag
aliases: ["Other Name", "Synonym"]
status: active
priority: p0
---
```

### Callouts and Alerts
Use native callout syntax (Obsidian/GitHub style) instead of simple bullet points to highlight semantic blocks:
- `> [!note]` — General information
- `> [!abstract]` — Initial summary
- `> [!warning]` — Medium alert
- `> [!danger]` or `> [!caution]` — Critical threat
- `> [!tip]` — Operational tip

### Wikilinks and Block IDs
Use `[[NoteName]]` to link notes and build the knowledge graph.
To reference specific paragraphs, use Block IDs: `This is a paragraph. ^my-block-id`.

---

## 2. Style and Syntax Rules (Wiki-Style)

### Inverted Pyramid Layout (MoSS)
Every note must function as a continuous monograph. 
- **First line:** Maximum, dense definition of the topic. Anyone reading only the first paragraph must understand WHAT it is, WHERE it is used, and WHY it is relevant.
- **Titles and Redirects:** Use the most established term as the title (H1). Synonyms should be placed in the YAML `aliases` to avoid knowledge graph fragmentation.

### Operational Neutrality (NPOV)
The agent must adopt a **Neutral Point of View**. The note must not take personal stances ("We should", "It is essential"). It must report the perspectives present in the literature. If a framework is criticized, it should be included in the "Current Consensus and Debate" section.

### Anti-Slop & Prose Curation
Reject informational fragmentation and low-value-add formats ("AI-slop"):
- **Bullet Point Threshold:** Bulleted lists must never serve as the skeleton of the monograph. A maximum of **10% of the total lines** of the note body may contain bullet points. Information must be expressed through continuous, argumentative prose.
- **Ban on Emojis:** Avoid decorative emojis in encyclopedic texts, titles, tags, or comments to maintain a formal and scientific tone. (Note: Emojis may be used as folder or macro-category icons, but not within the body text).

---

## 3. The File Clerk Pipeline (Advanced ICM Analytics)
Inspired by the Interpretable Context Methodology (ICM), the Agent's operating environment in analytical projects must not be flat. The intelligence of the system resides in the folder hierarchy, which acts as "Processing Stages". 

Every Knowledge Base or analytical project must implement a sequential folder pipeline structured as follows:
1. **`1.1 - RAW/` (Input Ingestion)**: Here the user deposits raw data. No alterations occur in this folder.
2. **`1.3 - ANALISI/` and `WORKFLOW/` (Enrichment and Analysis)**: A dedicated workflow reads the RAW data and autonomously enriches it via web searches (using specific skills such as scraping or OSINT). The results are "extracts" or intermediate reports saved in the analysis subfolders.
3. **`BOZZE/` (Structuring)**: A second Agent collects the analytical extracts and formats them into structured drafts (using the OKF standard), ready for the user's Review Gate.
4. **`WIKI/` (Promotion and Ontology)**: After human approval, a Librarian Agent moves the draft into the official wiki. This agent has the specific task of linking the note to the rest of the semantic graph, updating indices (MoCs), and automatically compiling the glossary.

This segregation of tasks prevents cognitive overload: no single agent does "everything at once", but rather the file itself travels through the assembly line.
