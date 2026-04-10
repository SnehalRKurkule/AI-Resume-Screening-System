from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_similarity(resume, jd):
    emb1 = model.encode([resume])
    emb2 = model.encode([jd])
    return cosine_similarity(emb1, emb2)[0][0]