from ollama import chat


MODEL_NAME = "qwen3:8b"


def ask(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False
    )

    return response.message.content


if __name__ == "__main__":
    prompt = "Explain what an LLM is in simple words."

    response = ask(prompt)

    print(response)