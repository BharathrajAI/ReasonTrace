from llm_client import ask
from memory_store import create_database, get_memory_texts


def build_prompt(question: str, memories: list[str]) -> str:
    memory_text = "\n".join(
        f"- {memory}" for memory in memories
    )

    prompt = f"""
You are an AI assistant with access to stored user memories.

Stored memories:
{memory_text}

User question:
{question}

Answer the question using the stored memories when they are relevant.
"""

    return prompt


def main():
    create_database()

    memories = get_memory_texts()

    question = "Where does Bharath currently live?"

    prompt = build_prompt(question, memories)

    answer = ask(prompt)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()