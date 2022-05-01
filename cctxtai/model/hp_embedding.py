from cctxtai.model.embedding import create_embedding, save_embedding
from cctxtai.preprocessing.hp_transform import TRANFORMED_DIR


def run():
    files = list(TRANFORMED_DIR.glob("*.txt"))
    data = dict()
    for file in files:
        with open(file, "r") as f:
            data[file.name] = f.read()
    embedding = create_embedding(data)
    save_embedding(embedding, TRANFORMED_DIR.parent.joinpath("20_embeddings").joinpath("harry_potter"))


if __name__ == '__main__':
    run()
