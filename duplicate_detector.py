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
