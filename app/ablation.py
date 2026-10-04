from llm_client import ask
from claim_comparator import compare_claim

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

    return ask(prompt)


def run_all_ablations(
    question: str,
    memories: list[str]
):

    results = []

    for index, memory in enumerate(memories):

        print(f"\nTesting removal of M{index + 1}...")
        print("Removed:", memory)

        answer = run_ablation(
            question,
            memories,
            remove_index=index
        )

        results.append({
            "memory_index": index,
            "memory": memory,
            "answer": answer
        })

        print("Answer:", answer)

    return results

def analyze_ablation_results(
    results: list[dict],
    target_claim: str
):

    print("\n" + "=" * 50)
    print("REASONTRACE DIAGNOSIS")
    print("=" * 50)

    for result in results:

        memory_number = result["memory_index"] + 1
        ablated_answer = result["answer"]

        claim_survives = compare_claim(
            target_claim,
            ablated_answer
        )

        if claim_survives:
            status = "NOT NECESSARY"
        else:
            status = "INFLUENTIAL"

        print(f"\nM{memory_number}")
        print("Memory:", result["memory"])
        print("Answer:", ablated_answer)
        print("Claim survives:", claim_survives)
        print("Status:", status)

if __name__ == "__main__":

    question = "Where does Bharath currently live?"

    memories = [
        "Bharath lives in Chennai",
        "Bharath moved to Bangalore",
        "Bharath likes Python"
    ]

    print("\nRunning all memory ablations...")

    results = run_all_ablations(
        question,
        memories
    )

    print("\n" + "=" * 50)
    print("ABLATION RESULTS")
    print("=" * 50)

    for result in results:

        print(f"\nM{result['memory_index'] + 1}:")
        print("Memory:", result["memory"])
        print("Answer:", result["answer"])
        
    target_claim = "Bharath currently lives in Bangalore."

    analyze_ablation_results(
        results,
        target_claim
    )