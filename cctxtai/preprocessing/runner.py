import click
from cctxtai.preprocessing import PREPROCESSING_LOG
from cctxtai.preprocessing._reader import DataGenerator
from cctxtai.preprocessing._transform import transform
from cctxtai.preprocessing._writer import write_to_parquet
from cctxtai.model.embedding import create_embedding, save_embedding


@click.command()
@click.argument("filename")
@click.argument("max_lines", default=-1)
def run(filename: str, max_lines: int):
    data = []
    try:
        data_gen = DataGenerator(source_file_path=filename)
        PREPROCESSING_LOG.debug(f"Init DataGenerator from {filename}")
        data = data_gen(max_lines=max_lines)
    except FileNotFoundError as e:
        PREPROCESSING_LOG.error(e)

    result = transform(data)
    filename = filename.replace("00_raw", "10_transformed")
    filename = filename.replace("json", "parquet")
    texts = [x.content for x in result]

    write_to_parquet(result, filename)

    embedding = create_embedding(texts)
    save_embedding(embedding, "/Users/philipp/git/cctxtai/data/20_embeddings/openlegal")


if __name__ == '__main__':
    run()
