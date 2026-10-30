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
