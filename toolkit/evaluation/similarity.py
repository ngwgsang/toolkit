from sklearn.metrics.pairwise import cosine_similarity

def embedding_cosine(a, b):
    return cosine_similarity([a], [b])[0][0]

def average_embedding_similarity(embeddings1, embeddings2):
    scores = [embedding_cosine(e1, e2) for e1, e2 in zip(embeddings1, embeddings2)]
    return sum(scores) / len(scores)
