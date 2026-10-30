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
