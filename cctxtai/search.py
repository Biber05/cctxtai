from pathlib import Path
from typing import List, Tuple

import click
from cctxtai.model.embedding import load_embedding


@click.command()
@click.argument("embedding_name")
@click.argument("text")
@click.argument("limit", default=3)
def _run(embedding_name: str, text: str, limit: int):
    embedding = load_embedding(Path.cwd().joinpath(f"data/20_embeddings/{embedding_name}").__str__())
    result: List[Tuple[int, float]] = embedding.search(text, limit=limit)
    _print(result)


def _print(result):
    for i, pred in result:
        with open(f"/Users/philipp/git/cctxtai/data/10_transformed/harry_potter/{i}", "r") as file:
            print(f"Prediction: {pred} \n"
                  f"Index: {i} \n"
                  f"============ \n"
                  f"{file.readline()}")


if __name__ == '__main__':
    _run()
