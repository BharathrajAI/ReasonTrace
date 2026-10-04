from llm_client import ask


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


def run_ablation(
    question: str,
    memories: list[str],
    remove_index: int
) -> str:

    remaining_memories = [
        memory
        for index, memory in enumerate(memories)
        if index != remove_index
    ]

    prompt = build_prompt(
        question,
        remaining_memories
    )

    answer = ask(prompt)

    return answer


if __name__ == "__main__":

    question = "Where does Bharath currently live?"

    memories = [
        "Bharath lives in Chennai",
        "Bharath moved to Bangalore",
        "Bharath likes Python"
    ]

    # Remove M2
    answer = run_ablation(
        question,
        memories,
        remove_index=2
    )

    print("\nRemoved memory:")
    print("-", memories[2])

    print("\nRemaining memories:")

    for index, memory in enumerate(memories):
        if index != 2:
            print("-", memory)

    print("\nLLM Answer:")
    print(answer)