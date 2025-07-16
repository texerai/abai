import os
import sys
import openai
from openai import OpenAI

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: The environment variable 'OPENAI_API_KEY' is not set.")
    sys.exit(1)

# Create client
client = OpenAI(api_key=api_key)

def chat_with_openai(prompt, model="gpt-4", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat.")
            break
        reply = chat_with_openai(user_input)
        print("Assistant:", reply)
