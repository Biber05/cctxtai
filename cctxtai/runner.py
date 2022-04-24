import click

from cctxtai.preprocessing.reader import DataGenerator
from cctxtai.preprocessing.transform import transform
from cctxtai.utils import create_logger


@click.command()
@click.argument("filename")
@click.argument("max_lines", default=-1)
def run(filename: str, max_lines: int):
    log = create_logger(name="runner", log_lvl="DEBUG")
    data = []
    try:
        data_gen = DataGenerator(source_file_path=filename)
        log.debug(f"Init DataGenerator from {filename}")
        data = data_gen(max_lines=max_lines)
    except FileNotFoundError as e:
        log.error(e)

    result = transform(data)



if __name__ == '__main__':
    run()
