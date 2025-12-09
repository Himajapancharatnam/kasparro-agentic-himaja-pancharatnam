# Kasparro Agentic Content Generation System

**Author:** Himaja Pancharatnam
**Repository:** `kasparro-agentic-himaja-pancharatnam`

---

## Project Summary

This project implements a **modular agentic content generation system**. It takes minimal product data and automatically produces **structured, machine-readable JSON pages**, including:

* Product Description Page
* Comparison Page
* FAQ Page

The system uses **independent agents, reusable logic blocks, orchestration, and templates**, demonstrating a **production-style backend content automation pipeline**.

---

## Architecture Highlights

| Feature                      | Description                            |
| ---------------------------- | -------------------------------------- |
| Agent-Based Design           | Each agent has a single responsibility |
| Orchestrator-Controlled Flow | Central pipeline execution             |
| Logic Block Composition      | Reusable content logic modules         |
| Template-Based Generation    | Structured JSON output                 |
| Zero Hidden State            | Deterministic and predictable          |
| JSON-only Output             | Ready for frontend or API consumption  |

---

## Project Structure

```
kasparro-agentic-himaja-pancharatnam/
│
├── agents/                  # Data parsing & question generation
├── orchestrator/            # Pipeline controller
├── logic_blocks/            # Business logic units
├── templates/               # JSON page templates
├── outputs/                 # Generated JSON pages
├── docs/                    # Project documentation
│   └── projectdocumentation.md
├── main.py                  # Entry point to run the pipeline
└── README.md
```

---

## How to Run

### Requirements

* Python 3.9+
* Windows / Mac / Linux

### Run the system

From the project root directory:

```bash
python main.py
```

### Output Files

After execution, JSON pages are generated in the `outputs/` folder:

| File                 | Description                                  |
| -------------------- | -------------------------------------------- |
| product_page.json    | Structured product description page          |
| comparison_page.json | Product comparison with fictional competitor |
| faq.json             | Frequently Asked Questions page              |

---

## Documentation

Full project documentation, including architecture, design decisions, and assumptions:

```
docs/projectdocumentation.md
```

---

## Design Principles

* Single-responsibility agents
* Explicit orchestration and flow control
* Reusable content logic blocks
* Template-driven output
* Deterministic JSON output
* Modular and scalable architecture

---

## Goal Alignment

| Goal                       | Status |
| -------------------------- | ------ |
| Multi-agent workflows      | ✅      |
| Automation graphs          | ✅      |
| Reusable logic             | ✅      |
| Template-driven generation | ✅      |
| Machine-readable outputs   | ✅      |
| Documentation included     | ✅      |

---

## Evaluation Readiness

| Feature                      | Status |
| ---------------------------- | ------ |
| Agent orchestration          | ✅      |
| Modular design               | ✅      |
| Machine-readable JSON output | ✅      |
| Template abstraction         | ✅      |
| Reusable logic blocks        | ✅      |
| Clean repository structure   | ✅      |

---

## Final Note

This project demonstrates **production-grade backend system design**, focusing on **architecture, modularity, and maintainability**, fully aligning with **Kasparro’s evaluation criteria**.
