import tempfile
from pathlib import Path

from file_organizer import get_category
from duplicate_detector import find_duplicates
from ai_classifier import classify_text


def test_file_category():
    assert get_category(Path("photo.jpg")) == "Images"
    assert get_category(Path("script.py")) == "Code"
    assert get_category(Path("notes.txt")) == "Documents"


def test_duplicate_detection():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "first.txt").write_text("same content", encoding="utf-8")
        (root / "second.txt").write_text("same content", encoding="utf-8")

        duplicates = find_duplicates(folder)

        assert len(duplicates) == 1
        assert len(duplicates[0]) == 2


def test_text_classification():
    result = classify_text(
        "Python programming software development databases technology"
    )
    assert result == "Technology"
