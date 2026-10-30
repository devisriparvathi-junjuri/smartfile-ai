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
