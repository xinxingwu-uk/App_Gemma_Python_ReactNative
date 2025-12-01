# Hugging Face Gemma Client (Python)

This repository contains a minimal Python example that calls the **Gemma 2B Instruct** model (`google/gemma-2-2b-it`) through the **Hugging Face Inference Router** API.

The script:

- Sends a text prompt to the Hugging Face `/v1/chat/completions` endpoint  
- Receives the model’s reply  
- Prints the generated text to the console  

It’s meant as a **teaching / starter example** for using Hugging Face chat models in Python.

---

## Features

- Uses the `requests` library (no extra frameworks)
- Simple `query(prompt)` function you can reuse anywhere
- Configurable:
  - `model` name
  - `max_tokens`
  - `temperature`

---
---

## Requirements

- Python 3.8+
- A Hugging Face account
- A **Hugging Face Access Token** with Inference API permissions
- Python package:
  ```bash
  pip install requests

<hr>

# Gemma 2B Chat – React Native Demo

A super simple React Native app that talks to **Google Gemma 2B Instruct** through the **Hugging Face Inference Router**.  
You type a prompt, tap **Send**, and see the model’s response on your phone.

> This project is for learning/demo use. Do **not** commit real API keys to a public repository.

---

## Features

- Simple chat-style UI (one prompt → one response)
- Uses Hugging Face `chat/completions` endpoint
- Calls `google/gemma-2-2b-it` via `fetch`
- Loading spinner and basic error handling
- Beginner-friendly, single-file `App.js`

---

## Prerequisites

- Node.js (LTS recommended)
- React Native environment  
  - Easiest: [Expo CLI](https://expo.dev)  
- A Hugging Face account and an **API Access Token**

---

## Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
