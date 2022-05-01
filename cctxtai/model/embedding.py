from typing import Union, Dict, AnyStr, List

from txtai.embeddings import Embeddings


def create_embedding(data: Union[List[AnyStr], Dict], model_name: str = "sentence-transformers/nli-mpnet-base-v2"):
    embeddings = Embeddings({"path": model_name})
    if isinstance(data, list) is None:
        print(f"Use UIDs")
        embeddings.index([(uid, text, None) for uid, text in enumerate(data)])
    elif isinstance(data, Dict):
        print(f"Use custom ids")
        embeddings.index((idx, text, None) for idx, text in data.items())
    return embeddings


def save_embedding(embedding, filename: str):
    embedding.save(filename)


def load_embedding(filename: str):
    embeddings = Embeddings()
    embeddings.load(filename)
    return embeddings
