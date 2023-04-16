# Chatmaker

**Goal:** Easily convert any LLM python API call into a chatbot with a UX

Example provided using OpenAI's ChatCompletion API, but replaceable with another LLM model

Today, two UIs for the chatbot, CLI (with color, thanks to rich) or Local Webserver (using Flask)

## To operate
1. Set OPENAI_API_KEY environment variable
2. Decorate your chat function with @chatbot("cli") or @chatbot("web"), as detailed in the openai_example.py
