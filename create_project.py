from pathlib import Path

root = Path.cwd()

files = {
    "app.py": r'''
import streamlit as st
from pathlib import Path
from file_organizer import organize_files
from duplicate_detector import find_duplicates
from ai_classifier import classify_text

st.set_page_config(page_title="SmartFile AI", page_icon="📂", layout="wide")

st.title("📂 SmartFile AI")
st.caption("Intelligent file organization powered by Python and machine learning.")

st.info("Choose a test folder first. Files will only be moved when you explicitly click Organize.")

folder = st.text_input("Folder path", placeholder=r"C:\Users\Devisri\Downloads")

col1, col2 = st.columns(2)

if folder and Path(folder).is_dir():
    with col1:
        st.subheader("📊 Folder overview")
        files = [p for p in Path(folder).iterdir() if p.is_file()]
        st.metric("Files found", len(files))
        st.write("File types:", len(set(p.suffix.lower() for p in files)))

    with col2:
        st.subheader("🔍 Duplicate detection")
        if st.button("Find duplicate files"):
            duplicates = find_duplicates(folder)
            if duplicates:
                for group in duplicates:
                    st.warning("Duplicate files:")
                    for item in group:
                        st.code(str(item))
            else:
                st.success("No duplicate files detected.")

    st.subheader("🧠 AI document classification")
    text = st.text_area("Paste document text to classify")
    if st.button("Classify text") and text.strip():
        category = classify_text(text)
        st.success(f"Predicted category: {category}")

    st.subheader("📁 Organize files")
    st.warning("This action moves files into category folders. Test on a copy of your files first.")
    if st.button("Organize files"):
        result = organize_files(folder)
        st.success(f"Organized {result} files.")
elif folder:
    st.error("That folder does not exist.")
else:
    st.write("Enter a folder path to get started.")
''',

    "file_organizer.py": r'''
from pathlib import Path
import shutil

CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf"},
    "Spreadsheets": {".csv", ".xlsx", ".xls"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Video": {".mp4", ".mov", ".avi", ".mkv"},
}

def get_category(path):
    suffix = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "Other"

def organize_files(folder):
    root = Path(folder).resolve()
    count = 0

    for item in list(root.iterdir()):
        if not item.is_file():
            continue

        category = get_category(item)
        destination_dir = root / category

        # Avoid overwriting an existing file.
        destination = destination_dir / item.name
        if destination.exists():
            continue

        destination_dir.mkdir(exist_ok=True)
        shutil.move(str(item), str(destination))
        count += 1

    return count
''',

    "duplicate_detector.py": r'''
from pathlib import Path
from collections import defaultdict
import hashlib

def file_hash(path):
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def find_duplicates(folder):
    root = Path(folder).resolve()
    groups = defaultdict(list)

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            groups[(path.stat().st_size, file_hash(path))].append(path)
        except (OSError, PermissionError):
            continue

    return [paths for paths in groups.values() if len(paths) > 1]
''',

    "ai_classifier.py": r'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EXAMPLES = [
    ("Technology software python programming computer database", "Technology"),
    ("Invoice payment budget finance revenue accounting", "Finance"),
    ("Resume career employment interview experience", "Career"),
    ("Assignment lecture examination course student education", "Education"),
    ("Recipe cooking ingredients food kitchen", "Food"),
    ("Doctor hospital medicine health patient", "Health"),
]

def classify_text(text):
    documents = [example[0] for example in EXAMPLES]
    labels = [example[1] for example in EXAMPLES]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents + [text])
    similarities = cosine_similarity(matrix[-1], matrix[:-1])[0]

    if similarities.max() == 0:
        return "Other / Uncertain"

    return labels[similarities.argmax()]
''',

    "requirements.txt": """streamlit
scikit-learn
pandas
pymupdf
""",

    ".gitignore": """venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
.env
""",

    "README.md": """# SmartFile AI

An intelligent file organization tool built with Python and Streamlit.

## Features
- Organize files by extension.
- Detect exact duplicate files using SHA-256 hashes.
- Classify pasted text using TF-IDF similarity.
- Inspect a folder through a web interface.

## Installation

    python -m pip install -r requirements.txt
    streamlit run app.py

## Limitations
The current classifier uses a small set of example texts and TF-IDF similarity. It is a baseline text-classification feature, not a large language model. File organization moves files, so test on a copy first.

## Technology
Python, Streamlit, scikit-learn, SHA-256.
""",
}

for name, content in files.items():
    path = root / name
    if path.exists():
        print(f"Preserved existing file: {name}")
    else:
        path.write_text(content.lstrip(), encoding="utf-8")
        print(f"Created: {name}")

print("\nProject generation complete!")
print("Run the app with: streamlit run app.py")
