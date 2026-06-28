from docx import Document
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

doc_path = os.path.join(
    BASE_DIR,
    "India_runs_data_and_ai_challenge",
    "job_description.docx"
)

doc = Document(doc_path)

job_description = ""

for para in doc.paragraphs:
    job_description += para.text + "\n"

print(job_description)