# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **document repository** for a tender/proposal project related to a modular brine plant (Módulo de Salmuera) in Taltal. The repository contains technical specifications, economic proposals, technical offers, and project schedules in PDF format.

**Project Context:**
- Project code: BAE 12803 - PLANTA MODULAR
- Supplier: BW Water
- Involved parties: ADASA (scheduling)
- Document types: Technical bases, economic offers, technical proposals, schedules

## Repository Structure

```
MODULO DE SALMUERA TALTAL/
├── .claude/                     # Claude Code configuration and skills
│   ├── README.md
│   └── skills/
│       └── revision-tecnica/    # Technical review skill
│           └── SKILL.md
├── BASES TECNICAS/              # Technical specifications and tender documents
│   ├── BAE 12803 PLANTA MODULAR - VF_parte 1.pdf
│   ├── BAE 12803 PLANTA MODULAR - VF_parte 2.pdf
│   ├── P00-IT-00-000-101 (CODIFICACION GENERAL).pdf
│   ├── P22-ET-09-000-001-0 (ET Módulo).pdf
│   └── P22-IT-09-000-001-0 (PIE BASE).pdf
├── OFERTA ECONOMICA/            # Economic proposal and budget
│   ├── Doc1.3_02 Presupuesto Itemizado 12803_BWWASep.182025_s.pdf
│   └── OFERTA ECONOMICA BW WATER.pdf
├── OFERTA TECNICA/              # Technical proposal (multi-part)
│   ├── OFERTA TECNICA BWWATER PARTE 1.pdf
│   ├── OFERTA TECNICA BWWATER PARTE 2.pdf
│   ├── OFERTA TECNICA BWWATER PARTE 3.pdf
│   └── OFERTA TECNICA BWWATER PARTE 4.pdf
├── PROGRAMAS/                   # Project schedules
│   ├── PROGRAMA BASE ADASA NOVIEMBRE 2025.pdf
│   └── Project TalTal-Preliminary Taltal Schedule.pdf
└── REVISIONES/                  # Review milestones and compliance tracking
    └── Hitos de revision.md
```

## Document Organization

### BASES TECNICAS (Technical Specifications)
Contains the tender requirements and technical specifications:
- **BAE 12803 PLANTA MODULAR**: Main tender document (2 parts)
- **P00-IT-00-000-101**: General codification standards
- **P22-ET-09-000-001-0**: Module specifications (ET = Especificación Técnica)
- **P22-IT-09-000-001-0**: Base engineering document (PIE BASE)

### OFERTA ECONOMICA (Economic Proposal)
BW Water's economic offer:
- **OFERTA ECONOMICA BW WATER.pdf**: Main economic proposal
- **Presupuesto Itemizado**: Itemized budget dated September 18, 2025

### OFERTA TECNICA (Technical Proposal)
BW Water's technical response split into 4 parts for file size management

### PROGRAMAS (Schedules)
Project timelines:
- **PROGRAMA BASE ADASA NOVIEMBRE 2025**: Baseline schedule from ADASA
- **Project TalTal-Preliminary Taltal Schedule**: Preliminary project timeline

### REVISIONES (Review Milestones)
Tracking of all technical, compliance, and quality reviews:
- **Hitos de revision.md**: Centralized log of all project reviews with verdicts and observations
- Each review includes: date, reviewer, documents reviewed, criteria, results, and conclusions
- Reviews are numbered sequentially (e.g., REVISIÓN #001, #002, etc.)

### .claude (Claude Code Configuration)
Claude Code skills and configuration:
- **skills/revision-tecnica/**: Specialized skill for technical reviews and compliance checking
  - Provides structured review process
  - Standardized documentation format
  - Project-specific guidelines and criteria
  - Integrates with REVISIONES/Hitos de revision.md
- See `.claude/README.md` for complete skill documentation

## Document Naming Conventions

The project uses a structured coding system:
- **PXX-YY-ZZ-AAA-BBB-V** format where:
  - P = Project identifier
  - XX = Project number (e.g., 00, 22)
  - YY = Document type (IT = Ingeniería Técnica, ET = Especificación Técnica)
  - ZZ = Discipline code (09 = related to modules)
  - AAA-BBB = Sequential numbering
  - V = Version number

## Working with This Repository

### Viewing Documents
All documents are in PDF format. To work with them:
- PDFs can be read using the Read tool (Claude can extract text and visual content)
- For document comparison, extract text from multiple PDFs and analyze differences
- For schedule analysis, focus on the PROGRAMAS directory

### Common Tasks

**Extracting information from tender documents:**
```bash
# Use Read tool on specific PDFs in BASES TECNICAS/
```

**Comparing proposals:**
```bash
# Use Read tool to extract content from OFERTA TECNICA parts
# Compare against requirements in BASES TECNICAS
```

**Schedule analysis:**
```bash
# Use Read tool on schedule PDFs in PROGRAMAS/
```

**Finding specific technical requirements:**
```bash
# Search through BASES TECNICAS documents
# Reference P22-ET-09-000-001-0 for module specifications
```

**Documenting reviews:**
```bash
# All reviews must be documented in REVISIONES/Hitos de revision.md
# Use the provided template to add new review entries
# Include: date, documents reviewed, criteria, verdict (✅/❌/⚠️), and observations
```

## Language and Context

- **Primary language**: Spanish (Chile)
- **Industry**: Water treatment / Desalination / Brine management
- **Project type**: Modular plant tender/proposal
- **Document date range**: May 2025 - November 2025

## Key Information

When analyzing documents in this repository:
1. The BASES TECNICAS define the requirements (client side)
2. The OFERTA TECNICA is BW Water's response to those requirements
3. The OFERTA ECONOMICA contains pricing and budget information
4. The PROGRAMAS show project timelines and milestones
5. Cross-reference document codes (PXX-YY-ZZ format) when analyzing compliance

## Review Process

All reviews performed on this project must be documented in [REVISIONES/Hitos de revision.md](REVISIONES/Hitos de revision.md).

### Review Documentation Requirements:
1. **Sequential numbering**: Each review must have a unique ID (REVISIÓN #001, #002, etc.)
2. **Complete metadata**: Date, reviewer name, and review type
3. **Clear scope**: Specify which documents were reviewed and evaluation criteria
4. **Verdict**: Use standard symbols:
   - ✅ CUMPLE (Complies)
   - ❌ NO CUMPLE (Does not comply)
   - ⚠️ CUMPLE CON OBSERVACIONES (Complies with observations)
5. **Observations**: List specific findings, discrepancies, or notes
6. **Conclusion**: Summary of review outcome and any required actions

### Review Types:
- **Técnica** (Technical): Technical compliance reviews
- **Económica** (Economic): Budget and cost reviews
- **Programa** (Schedule): Timeline and milestone compliance
- **Cumplimiento** (Compliance): Regulatory or contractual compliance
- **Otra** (Other): Any other type of review

### When to Document a Review:
- Whenever comparing BW Water's proposal against ADASA or client requirements
- After analyzing technical specifications for compliance
- When evaluating schedule adherence
- After cost or budget analysis
- Any formal review or verification activity
