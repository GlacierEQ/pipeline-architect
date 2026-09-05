# Pipeline Architect

Meta-pipeline that builds production-grade pipelines with skill integration, connector wiring, and sequential thinking enforcement.

## Quick Start

```bash
# Build a pipeline from concept
python3 scripts/architect.py \
  --name "my-pipeline" \
  --purpose "What it does" \
  --domain engineering \
  --complexity 8 \
  --quality 9.0 \
  --skills "skill-1,skill-2" \
  --connectors "github,notion" \
  --format all
```

## Features

- **Sequential Thinking Enforcement** — 5-step chain on complex tasks
- **Skill Integration** — Maps 35+ skills across 7 categories
- **Connector Wiring** — GitHub, Notion, Supabase, Vercel, OpenRouter, Dropbox, Gmail
- **Quality Scoring** — 5-dimension scoring with 9+ target
- **Pipeline Generation** — YAML configs, markdown reports, JSON evidence

## Skill Categories

| Category | Skills |
|----------|--------|
| Engineering | helix-pro-code, compose-next, quality-gate, production-readiness-gate |
| Research | deep-research, super-research, arxiv |
| Security | semgrep, differential-review, supply-chain-risk-auditor |
| Data | data-analytics, build-report, visualize-data |
| Design | frontend-design, mega-web, design-blueprint |
| Memory | memory-unified, context-capsule, handoff-record |
| Orchestration | swarm-orchestrator, skill-connector-router, make-it-heavy |

## Connectors

| Connector | Type | Purpose |
|-----------|------|---------|
| GitHub | API | Repos, issues, PRs |
| Notion | API | Docs, databases |
| Supabase | Database | Postgres, auth |
| Vercel | Service | Deploy, edge |
| OpenRouter | API | LLM routing |
| Dropbox | Storage | Files |
| Gmail | API | Email |

## Quality Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Completeness | 20% | All aspects covered |
| Correctness | 25% | No errors, verifiable |
| Clarity | 20% | Unambiguous, well-structured |
| Confidence | 20% | Evidence-backed |
| Coherence | 15% | Logically consistent |

**Formula:** `score = Σ(dimension × weight)` → **Target: 9.0+**

## Sequential Thinking Chain

For complexity ≥ 7:

```
1. OBSERVE → What do I see?
2. ANALYZE → What does it mean?
3. HYPOTHESIZE → What might be true?
4. VERIFY → How can I confirm?
5. SYNTHESIZE → What's my conclusion?
```

## Output

- **JSON** — Machine-readable evidence
- **YAML** — Pipeline config
- **Markdown** — Human-readable report

## Structure

```
pipeline-architect/
├── SKILL.md                    # Spec
├── README.md                   # This file
├── scripts/
│   └── architect.py            # Meta-pipeline engine
├── templates/                  # Generated pipelines
├── skills/                     # Generated skills
└── references/                 # Documentation
```

## License

APEX Estate — GlacierEQ
