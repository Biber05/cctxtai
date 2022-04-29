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


if __name__ == '__main__':
    with open("/Users/philipp/git/cctxtai/data/_test/wikipedia.txt", "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(line)
    e = create_embedding(lines[0:1_000])
    save_embedding(e, "/Users/philipp/git/cctxtai/data/20_embeddings/wikipedia")
    # result = e.search("Republic", 1)
    # print(result)
