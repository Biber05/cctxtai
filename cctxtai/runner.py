import click

from cctxtai.preprocessing.reader import DataGenerator
from cctxtai.utils import create_logger


@click.command()
@click.argument("filename")
@click.argument("max_lines", default=-1)
def run(filename: str, max_lines: int):
    log = create_logger(name="runner", log_lvl="DEBUG")
    try:
        data_gen = DataGenerator(source_file_path=filename)
        log.debug(f"Init DataGenerator from {filename}")
        data = data_gen(max_lines=max_lines)
        log.debug(data[0])
    except FileNotFoundError as e:
        log.error(e)


if __name__ == '__main__':
    run()
