def calculate_score(candidate):
    score = 0

    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 30
    elif exp > 9:
        score += 20
    else:
        score += 10

    role = candidate["profile"]["current_title"].lower()

    if "ai" in role:
        score += 30
    elif "machine learning" in role:
        score += 30
    elif "data" in role:
        score += 20

    skills = [s["name"].lower() for s in candidate["skills"]]

    required = [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "sql",
        "aws"
    ]

    for skill in required:
        if skill in skills:
            score += 5

    return score