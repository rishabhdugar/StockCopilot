import requests
import json
import os


def chat_completion(system_message, user_message):
    url = "https://ausopenai.azure-api.net/openai/deployments/gpt-35-turbo-16k/chat/completions?api-version=2023-05-15"

    payload = json.dumps(
        {
            "messages": [
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ]
        }
    )
    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv("OPENAI_TOKEN"),
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(response.text)
        raise Exception("Error with OpenAI API")
