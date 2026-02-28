import requests

# Hardcoded API key (for testing only)
OPENROUTER_API_KEY = "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"

def ask_health_bot(user_message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",  # Required by OpenRouter
        "X-Title": "Health Bot"  # Optional but recommended
    }
    
    payload = {
        "model": "google/gemini-2.0-flash-exp:free",  # Updated model name
        "messages": [
            {
                "role": "user",  # Gemini models don't support system role
                "content": (
                    "You are a health information assistant. "
                    "Do NOT diagnose or prescribe. "
                    "Only provide general health information.\n\n"
                    f"User question: {user_message}"
                )
            }
        ]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        # Print the actual error message from OpenRouter
        error_detail = response.json() if response.text else {}
        print(f"OpenRouter Error: {error_detail}")
        raise