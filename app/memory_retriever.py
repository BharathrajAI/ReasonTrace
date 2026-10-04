def find_candidate_memories(claim: str, memories: list[str]) -> list[str]:
    """
    Find memories that share words with the claim.

    This is a simple prototype.
    We will replace this with a stronger retrieval method later.
    """

    claim_words = set(claim.lower().split())

    candidates = []

    for memory in memories:
        memory_words = set(memory.lower().split())

        if claim_words.intersection(memory_words):
            candidates.append(memory)

    return candidates


if __name__ == "__main__":

    claim = "Bharath currently lives in Bangalore."

    memories = [
        "Bharath lives in Chennai",
        "Bharath moved to Bangalore",
        "Bharath likes Python"
    ]

    candidates = find_candidate_memories(
        claim,
        memories
    )

    print("Candidate memories:")

    for memory in candidates:
        print("-", memory)