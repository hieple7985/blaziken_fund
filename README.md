# Blaziken Fund - Dev Setup (Baseline)

This folder contains the early prototype for **Blaziken Fund** – a Pokémon RWA Fund Manager Agent for **Poketrade.fun** on **Base**, designed to be launched and grown through **CreatorBid**.

For now, the goal is to have a minimal, reproducible setup that can:
- create a Python virtual environment,
- install core dependencies for the agent backend,
- serve as the baseline for integrating onchain data, TCG meta signals, and CreatorBid/Base tooling.

## Prerequisites

- Python 3.10+

## Setup

```bash
cd hackathons/013-pokethon-1st-ai-agents/3_dev/blaziken_fund
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Further modules (agent engine, onchain adapters, simple UI) will be added iteratively on top of this baseline.
