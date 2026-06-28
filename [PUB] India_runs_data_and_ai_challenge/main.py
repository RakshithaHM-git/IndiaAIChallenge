import os
import json
from matcher import calculate_score
from openpyxl import Workbook

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIR = os.path.join(
    BASE_DIR,
    "India_runs_data_and_ai_challenge"
)

candidate_file = os.path.join(
    DATASET_DIR,
    "candidates.jsonl"
)

# -----------------------------
# Check dataset
# -----------------------------
if not os.path.exists(candidate_file):
    print("ERROR: candidates.jsonl not found!")
    print(candidate_file)
    exit()

print("=" * 60)
print("INDIA.RUN - Intelligent Candidate Discovery")
print("=" * 60)

print("\nLoading candidates...")

candidates = []

# -----------------------------
# Load candidates
# -----------------------------
with open(candidate_file, "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)
        candidate["score"] = calculate_score(candidate)
        candidates.append(candidate)

print(f"\nLoaded {len(candidates)} candidates successfully.")

# -----------------------------
# Sort candidates
# -----------------------------
candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTop 10 Candidates")
print("-" * 60)

for i, c in enumerate(candidates[:10], start=1):
    print(
        f"{i}. "
        f"{c['candidate_id']} | "
        f"{c['profile']['anonymized_name']} | "
        f"{c['profile']['current_title']} | "
        f"Score: {c['score']}"
    )

# -----------------------------
# Create Excel
# -----------------------------
print("\nCreating submission.xlsx...")

wb = Workbook()

ws = wb.active
ws.title = "Ranked Candidates"

ws.append([
    "Rank",
    "Candidate ID",
    "Candidate Name",
    "Current Role",
    "Score"
])

for rank, candidate in enumerate(candidates, start=1):
    ws.append([
        rank,
        candidate["candidate_id"],
        candidate["profile"]["anonymized_name"],
        candidate["profile"]["current_title"],
        candidate["score"]
    ])

output_file = os.path.join(BASE_DIR, "submission.xlsx")

wb.save(output_file)

print("\nSUCCESS!")
print("Excel file created successfully.")
print(output_file)