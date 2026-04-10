import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])


def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def extract_skills(text):
    skills_list = [
        "python", "java", "sql", "excel", "power bi", "tableau",
        "machine learning", "deep learning", "nlp",
        "pandas", "numpy", "matplotlib", "seaborn",
        "html", "css", "javascript", "react",
        "aws", "azure", "gcp", "git", "c++", "c#", "ruby", "php", "go", "swift" , "kubernetes", "docker", "linux", "windows", "macos", "agile", "scrum", "kanban", "devops", "ci/cd", "tensorflow", "pytorch", "keras"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))