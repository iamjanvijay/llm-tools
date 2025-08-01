#!/bin/bash

# Curl equivalent of the Python OpenAI client
# This makes the same API call to the vLLM server

curl -X POST "http://localhost:10010/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer EMPTY" \
  -d '{
    "model": "meta-llama/Llama-3.2-3B-Instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is your name?"}
    ],
    "temperature": 0.7,
    "max_tokens": 10000,
    "n": 5
  }' 