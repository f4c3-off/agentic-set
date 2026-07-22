# 📜 CHANGELOG & CORE MEMORY (Tri-Repo Architecture)

Questo file è la "Memoria di Sistema" delle decisioni architetturali prese. Puoi portarlo sul nuovo PC per assicurarti che il contesto dell'evoluzione all'ICM non vada mai perso.

## [Versione 2.0] - Il Passaggio all'ICM Puro
Il paradigma "The Architect Project" (framework monolitico) è stato deprecato. Abbiamo stabilito una **Architettura a 3 Pilastri (Tri-Repo)**:

### 1. `the-architect` (L'Esecutore)
- **Logica**: Una singola Skill (`SKILL.md`) che funge da costruttore.
- **Funzione**: Intervista l'utente, seleziona l'archetipo, esegue lo scaffolding (creazione delle cartelle `1.1`, `1.2`, ecc.) e genera il `0-SISTEMA/CONTEXT.md` (Registro Globale).
- **Loop Operativo**: L'Architetto **NON** è nel loop operativo. Costruisce le stanze e muore. Il Master Orchestrator (o l'utente in chat) invoca i sub-agenti.

### 2. `agentic-set` (L'App Store)
- L'ex `ai-agent-resources`. Non esegue codice, è solo un database di conoscenze consultabile.
- **Scoperta**: L'Architetto usa i tool di sistema (`grep`) per scansionare tag come `#workflow:osint #domain:osint` o `#persona:explorer #role:data_gathering`.
- **Templates Isolati**: I ruoli sono stati separati fisicamente in file granulari all'interno di `templates/`:
  - `esploratore.md` (Data Gathering in `1.1 - RAW`)
  - `reporter.md` (Critical Thinking in `1.2 - BOZZE`)
  - `bibliotecario.md` (Knowledge Management e standard OKF in `1.4 - KNOWLEDGE_BASE`)
  - `sherman.md` (Red Teaming, dottrina Sherman Kent e probabilità calibrata in `1.3 - ANALISI`)

### 3. `architect-docs` (L'Accademia)
- Un repository separato unicamente per la teoria.
- Contiene `architecture_philosophy.md` (la transizione da The Architect Project).

## Principi Guida Ereditati (Memoria Storica)
Tutto il sistema si fonda sui principi di **Jake Van Clief**:
1. **Folders over Agents**: Se un problema può essere risolto spostando un file in una cartella con un `CONTEXT.md`, non serve un framework.
2. **La morte dei Silos**: L'architettura è il filesystem. Trasparenza totale.
3. **Code-as-Action**: Per compiti computazionali complessi, gli agenti scrivono ed eseguono script temporanei in `0-SISTEMA/tmp/`, mantenendo intatta la cartella delle Skill.
4. **Human-in-the-Loop**: La gestione degli errori non avviene tramite complicati DAG Python di fallback, ma tramite la chat. L'agente si ferma e chiede all'operatore.

---
*Status: Operativo. Pronto per il deployment su qualsiasi macchina locale dotata di agenti CLI o GUI compatibili (Antigravity, Goose, Claude Code).*
