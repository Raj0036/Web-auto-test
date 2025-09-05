
# Adaptive Attack Simulator - GitHub-Ready Release

This repository contains a ready-to-upload Adaptive Attack Simulator skeleton.
**Intended for authorized testing only.** Do not run against targets you do not own or have permission to test.

## Quickstart
```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python aas_cli.py https://example.com
# or start web GUI:
python web_gui.py
```
Reports will be created in `reports/` (Markdown + JSON).

If you publish this repo publicly, **remove or replace** the `.env` file containing the pre-generated token to avoid leakage.
