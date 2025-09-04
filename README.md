# DavaX-Agents

This repo contains some OpenAI Agents python SDK examples.

## Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key exported as an environment variable: `ENDAVA_OPENAI_API_KEY`
- Google Gemini OpenAI API key exported as an environment variable: `GEMINI_API_KEY`

### Installation

1. Create virtual environment (recommended):

```bash
python -m venv .env
source .env/bin/activate  # On Windows: .env\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API keys:

```bash
export ENDAVA_OPENAI_API_KEY=your_api_key_here
export GEMINI_API_KEY=your_api_key_here
```

4. Install UV

```bash
pip install uv # Or: brew install uv
```

## Run Examples

Run python scripts from the `examples` folder.
