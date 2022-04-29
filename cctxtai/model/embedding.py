from txtai.embeddings import Embeddings


def create_embedding(data: [str], model_name: str = "sentence-transformers/nli-mpnet-base-v2"):
    embeddings = Embeddings({"path": model_name})
    embeddings.index([(uid, text, None) for uid, text in enumerate(data)])
    return embeddings


def save_embedding(embedding, filename: str):
    embedding.save(filename)


def load_embedding(filename: str):
    embeddings = Embeddings()
    embeddings.load(filename)
    return embeddings
