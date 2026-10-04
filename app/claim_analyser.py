def extract_claims(answer: str) -> list[str]:
    """
    Convert an answer into a list of claims.

    This is a simple prototype.
    We will improve it later.
    """

    claims = []

    if "Bangalore" in answer:
        claims.append("Bharath currently lives in Bangalore.")

    return claims


if __name__ == "__main__":

    answer = (
        "Based on the stored memories, Bharath moved to Bangalore. "
        "Therefore, Bharath currently lives in Bangalore."
    )

    claims = extract_claims(answer)

    print("Detected claims:")

    for claim in claims:
        print("-", claim)