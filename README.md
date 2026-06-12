# Copy Trading Bot

A GitHub-ready starter project for a Kotak Neo based copy-trading workflow.

## Overview

This repository currently includes:
- a Python backend starter in [backend](backend)
- a smoke-testable startup entry point in [backend/main.py](backend/main.py)
- an environment template in [backend/.env.example](backend/.env.example)
- CI setup in [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py --once
```

### Run tests

```bash
cd backend
python -m pytest -q
```

## Repository structure

```text
.
├── backend/              # Backend application and config
│   ├── main.py
│   ├── requirements.txt
│   ├── README.md
│   └── .env.example
├── .github/workflows/    # CI automation
└── LICENSE
```

## Notes

- The current backend is a working startup / smoke-test scaffold.
- Real trading logic and broker integration can be added on top of this foundation.
- Keep your real credentials in the local `.env` file and do not commit secrets.

## Disclaimer

This project is for learning and development use only. Trading involves financial risk. Test carefully before using real funds.

## License

MIT License — see [LICENSE](LICENSE).
