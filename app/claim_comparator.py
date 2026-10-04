from llm_client import ask


def compare_claim(target_claim: str, answer: str) -> bool:

    prompt = f"""
You are evaluating whether an answer supports a target claim.

Target claim:
{target_claim}

Answer:
{answer}

Question:
Does the answer express the same meaning as the target claim?

Reply with ONLY one word:

YES

or

NO
"""

    result = ask(prompt).strip().upper()

    return result.startswith("YES")


if __name__ == "__main__":

    target_claim = "Bharath currently lives in Bangalore."

    answer = "He is currently based in Bangalore."

    result = compare_claim(
        target_claim,
        answer
    )

    print("Claim survives:", result)