#!/usr/bin/env bash
set -e
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdir -p data
echo "Setup complete. Virtualenv activated. To activate: source .venv/bin/activate"
