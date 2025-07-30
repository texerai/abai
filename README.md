# tai: Your terminal AI assistant 

Simple command-line chatbot framework supporting pluggable LLM APIs. I mostly work in terminals and got tired of switching back and forth to the browser just to ask something simple. This tool is a lightweight layer that connects to LLMs directly from the terminal — fast, distraction-free, and scriptable.

## Requirements

* Python 3.7+
* API client library (e.g., `openai`, `anthropic`, etc.)
* API key set as an environment variable (e.g., `LLM_API_KEY`)

## Install

Install the required client library based on your chosen provider. Example:

```bash
pip install openai  # or another client
```

## Set API Key

```bash
export LLM_API_KEY="your-api-key"
```

## Run

```bash
python abai.py
```

Type messages and get responses. Type `exit` to quit.

## Notes

* Change model/provider in the script as needed.
* Make sure to handle rate limits and quotas based on your provider.
* Abstract the API call logic for easy provider switching.
