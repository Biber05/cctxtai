import click

from cctxtai.utils import create_logger
from cctxtai.utils.data import DataGenerator


@click.command()
@click.argument("filename")
def run(filename: str):
    log = create_logger(name="runner", log_lvl="DEBUG")
    try:
        data_gen = DataGenerator(source_file_path=filename)
        log.debug(f"Init DataGenerator from {filename}")
        data = data_gen()
        log.debug(data[0])
    except FileNotFoundError as e:
        log.error(e)


if __name__ == '__main__':
    run()
