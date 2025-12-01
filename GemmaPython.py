import requests

# 1. Put your own Hugging Face token here
#    (Do NOT share this token or upload it to GitHub)
HF_TOKEN = "Your Token"

API_URL = "https://router.huggingface.co/v1/chat/completions"

def query(prompt):
    """Send a prompt to Gemma and get the reply text."""
    headers = {
        "Authorization": "Bearer " + HF_TOKEN,
        "Content-Type": "application/json",
    }

    payload = {
        "model": "google/gemma-2-2b-it",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 128,
        "temperature": 0.5,
    }

    # Send request to Hugging Face
    response = requests.post(API_URL, headers=headers, json=payload)

    # If something went wrong (4xx / 5xx), this will raise an error
    response.raise_for_status()

    data = response.json()

    # Take the text from the first choice
    return data["choices"][0]["message"]["content"]

# Example: ask the model something
answer = query("Write a program that prints numbers from 1 to 100.")
print(answer)

