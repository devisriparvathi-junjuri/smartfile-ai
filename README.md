# 🧠 SmartFile AI — Intelligent File Organizer

**An AI-assisted file management application built with Python that organizes files, detects duplicates, and classifies text using machine learning.**

SmartFile AI helps users manage cluttered folders through automated file categorization, duplicate detection, and lightweight text classification in a simple web interface.

---

## ✨ Features

- 📂 **Automated File Organization** — Categorizes files into folders based on their extensions.
- 🔍 **Duplicate Detection** — Identifies duplicate files using SHA-256 hashing.
- 🤖 **Text Classification** — Uses TF-IDF vectorization and cosine similarity to classify text into predefined categories.
- 📊 **Interactive Dashboard** — Provides a user-friendly interface built with Streamlit.
- 🛡️ **Non-Destructive Duplicate Handling** — Skips duplicate destination filenames rather than overwriting existing files.
- 🐍 **Python-Based Architecture** — Uses modular Python files to separate application functionality.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Scikit-learn | Text vectorization and similarity analysis |
| SHA-256 | Duplicate file identification |
| Pandas | Data processing dependency |
| PyMuPDF | PDF-processing dependency for future extensions |

## 🏗️ Project Structure

```text
smartfile-ai/
├── app.py                  # Streamlit application
├── file_organizer.py       # File categorization and organization
├── ai_classifier.py        # TF-IDF text classification
├── duplicate_detector.py   # SHA-256 duplicate detection
├── requirements.txt        # Python dependencies
├── create_project.py       # Project file generator
├── .gitignore              # Git exclusions
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11 or later
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smartfile-ai.git
cd smartfile-ai
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local address displayed in your terminal to use the application.

## 🚀 How to Use

1. Launch the application.
2. Enter the path of a folder you want to inspect.
3. Review the number of files and their extensions.
4. Run duplicate detection to identify identical files.
5. Paste document text into the classification section to predict its category.
6. Use the organization feature to sort files into category folders.

> **Safety note:** Test file organization on a temporary folder containing copies of your files. The current implementation moves files and does not provide an automatic undo function.

## 🧠 How the Classification Works

SmartFile AI currently uses a lightweight similarity-based classification approach:

1. Converts example texts and user-provided text into TF-IDF vectors.
2. Calculates cosine similarity between the input and example texts.
3. Assigns the category of the most similar example.
4. Returns an uncertain category when no meaningful vocabulary overlap is detected.

**Current limitation:** This is a baseline text-classification technique, not a generative AI model. Its predictions depend on a small, predefined set of examples and may be inaccurate for unfamiliar documents.

## 🔍 Duplicate Detection

The duplicate detector calculates a SHA-256 hash for each file and groups files with matching sizes and hashes.

This helps identify files with identical contents, even when their filenames differ.

The application identifies duplicates but does not automatically delete them.

## 🔮 Future Improvements

- [ ] Content-based classification of PDF and text documents
- [ ] AI-powered document summarization
- [ ] Support for additional file categories
- [ ] Preview changes before organizing files
- [ ] Organization history and undo functionality
- [ ] Downloadable JSON and CSV reports
- [ ] Automated tests with Pytest
- [ ] Continuous integration with GitHub Actions
- [ ] Improved dashboard design and file statistics

## 🎯 Project Goals

SmartFile AI explores practical applications of Python automation and machine learning through a modular, extensible file management tool.

The project is intended as a learning and portfolio project for demonstrating Python development, basic NLP, file handling, and application design.

## 🤝 Contributing

Contributions, suggestions, and bug