# Chat Stream – Real‑Time Community‑Sentiment Synthesizer

We live in an age where a single live‑stream can generate tens of thousands of chat messages per hour. Human moderators, analysts, and even streamers themselves cannot keep up, let alone spot the actionable threads of agreement, dissent, or fresh ideas hidden inside the torrent. **Chat Stream turns that flood into a rolling, two‑sentence “headline” with an explicit sentiment bar and a confidence score, refreshing twice per second.** The result is a heads‑up display for large‑scale conversation: producers get instant feedback loops, viewers see that their voice contributes, and downstream dashboards can trigger alerts or overlay statistics in real time.

### Value Proposition
*   **Speed & Scale** – Handles a sustained 20 messages/second (100× a typical Twitch chat) on commodity hardware or a medium cloud instance.  
*   **Transparency** – Outputs a confidence score plus exposure of raw bucket summaries for auditability—no black‑box claims.  
*   **Modularity** – Models are hot‑swappable at runtime; choose open‑weights offline models for privacy or paid LLM APIs for peak quality.  
*   **Cost Control** – Bucketing and fractal aggregation keep inference calls proportional to message entropy rather than volume, driving down token spend by 90 % in stress tests.  
*   **Interoperability** – Emits both JSON and WebSocket streams for easy overlay in OBS, Discord bots, or custom dashboards.

### High‑Level Architecture
stdin (raw chat) → ring‑buffer → topic & time bucketer
→ sentiment model (RoBERTa‑tiny) + summary model (Long‑T5 or OpenAI turbo)
→ snapshot assembler {summary, ±%, conf}
→ fractal aggregator (5 s → 1 min → 10 min)
→ sinks (CLI, WebSocket, Prometheus)

shell
Copy

### Repository Layout
TERMS.md contractual terms, milestones, and penalties
src/ reference Python 3.11 implementation
└── chatstream/
├── ingest.py async WebSocket / stdin readers
├── bucket.py time+semantic bucketing logic
├── models.py pluggable wrappers (local, HF, OpenAI)
├── aggregate.py fractal tree reducer
└── sinks.py CLI & WebSocket publishers
benchmarks/ latency + ROUGE evaluation harness
docs/ architecture diagrams & API schema (OpenAPI 3.1)
submissions/ folder where contractors place final artefacts

markdown
Copy

### Quick‑Start for Contributors
1. `make dev` spins up **Poetry**, **ruff**, and **pre‑commit**.  
2. Copy `.env.example` to `.env` and drop any API keys (optional).  
3. Run `python -m chatstream.demo` to follow a prerecorded YouTube chat dump and watch live summaries refresh in the terminal.  
4. Add a new model by subclassing `BaseModel` in `models.py`; hot‑swap with `--llm mymodel` at runtime.

### Definition of Done
The project is “done” when all criteria below are met and verified by the arbiter’s CI pipeline:

* Throughput ≥20 msgs/s sustained for 60 minutes on an 8 vCPU, 16 GB RAM VM; ≤200 ms 95ᵗʰ‑percentile end‑to‑end latency.  
* Average ROUGE‑L ≥0.25 against a 1 000‑window human‑curated gold set; macro‑F1 (pos/neg/neutral) ≥0.85 for sentiment.  
* Memory footprint <4 GB RSS during stress test; queue back‑pressure never exceeds 1 000 pending messages.  
* Hot‑swap demo: replace summarizer at runtime with no stream interruption (<2 seconds frozen output).  
* Complete code coverage ≥80 %, lint‑clean (`ruff --fix`) and type‑checked (`mypy --strict`).  
* Documentation: architecture diagram (SVG), API schema (OpenAPI), and operator run‑book (Markdown) all live in `docs/`.  
* Reproducible Docker build (`docker build . && docker run chatstream demo`) matches performance numbers.  
* All artefacts, benchmark logs, and a signed checksum bundle are pushed to `submissions/` for on‑chain hash anchoring.  
* The arbiter’s automated job tags the repo as `v1.0.0` and signs off in the Trustless Business interface.

### Roadmap Beyond v1
Post‑contract tickets (outside current scope) include multilingual support, toxicity filters, and a React overlay component.

### License & Governance
Dual‑licensed MIT + Business Source; model weights follow upstream licenses. Governance decisions (mode
